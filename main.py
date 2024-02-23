from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


def get_morse_dic():
    url = "https://www.sckans.edu/~sireland/radio/code.html"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')
    morse_table = soup.find_all('td')
    morse_list = [td.text.strip() for td in morse_table]
    punctuation_list = [".", ",", ":", "?", "'", "-", "/", "(", '"']
    punc_indx = 0
    let_indx = 0
    for index, val in enumerate(morse_list):
        if index <= 207:
            if len(val) == 1 or "*" in val or "-" in val and val != "X-ray":
                morse_list[let_indx] = val
                let_indx += 1
        else:
            if len(val) > 1 and "*" not in val and "-" not in val:
                morse_list[index] = punctuation_list[punc_indx]
                punc_indx += 1
    del morse_list[let_indx:208]
    morse_dic = dict(zip(morse_list[:-2:2], morse_list[1:-2:2]))
    return morse_dic


morse_dic = get_morse_dic()

str_to_decode = input("Please type in the sentence you want decoded: ")

chars_from_input = [char for char in str_to_decode.upper()]

word_in_morse = " ".join([morse_dic[char] for char in chars_from_input if char in morse_dic])

print(f"Your word/sentence in morse code is: {word_in_morse.replace('*', '.')}")

coded_char_list = word_in_morse.split(" ")

# Decodes the code by selecting the uncoded characters in morse_dic by the index of the corresponding morse value
# uncoded_list = [list(morse_dic.keys())[list(morse_dic.values()).index(morse_char)] for morse_char in coded_char_list if morse_char in morse_dic.values()]
# print(" ".join(uncoded_list))
