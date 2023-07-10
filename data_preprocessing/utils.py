import os, sys
import json


def check_config():
    if 'CONDA_DEFAULT_ENV' in os.environ:
        print("Current environment: conda")
        print(os.envrion['CONDA_DEFAULT_ENV'])
    else:
        if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
            print("Current environment: virtualenv.  Path:'%s'" % sys.prefix)
        else:
            print("Outside a virtualenv.")
    print("Shell:", os.environ['SHELL'])
    print("Current path:", os.getcwd())
    print("GPUs:", os.environ['CUDA_VISIBLE_DEVICES'])


def load_text(mode='cased' : str, path : str):
    """
    Load the textual input from the json file.
    
    @param mode:str  Specify whether the text should keep cased or be converted to uncased text.
                     Default: 'cased': keep the text cased as in the json file.
    @param path:str  path of the json file.
    @returns articles:list[dict]  A list of article objects in the form of dictionaries.
    """

    articles = []
    for line in open(path, 'r'):
        # If mode == 'cased', then keep the cased texts as they are.
        if mode == 'cased':
            articles.append(json.loads(line))
        # If mode == 'uncased', then convert all texts to lowercase.
        elif mode == 'uncased':
            articles.append(json.loads(line.lower()))
        else:
            raise ValueError("Please choose a valid reading mode('cased' / 'uncased')")
    return articles
