import spacy
nlp = spacy.load('en')
doc = nlp(u'London is a big city in the United Kingdom.')
print "lmao"
for ent in doc.ents:
    print "lol"
    print(ent.label_, ent.text)