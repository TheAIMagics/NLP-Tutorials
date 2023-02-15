
import spacy

with open("./data/test.txt",'r',encoding="utf8") as f:
    text = f.read().replace('\n\n'," ").replace("\n",' ')
    chapters = text.split('CHAPTER ')[1:]

nlp = spacy.load('en_core_web_sm')

chapter1 = chapters[0]

doc = nlp(chapter1)

sentences = list(doc.sents)

sentence = sentences[1]

for word in sentence:
    if word.pos_ == 'VERB':
        print(word, "lemma=", word.lemma_)
