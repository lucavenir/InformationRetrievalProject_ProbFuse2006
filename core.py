#!/usr/bin/env python
# -*- coding: utf-8 -*-

# helper functions to keep code organized
from lib.prob_fuse_lib import *

def main():
	# define folders used
	input_folder_path = "output/preprocessed_scores" # generated by preprocess.py
	output_folder_path = "output/probfuse/"
	param_file = "input/Xtparams.txt"

	x_choices, t_choices = extract_params(param_file)

	print()
	print("x: "+str(x_choices))
	print("t: "+str(t_choices))
	print()

	# quick check on folder existence and its content
	check_relevances_exist(input_folder_path)

	# x is the number of segmentes
	for x in x_choices:
		# t is the training set size, as a percentage of the queries
		for t in t_choices:
			# For each ProbFuse configuration, we want to try ProbFuseAll and ProbFuseJudged
			for judge in [True, False]:
				# calling the core function
				if judge:
					string_judge = "ProbFuseJudged"
				else:
					string_judge = "ProbFuseAll"
				print ("Combinining with parameters: N_SEGMENTS="+str(x)+", TRAINING_TOPICS="+str(t*50)+", "+string_judge)
				prob_fuse(input_folder_path, output_folder_path+string_judge+"_"+str(x)+"_"+str(t)+".res", x, t, judge)

	print()
	print("ProbFuse2006 done! Output files are in '" + output_folder_path + "'")
	

if __name__ == '__main__':
   main()

#