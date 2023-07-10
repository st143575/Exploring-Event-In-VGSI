# Combining Tradition with Modernness: Exploring Event Representations in Vision-and-Language Models for Visual Goal–Step Inference

This is the code for our paper:  
Combining Tradition with Modernness: Exploring Event Representations in Vision-and-Language Models for Visual Goal–Step Inference  
[[paper](https://aclanthology.org/2023.acl-srw.36/)].

## Dataset
We use the data provided by [Yang et al., 2021](https://arxiv.org/abs/2104.05845). The dataset is available [here](https://drive.google.com/drive/folders/1hjjcNSUSqv8AbA7R-5lIKmui-ySCEWJw?usp=sharing). We preprocessed the data as described in our paper.

## Usage

### Requirements
TBD

### Data Preprocessing
Step 1: Download the dataset. Put WikihowText_data.json under ./data/data_preprocessing.

Step 2: Run the code in ./data_preprocessing/data_preprocessing.ipynb.

PS: The output of data_preprocessing.ipynb can be found in Google Drive (TBD).

Step 3: 
- Run
	```
	python sid2step.p -i output/articles_df.p -o output/
 	```

### Dependency Parsing
Step 1: Go to the directory ./event_representations/dependency_parsing/.

Step 2:

- Put the files articles_df.p and sid2step.p (see the directory data_preprocessing/output/) in the directory ./input/.

- To parse the goal sentences, 

	- Go to the directory ./goal_parsing/.
	
	- Run  
		```
		python goal_parsing_supar.py -i ../input/articles_df.p -o output/
	 	```

- To parse the step headline sentences,

	- Go to the directory ./step_parsing/.
	
	- For convenience, the 772k step headlines were separately parsed.
	  Run  
	  	```
		python step_parsing_supar_1.py -i ../input/sid2step.p -o output/  
		python step_parsing_supar_2.py -i ../input/sid2step.p -o output/  
		...  
		python step_parsing_supar_8.py -i ../input/sid2step.p -o output/  
	   	```
	
	- Merge the 8 results:
	  Run ```python step_parsing_merge.py```
	
	PS: The output of step_parsing_merge.py can be found in Google Drive (TBD).

-- IN PROCESSING, MORE COMING SOON. --
