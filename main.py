# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://www.sckans.edu/~sireland/radio/code.html")
# morse_table = driver.find_element(By.CSS_SELECTOR, "tbody")
# print(morse_table.text)
# driver.quit()
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.sckans.edu/~sireland/radio/code.html"

page = urlopen(url)
# print(page)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())
morse_table = soup.find_all('td')

morse_list = []
for td in morse_table:
    morse_list.append(td.text.strip())

letters = morse_list[:208:8]
codes = morse_list[1:208:8]
morse_dic = {letters[i]: codes[i] for i in range(len(letters))}
numbers = morse_list[208:-2:4]
numcodes = morse_list[209:-2:4]
num_dic = {numbers[i]: numcodes[i] for i in range(len(numbers))}
morse_dic.update(num_dic)
punctuation_list = [".", ",", ":", "?", "'", "-", "/", "(", '"']
puncodes = morse_list[211:-2:4]
punctuation_dic = {punctuation_list[i]: puncodes[i] for i in range(len(punctuation_list))}
morse_dic.update(punctuation_dic)

decode = input("Please type in the sentence you want decoded: ")

letter_list = [letter for letter in decode.upper()]

coded_word = " ".join([morse_dic[letter] for letter in letter_list if letter in morse_dic])

print(f"Your word/sentence in morse code is: {coded_word.replace('*', '.')}")

coded_letters = coded_word.split(" ")
# print(coded_letters)

# print(list(morse_dic.keys())[list(morse_dic.values()).index(code)])

uncoded_list = [list(morse_dic.keys())[list(morse_dic.values()).index(code)] for code in coded_letters if code in morse_dic.values()]

print(" ".join(uncoded_list))
