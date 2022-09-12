import bs4 as bs
import extractive_text_summary
import urllib.request
import re

#scraped_data = urllib.request.urlopen("https://www.gutenberg.org/files/1400/1400-h/1400-h.htm")
#file = scraped_data.read()
#parsed_text = bs.BeautifulSoup(file, "lxml")
#paragraphs = parsed_text.find_all("p")
#book_text = ""
#for p in paragraphs:
#    book_text += p.text

def web_scrape(url : str):
    scraped_data = urllib.request.urlopen(url)
    file = scraped_data.read()
    parsed_text = bs.BeautifulSoup(file, "lxml")
    paragraphs = parsed_text.find_all("p")
    full_text = ""
    for p in paragraphs:
        full_text += p.text
    re.sub(r'\[[0-9]*\]', ' ', full_text)
    re.sub(r'\s+', ' ', full_text)

#print(extractive_text_summary.extractive_text_summary(web_scrape("https://www.gutenberg.org/files/1400/1400-h/1400-h.htm", 10)))

with open('great_expectations_ch1.rtf', 'r') as ge_ch1:
    ge_ch1_text = ge_ch1.read()
print(extractive_text_summary.extractive_text_summary(ge_ch1_text, 10))