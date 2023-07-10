"""
Dependency parsing on goals with supar.
"""

from argparse import ArgumentParser
# packages for supar
from supar import Parser
# packages for seralizing and de-seralizing python objects
import dill as pickle



def parse(input_path:str, output_path:str):
    """
    Do dependency parsing on the goal sentences of articles.
    
    Args:
        input_path:str  The path to the input data (i.e. articles_df.p).

        output_path:str The path to the output data (i.e. fid2goaldeptree.p).
    """

    # Load articles_df.
    articles_df = pickle.load(open(input_path, 'rb'))

    # Load dependency parser via supar.
    # The pretrained biaffine-dep-roberta-en(2.6G) is stored in .cache/supar.
    parser = Parser.load('biaffine-dep-roberta-en')

    print("Start parsing...\n")


    # Parse the goals and store the result to fid2deptree.
    fid2deptree = dict()
    print("Parse the 53187 goal sentences.\n")
    for fid, goal in zip(articles_df['file_id'], articles_df['goal']):
        if fid not in fid2deptree:
            print(fid, goal)
            fid2deptree[fid] = parser.predict(goal, lang='en', prob=True, verbose=False)
            print(fid, "parsed.\n")

    # Write the result to the fid2goaldeptree.p file.
    print("Parsing finished. Start writting fid2goaldeptree.p file.\n")
    with open(output_path + 'fid2goaldeptree.p', 'wb') as file:
        pickle.dump(fid2deptree, file)
    print("fid2goaldeptree.p writting finished.")


parser = ArgumentParser()
parser.add_argument('-i', '--input_dir', help='path to the input folder')
parser.add_argument('-o', '--output_dir', help='path to the output folder')

args = parser.parse_args()

parse(input_path=args.input_dir, output_path=args.output_dir)