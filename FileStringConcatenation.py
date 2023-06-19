from itertools import product

with open('inquiries.txt', 'r') as i:
    inquiries = [line.strip() for line in i]
with open('utterances.txt', 'r') as u:
    utterances = [line.strip() for line in u]

# concatenate randomly
sentences = []
for sent1, sent2 in product(utterances, inquiries):
    sentences.append(sent2 + " " + sent1)

with open('concatenated.txt', 'w+') as c:
    for sent in sentences:
        c.write(sent + "," + "\n")