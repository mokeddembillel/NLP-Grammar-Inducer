

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
