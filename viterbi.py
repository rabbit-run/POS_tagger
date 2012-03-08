#!/usr/bin/env python
# encoding: utf-8
"""
Viterbi.py

Created by Zehua Mai on 2012-03-01.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

from __future__ import division
import pickle
from math import log
import sys

class Viterbi:
    def __init__(self):
        with open('likelihood.pkl', 'rb') as output_likelihood:
            self.likelihood_table = pickle.load(output_likelihood)
        with open('prior_prob.pkl', 'rb') as output_prior_table:
            self.prior_prob_table = pickle.load(output_prior_table)
        with open('tags.pkl', 'rb') as output_tags:
            self.tags = pickle.load(output_tags)
        with open('vocabulary.pkl', 'rb') as output_vocabulary :
            self.vocabulary = pickle.load(output_vocabulary)
    
    def check_OOV(self, word):
        if word not in self.vocabulary:
            if word[-1] == 's':
                self.likelihood_table['NNS'][word] = \
                        min(self.likelihood_table['NNS'].values())
                self.likelihood_table['VBZ'][word] = \
                        min(self.likelihood_table['VBZ'].values())
            else:
                self.likelihood_table['NN'][word] = \
                        min(self.likelihood_table['NN'].values())
                self.likelihood_table['JJ'][word] = \
                        min(self.likelihood_table['JJ'].values())
    
    def prior_prob(self,currentState, previousState):
        if previousState not in self.prior_prob_table[currentState]:
            return min(self.prior_prob_table[currentState].values()) / 2
        else:
            return self.prior_prob_table[currentState][previousState] 
    
    def likelihood(self,word, tag):
        if word not in self.likelihood_table[tag]:
            return 0
        else:
            return self.likelihood_table[tag][word]
    
    def go(self, sentence):
        viterbi = [{}]
        path={}
        
        # initialize
        for tag in self.tags:
            self.check_OOV(sentence[0])
            if 'start' in self.prior_prob_table[tag] and \
                self.likelihood(sentence[0], tag) != 0:
                viterbi[0][tag] = log(self.prior_prob_table[tag]['start']) + \
                             log(self.likelihood(sentence[0], tag))
            path[tag] = [tag]
        
        
        # run viterbi 
        for wordIndex in range(1, len(sentence)):
            viterbi.append({})
            newpath = {}
            
            word = sentence[wordIndex]
            # Uncomment the following line to make it case insensitive
            # word = word.lower()
            self.check_OOV(word)
            
            for currentState in self.tags:
                if self.likelihood(word, currentState) != 0:
                    (prob, state) = max([(viterbi[wordIndex -1][previousState] + \
                            log(self.prior_prob(currentState,previousState)) + \
                            log(self.likelihood(word, currentState)), previousState)  \
                            for previousState in viterbi[wordIndex -1]]) 
                    viterbi[wordIndex][currentState] = prob
                    newpath[currentState] = path[state] + [currentState]
                    
            path = newpath
        # final step
        (prob, state) = max([(viterbi[len(sentence) - 1][lastTag], lastTag)
                                for lastTag in viterbi[len(sentence) - 1]])
        return path[state]
            
        
        
        
        
        
        
        
        
        
        
        