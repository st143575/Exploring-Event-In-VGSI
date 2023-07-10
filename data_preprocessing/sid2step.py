"""
Preprocessing for parsing step headlines.
"""

from argparse import ArgumentParser
import dill as pickle



def sid2step(input_dir:str, output_dir:str):
	"""
	Create a mapping from step_ids to step headlines and write it to sid2step.p file.

	Args:
		input_path:str  The path to the input data (i.e. articles_df.p).

        output_path:str The path to the output data (i.e. sid2step.p).
	"""

	# Load articles_df.
	articles_df = pickle.load(open(input_dir, 'rb'))

	# Create a list of all step headlines.
	all_steps = []
	for methods in articles_df['methods']:
	    for method in methods:
	        all_steps += method['steps']
	        
	# Build a mapping from step_ids to step headlines.
	sid2step = dict()
	for step in all_steps:
	    sid = step['step_id']
	    if sid not in sid2step:
	        sid2step[sid] = step['headline']

	print(len(all_steps), len(sid2step), '\n')

	# Write sid2step to sid2step.p file.
	print('Start writing sid2step...')
	with open(output_dir + 'sid2step.p', 'wb') as file:
	    pickle.dump(sid2step, file)
	print('Done!')



parser = ArgumentParser()
parser.add_argument('-i', '--input_dir', help='path to the input folder')
parser.add_argument('-o', '--output_dir', help='path to the output folder')

args = parser.parse_args()

parse(input_path=args.input_dir, output_path=args.output_dir)