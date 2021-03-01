

# Reading the corpus
file = open('./brown/ca01')
file = file.read()

# Removing useless symbols
file = file.replace(" ``/``", '') \
    .replace("''/'' ",'') \
    .replace('(/( ','') \
    .replace(')/)','')
