import spacy
from spacy import displacy

with open("./data/test.txt",'r',encoding="utf8") as f:
    text = f.read().replace('\n\n'," ").replace("\n",' ')
    chapters = text.split('CHAPTER ')[1:]

nlp = spacy.load('en_core_web_sm')

chapter1 = chapters[0]

doc = nlp(chapter1)

sentences = list(doc.sents)

sentence = sentences[8]
 
'''html = displacy.render(doc, style= "ent")

with open("visualize.html","w") as f:
    f.write(html)'''

# Customizing visualizations
#colors = {"PERSON":"#4E0000"}
colors = {"PERSON":"linear-gradient(90deg,#aa9cfc,#fc9ce7)"}
options = {"ents":['PERSON'], 'colors':colors}

html = displacy.render(doc, style= "ent",options=options)

with open("visualize.html",'w') as f:
    f.write(html)