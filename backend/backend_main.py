from nltk import ngrams
from nltk.corpus import brown
from nltk import UnigramTagger
from nltk import NgramTagger
from nltk import DefaultTagger
from pickle import load
from nltk.tokenize import word_tokenize
import re
from nltk.parse import RecursiveDescentParser, EarleyChartParser
import nltk

def read_file(path):
    # Reading the corpus
    file = open(path)
    file = file.read()
    return file

def get_tags(file, words=False):
    # Removing useless symbols
    #print(file)
    file = file.replace("``/``", '') \
        .replace("''/''",'') \
        .replace('(/(','') \
        .replace(')/)','') \
        .replace("``/``",'') \
        .replace('--/--','') \
        .replace(';/;','') \
        .replace('?','.') \
        .replace('!','.') \
        .replace(',/,','') \
        .replace('\\/\\','')
    
    # Splitting into sentences by '.' (sby <==> split by)
    sents_sby_dot = file.split('./.')
    
    # Splitting by colon
    sents_sby_dot_colon = []
    for sent in sents_sby_dot:
        sents_sby_dot_colon += sent.split(':/:')
    # Creating a list of tags for each sentence
    sents_tags = []
    if words:
        for sent in sents_sby_dot_colon:
            sent_tags = []
            for word in sent.split():
                word_tag = tuple(word.split('/'))
                if len(word_tag) == 2:
                    sent_tags.append(word_tag)
            sents_tags.append(sent_tags)
    else:
        for sent in sents_sby_dot_colon:
            tags = []
            for word in sent.split():
                word_tag = tuple(word.split('/'))
                if len(word_tag) == 2:
                    tags.append(word_tag[1])
            sents_tags.append(tags)
    
    # Remove void sentences
    for sent in sents_tags:
        if len(sent) == 0:
            sents_tags.remove(sent)
    return sents_tags

def n_gram_extraction_one_sent(sent_tags, uni_bi_grams):
    # Creating a list of N-Grams for each sentence
    
    
    sent_rules = []
    if len(sent_tags) < 30:
        for j in range(uni_bi_grams, len(sent_tags)):
            sent_rules += ngrams(sent_tags, j)
    #return sorted(sent_rules, key=lambda item: len(item), reverse=True)
    return sent_rules

def n_gram_extraction(sents_tags, uni_bi_grams=2):
    # Creating a list of N-Grams for each sentence
    sents_rules = []
    for i in range(len(sents_tags)):
        sents_rules.append(n_gram_extraction_one_sent(sents_tags[i], uni_bi_grams))
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
        
##############################################################################
def induce_grammar(file):
    # Get a list of tags of each sentence
    sents_tags = get_tags(file)
    # Get N-grams
    n_g = n_gram_extraction(sents_tags)
    # Get Frequency distribution
    freq = frequency_distribution(n_g)
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
        
    for i in sents_tags:
        rules.append(('NT' + str(len(rules)+1), ' '.join(i)))
        
    return rules, freq, len(sents_tags)

##############################################################################

def my_brown_tagger():
    
    
    # sample = brown.tagged_sents(categories=['news', 'editorial', 'reviews', 'religion', 'humor', 'science_fiction', 'adventure', 'lore', 'mystery', 'romance'])
    # default_tagger = DefaultTagger('NN')
    # uni_tagger = UnigramTagger(sample, cutoff=0, backoff=default_tagger)
    # quad_tagger = NgramTagger(4, sample, cutoff=0, backoff=uni_tagger)
    
    # from pickle import dump
    # output = open('../Tagger/my_tagger.pkl', 'wb')
    # dump(quad_tagger, output, -1)
    # output.close()
    
    input_ = open('../Tagger/my_tagger.pkl', 'rb')
    quad_tagger = load(input_)
    input_.close()
    return quad_tagger

def tag_sentence(sent):
    sent = word_tokenize(sent)
    my_tagger = my_brown_tagger()
    t = my_tagger.tag(sent)
    text=""
    for i in t:
        text1= i[0].lower()+'/'+i[1].lower()+' '
        text+=text1
    return text

def get_grammar_str(grammar, s_content_length=None):
    print(grammar)
    for i in  grammar: 
        if len(i[1].split()) != 2:
            print(i)
    gram_str = 'S ->'
    
    # for i in range(-1, s_content_length, -1):
    #     gram_str = gram_str + ' ' + grammar[i][0] + ' |'
        
    for i in grammar:
        gram_str = gram_str + ' ' + i[0] + ' |'
    
    gram_str = gram_str + '\n'
    for i in grammar:
        left=i[0]
        right=''
        right_list=i[1].split()
        if re.search('NT[0-9]+',right_list[0]):
            right=right_list[0]
        else:
            #right="'"+right_list[0]+"'"
            right="\""+right_list[0]+"\""
        if re.search('NT[0-9]+',right_list[1]):
            right=right + " "  + right_list[1]
        else:
            #right=right + " " + "'"+right_list[1]+"'"
            right=right + " " + "\""+right_list[1]+"\""
        gram_str=gram_str+left+' -> '+right+'\n'
    return gram_str

def inference_nltk(grammar,list_of_tags, s_content_length=None):
    
    my_str_gram=get_grammar_str(grammar, s_content_length)
    # print(my_str_gram)
    # file=open('h_grammar.txt',"w")
    # file.write(my_str_gram)
    
    my_str_gram=nltk.CFG.fromstring(my_str_gram)
    #rd = RecursiveDescentParser(my_str_gram)
    rd = EarleyChartParser(my_str_gram)
    worked = False
    results = []
    error = False
    try:
        for i in rd.parse(list_of_tags):
            worked = True
            results.append(i)
            #print(i)
    except ValueError:
        error = True
    
    return worked, results, error
