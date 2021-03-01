

# Reading the corpus
file = open('./brown/ca01')
file = file.read()

# Removing useless symbols
file = file.replace(" ``/``", '') \
    .replace("''/'' ",'') \
    .replace('(/( ','') \
    .replace(')/)','')

# Splitting into sentences by '.' (sby <==> split by)
sents_sby_dot = file.split('./.')

# Splitting by colon
sents_sby_dot_colon = []
for sent in sents_sby_dot:
    sents_sby_dot_colon += sent.split(':/:')

# Creating a list of tagged words for each sentence
sents_tagged_words = []
for sent in sents_sby_dot_colon:
    sents_tagged_words.append([tuple(word.split('/')) for word in sent.split()])
    
# Creating a list of tags for each sentence
sents_tags = []
for sent in sents_tagged_words:
    sents_tags.append([word[1] for word in sent])

# Creating a list of N-Grams for each sentence
sents_rules = []
from nltk import ngrams
for i in range(len(sents_tags)):
    sent_rules = []
    for j in range(2, len(sents_tags[i])):
        sent_rules += ngrams(sents_tags[i], j)
    sents_rules.append(sent_rules)

# Creating a frequency distribution dictionary of rules
rules_frequency_dict = {}
for sent in sents_rules:
    for rule in sent:
        if rule in rules_frequency_dict:
            rules_frequency_dict[rule] += 1
        else:
            rules_frequency_dict[rule] = 1