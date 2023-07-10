"""Merge all the 8 step_parses_[1:8].p files into a single file."""

import dill as pickle


# Load the dependency trees of all step headlines.
step_file_path = './output/'
step_parses_1 = pickle.load(open(step_file_path + 'sid2stepdeptree_1.p', 'rb'))
step_parses_2 = pickle.load(open(step_file_path + 'sid2stepdeptree_2.p', 'rb'))
step_parses_3 = pickle.load(open(step_file_path + 'sid2stepdeptree_3.p', 'rb'))
step_parses_4 = pickle.load(open(step_file_path + 'sid2stepdeptree_4.p', 'rb'))
step_parses_5 = pickle.load(open(step_file_path + 'sid2stepdeptree_5.p', 'rb'))
step_parses_6 = pickle.load(open(step_file_path + 'sid2stepdeptree_6.p', 'rb'))
step_parses_7 = pickle.load(open(step_file_path + 'sid2stepdeptree_7.p', 'rb'))
step_parses_8 = pickle.load(open(step_file_path + 'sid2stepdeptree_8.p', 'rb'))

# Merge all step_parses_* to a single dictionary step_parses.
step_parses = dict()
step_parses.update(step_parses_1)
step_parses.update(step_parses_2)
step_parses.update(step_parses_3)
step_parses.update(step_parses_4)
step_parses.update(step_parses_5)
step_parses.update(step_parses_6)
step_parses.update(step_parses_7)
step_parses.update(step_parses_8)

# Write the merged dependendy trees step_parses into step_parses_all.p file.
with open('./output/step_parses_all.p', 'wb') as file:
    pickle.dump(step_parses, file)