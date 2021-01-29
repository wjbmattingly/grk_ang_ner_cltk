#requisites
import spacy

#loads the model
nlp = spacy.load("models/oe_ner")

#reads in the sample text
with open ("texts/beowulf.txt", "r", encoding="utf-8") as f:
    text = f.readlines()[0:100]
    text = ''.join([i for i in text if not i.isdigit()])

#creates the doc object of the text
doc = nlp(text)

#writes results to a file
with open ("results/oe_results.txt", "w", encoding="utf-8") as f:
    #iterates over the entities in the doc object
    for ent in doc.ents:
        f.write(f"{ent.text}, {ent.label_}\n")
