"""
Dependency parsing on step headlines with supar.
"""

from argparse import ArgumentParser
# packages for supar
from supar import Parser
# packages for seralizing and de-seralizing python objects
import dill as pickle


def parse(input_path:str, output_path:str):
    """
    Do dependency parsing on the step headline sentences of articles.
    
    Args:
        input_path:str  The path to the input data (i.e. articles_df.p).

        output_path:str The path to the output data (i.e. sid2stepdeptree_i.p).
    """

    # Load sid2step.p file.
    sid2step = pickle.load(open('sid2step.p', 'rb'))

    # Build a list of all step_ids.
    keys = list(sid2step.keys())

    # Load roberta-based biaffine dependency parser via supar.
    parser = Parser.load('biaffine-dep-roberta-en')


    print("Start parsing...\n")

    # Parse the third 100,000 steps(200000-299999).
print("Parse the third 100,000 step headlines(200000-299999).\n")
    sid2parse_step_3 = dict()
    for sid in keys[200000:300000]:
        if sid not in sid2parse_step_3:
            print(sid, sid2step[sid])
            sid2parse_step_3[sid] = parser.predict(sid2step[sid], lang='en', prob=True, verbose=False)
            print(sid, "parsed.\n")
            
    # Write the deptrees for the third 100,000 step headlines to sid2stepdeptree_3.p file.
    print("Parsing finished. Start writting sid2stepdeptree_2.p file.\n")
    with open(output_path + '/sid2stepdeptree_3.p', 'wb') as file:
        pickle.dump(sid2parse_step_3, file)
    print("sid2stepdeptree_3.p writting finished.\n")


parser = ArgumentParser()
parser.add_argument('-i', '--input_dir', help='path to the input folder')
parser.add_argument('-o', '--output_dir', help='path to the output folder')

args = parser.parse_args()

parse(input_path=args.input_dir, output_path=args.output_dir)
