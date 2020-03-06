Forked for DL Seminar

# Few-Shot NLG
Code and data for paper Few-Shot NLG with Pre-Trained Language Model
https://arxiv.org/abs/1904.09521


## Installation
pip install -r requirements.txt

## Instructions
Data and pre-trained GPT-2 can be downloaded via dropbox: https://www.dropbox.com/sh/u3t8yhcctqczpo0/AAAZV7S-qoIyaQW99r_88nUra?dl=0
```
-- sample_data: a sample train and test data for humans domain
-- data: full datasets for songs and books domain
-- models: pre-trained GPT-2 
```
To run our code, go to the code folder and run with: 

python ./Main.py --root_path ~/Data/NLP/few_shot_nlg/ --domain humans --gpt_model_name ../models/117M/ --output_path ~/Output/

Where the root path is the data folder. Specify an output path to store the results. The data preprocessing code can be found in preprocess.py. 

If you find our work helpful, please cite the arxiv version. 

# Modifications for DL Seminar (Author: Anne)

## Data preparation
In order to use the model with the E2E dataset, it has to be pre-processed with 
```
preprocess_e2e.py
```
This has to be done separately for trainset.csv, devset.csv (the output has to be named valid.box/.summary) and testset_w_refs.csv as supplied here 
http://www.macs.hw.ac.uk/InteractionLab/E2E/#data

Example usage:
```
preprocess_e2e.py input/testset_w_refs.csv input/restaurants/original_data/test.box input/restaurants/original_data/test.summary -s -d

where -s enables shuffling and -d enables the removal of duplicates
```
The pre-processed input is supplied in this repository.

## Preprocessing
To run the Main script, the input data has to be further processed by the supplied 
```
preprocess.py
```
A few adaptation were made to this script to enable correct processing with the new data.

Example usage:

```
preprocess.py input/ restaurants
```

## Training
A small adaptaion to
```
DataLoader.py
```
was necessary to create a context embedding for the new domain (i.e restaurants)

Example calls for training the models can be found in 

```
train_models.sh
```

## Testing

Example calls for testing models can be found in 

```
test_models.sh
```
where symbolic links have been created to the corresponding checkpoint folders of the trained models for better tracability, as renaming the date folders led to errors when loading the models.

## Evaluation
```
prep_test.py
``` 
was created to extract the required format for evaluating the model from the test.box and test.summary files containing duplicates (i.e without the -d option above)
The evaluation was performed using https://github.com/tuetschek/e2e-metrics 

Example usage:
```
./measure_scores.py input/restaurants/original_data/test.summary.eval <PATH_TO/test_summary.clean.txt>
```
Symlinks have been created for the corresponding test directories
(Both versions are tokenized, so no post-processing is necessary)


## Other
```stats.py```
Script for calculating the distribution of field order in MRs 
Example usage: 
```
stats.py input/restaurants/processed_data/train/train.box.lab
``` 
