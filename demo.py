import spacy

with open("./data/test.txt",'r',encoding="utf8") as f:
    text = f.read().replace('\n\n'," ").replace("\n",' ')
    chapters = text.split('CHAPTER ')[1:]

nlp = spacy.load('en_core_web_sm')

chapter1 = chapters[0]

doc = nlp(chapter1)

sentences = list(doc.sents)

sentence = sentences[2]

ents = list(sentence.ents)
'''print(ents[0].label)
print(ents[0].label_)
print(ents[0].text)
'''
people = []
doc_ents = list(doc.ents)

#NER
for ent in doc_ents:
    if ent.label_ == 'PERSON':
        people.append(ent)

# POS
for token in sentence:
    print(token.text, token.pos_)

# Noun and Noun Chunks
nouns = []

for token in sentence:
    if token.pos_ == 'NOUN':
        nouns.append(token)
#print("NOUN=",nouns)

print(list(doc.noun_chunks))
