#!/usr/bin/env python
# encoding: utf-8
"""
preprocess.py

Created by Zehua Mai on 2012-03-03.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

class Preprocessor(object):
    def __init__(self, fileName):
        self.fileName = fileName
        self.sentences = []
    
    def splitSenteces(self):
        f = open(self.fileName, 'r')
        sent = []
        for line in f:
            if line.rstrip():
                sent.append(line.rstrip())
            else:
                self.sentences.append(sent)
                sent = []
        f.close()
        
        
    def getSentences(self):
        if not self.sentences:
            self.splitSenteces()
        return self.sentences
        

