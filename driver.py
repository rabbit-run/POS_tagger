#!/usr/bin/env python
# encoding: utf-8
"""
driver.py

Created by Zehua Mai on 2012-03-03.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import optparse
from preprocess import Preprocessor
from viterbi import Viterbi
import viterbi_util

def main():
    p = optparse.OptionParser()
    p.add_option('-r', action = 'store_true', dest = "redo", default = False)
    opts, args = p.parse_args()
    
    output_file = ''
    if len(args) == 1:
        fileName = args[0]
    elif len(args) == 2:
        fileName = args[0]
        output_file = args[1]
    elif not args:
        sys.stderr.write("Error: please specify a file name\n")
        raise SystemExit(1)
    elif len(args) > 2:
        sys.stderr.write("Error: too much argument\n")
        raise SystemExit(1)
    
    # split the sentences
    processor = Preprocessor(fileName)
    sentences = processor.getSentences()
    
    # create the likelihood table, prior probability table and so on
    if opts.redo or not (os.path.isfile("likelihood.pkl")
        and os.path.isfile("prior_prob.pkl")
        and os.path.isfile("tags.pkl")
        and os.path.isfile("vocabulary.pkl")):
        viterbi_util.compute_table("training.pos")
        
    # run viterbi algorithm
    viterbi = Viterbi()
    output = []
    
    for sentence in sentences:
       tag_seq = viterbi.go(sentence)
       output.append((sentence, tag_seq))
    
    # write the result into a file
    viterbi_util.write_out(output, output_file)

    
if __name__ == '__main__':
    main()

