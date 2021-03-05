def read_file(path):
    # Reading the corpus
    file = open(path)
    file = file.read()
    return file

def get_tags(file):
    # Removing useless symbols
    #'\'','\"','.',';','^','~~','``',':',')','(','[',']','{','}','\'\'',','
    #file = re.sub('``/``|''/''|(/(|)/)|,/,|*/*|\/\|;/;', '', file)
    file = file.replace("``/``", '') \
        .replace("''/''",'') \
        .replace('(/(','') \
        .replace(')/)','') \
        .replace(',/,','') \
        .replace("``/``",'') \
        .replace('--/--','') \
        .replace(';/;','') \
        .replace('\\/\\','')
    
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
    return sents_tags

def n_gram_extraction(sents_tags):
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
    return sorted(rules_frequency_dict.items(), key=lambda item: item[1], reverse=True)

def get_max_n_gram(frequency_distribution):
    max_n_gram = frequency_distribution[0]
    return ' '.join(max_n_gram[0])


def substitution(sents_tags, rule_name, rule_tags):
    for i in range(len(sents_tags)):
        sent_str = ' '.join(sents_tags[i])
        # Replace in the middle of the sentence
        sent_str = sent_str.replace(' ' + rule_tags + ' ', ' ' + rule_name + ' ')
        # Replace at the start of the sentence
        if (sent_str.startswith(rule_tags + ' ')):
            sent_str = rule_name + ' ' + sent_str[len(rule_tags + ' '):]
        # Replace at the end of the sentence
        if (sent_str.endswith(' ' + rule_tags)):
            sent_str = sent_str[: -len(' ' + rule_tags)] + ' ' + rule_name 
        sents_tags[i] = sent_str.split()
    return sents_tags
        
def induce_grammar(file):
    # Get a list of tags of each sentence
    sents_tags = get_tags(file)
    # Get N-grams
    n_grams = n_gram_extraction(sents_tags)
    # Get Frequency distribution
    freq = frequency_distribution(n_grams)
    # Define rules list
    rules = []
    while True:
        # Get N-grams of each sentence
        n_grams = n_gram_extraction(sents_tags)
        # Get Frequency distribution list
        frequency_distribution_list = frequency_distribution(n_grams)
        # Break if finished
        if len(frequency_distribution_list) == 0:
            break
        # Append the most frequent rule
        rules.append(('NT' + str(len(rules)+1), get_max_n_gram(frequency_distribution_list)))
        # Substitution in tags of each sentence
        sents_tags = substitution(sents_tags, rules[-1][0], rules[-1][1])
    return rules,freq

def get_predecessor(rule):
    # Helper function used in Equation 3 
    sub_rule=[]
    for i in range(len(rule)-1):
        sub_rule.append(rule[i])
    sub_rule = tuple(sub_rule)
    return sub_rule

def get_frequency(frequencies,rule):
    # Get Frequency of rule
    for frequency in frequencies:
        if frequency[0] == rule:
            return frequency[1]
    return 0
