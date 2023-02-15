import spacy
import re

with open("./data/test.txt",'r',encoding="utf8") as f:
    text = f.read().replace('\n\n'," ").replace("\n",' ')
    chapters = text.split('CHAPTER ')[1:]
    chapter1 = chapters[2]

def find_sents(text= chapter1):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    sentences = list(doc.sents)
    return (sentences)

def find_quotes(text):
    quotes = re.findall(r" '(.*?)'",text)
    return (quotes)


found_sents = find_sents()

for sent in found_sents:
    str_sent = str(sent)
    #print(str_sent)
    found_quotes = find_quotes(str_sent)
    print(found_quotes)
    if len(found_quotes) >0:
        print(found_quotes)