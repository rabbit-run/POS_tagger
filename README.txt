
#########################
#                      ##
#   NLP Homework 4     ##
#                      ##
#########################

Zehua Mai     N15096707

#################

contained files:

README.txt		this file
driver.py			the main method, runs the whole program
preprocess.py	preprocess the input file, split the sentences
viterbi.py			this file implemented viterbi algorithm
viterbi_util.py		this contains utility method 
training.pos		training file, used to compute the likelihood table and prior probability table
likelihood.pkl		pickled data, likelihood table
prior_prob.pkl	pickled data, prior probability table
tags.pkl			pickled data, all the tags appeared in training data
vocabulary.pkl	pickled data, all the words appeared in the training data

#################

Instructions:

To run the program:

root$  python driver.py input_filename [output_filename]

output_filename is optional, the default output file name is "sys.txt"

I have already computed the prior probability table, likelihood table etc. and pickled them so the program can use them directly
However, if you want, you can use the following command to generate these data again.

root$  python driver.py -r input_filename [output_filename]

#################

Notes:

1. the tag senquence's probability tends to 0, which will lead to underflow. so I computed the logarithm of the possibility and add them up.

2. I tried to transfer all the words to lowercase, make them case insensitive. So the leading word will not be considered as a different word. However, the result was poor -- 5% lower than the original way.



