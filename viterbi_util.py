from __future__ import division
import sys
import pickle

def compute_table(filename):
    #filename = "training.pos"
    f = open(filename, 'r')
    tag_count = {'start' : 0}
    vocabulary = []
    likelihood_table = {}
    prior_prob_table = {}
    prior_tag = 'start'
    
    for line in f:
        if not line.isspace():
            (word, sep, tag) = \
                line.rstrip().partition('\t')
            
            # Uncomment the following line to make it case insensitive
            # word = word.lower()
            
            if word not in vocabulary:
                vocabulary.append(word)
            
            if tag in tag_count:
                tag_count[tag] += 1
            else:
                tag_count[tag] = 1
            
            if tag in prior_prob_table:
                if prior_tag in prior_prob_table[tag]:
                    prior_prob_table[tag][prior_tag] += 1
                else:
                    prior_prob_table[tag][prior_tag] = 1
            else:
                prior_prob_table[tag] = {prior_tag : 1}
            prior_tag = tag
            
            
            if tag not in likelihood_table:
                likelihood_table[tag] = {word : 1}
            else:
                if word not in likelihood_table[tag]:
                    likelihood_table[tag][word] = 1
                else:
                    likelihood_table[tag][word] += 1
        else:   
            tag_count['start'] += 1
            prior_tag = 'start'
    
    f.close()
    
    for tag, word in likelihood_table.iteritems():
        for w in word:
            word[w] = word[w]/tag_count[tag]
    
    for tag, priors in prior_prob_table.iteritems():
        for k in priors:
            priors[k] = priors[k]/tag_count[k]
    
    with open('likelihood.pkl', 'wb') as output_likelihood:
        pickle.dump(likelihood_table, output_likelihood, -1)
    
    with open('prior_prob.pkl', 'wb') as output_prior_table:
        pickle.dump(prior_prob_table, output_prior_table, -1)
        
    with open('tags.pkl', 'wb') as output_tags:
        tags = tag_count.keys()
        tags.remove('start')
        pickle.dump(tags, output_tags, -1)
        
    with open('vocabulary.pkl', 'wb') as output_vocabulary :
        pickle.dump(vocabulary, output_vocabulary, -1)
        
    
    
def write_out(output, fileName):
    if fileName:
        name = fileName
    else:
        name = 'sys.txt'
    
    formatted_strings = []
    for sentence, tag_seq in output:
        for index in range(0, len(sentence)):
            s = "%s\t%s\n" % (sentence[index], tag_seq[index])
            formatted_strings.append(s)
        formatted_strings.append('\n')
    
    with open (name, 'w') as output_file:
        output_file.writelines(formatted_strings)
        
    
    
    
    
    
    
    
