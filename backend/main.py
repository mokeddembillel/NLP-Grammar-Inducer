
def read_file(path):
    # Reading the corpus
    file = open(path)
    file = file.read()
    return file

def n_gram_extraction(file):
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
    
    # Creating a list of tags for each sentence
    sents_tags = []
    for sent in sents_sby_dot_colon:
        sents_tags.append([word.split('/')[1] for word in sent.split()])
    
    # Creating a list of N-Grams for each sentence
    sents_rules = []
    from nltk import ngrams
    for i in range(len(sents_tags)):
        sent_rules = []
        for j in range(2, len(sents_tags[i])):
            sent_rules += ngrams(sents_tags[i], j)
        sents_rules.append(sent_rules)
    return sents_rules

def frequency_distribution(n_grams):
    # Creating a frequency distribution dictionary of rules
    rules_frequency_dict = {}
    for sent in n_grams:
        for rule in sent:
            if rule in rules_frequency_dict:
                rules_frequency_dict[rule] += 1
            else:
                rules_frequency_dict[rule] = 1
    return rules_frequency_dict


file = read_file('./brown/ca01')

n_grams = n_gram_extraction(file)

rules_frequency_dict = frequency_distribution(n_grams)

