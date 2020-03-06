#!/bin/bash

# 500_20
python3 ./Main.py --mode train --root_path ~/project/e2e/Few-Shot-NLG/input/ --domain restaurants --gpt_model_name ../models/117M/ --output_path ~/project/e2e/Few-Shot-NLG/output/ &>train_500_20.log
# shuff_20
python3 ./Main.py --mode train --root_path ~/project/e2e/Few-Shot-NLG/input_shuff/ --domain restaurants --gpt_model_name ../models/117M/ --output_path ~/project/e2e/Few-Shot-NLG/output/ &>train_shuff_20.log
# dup_20
python3 ./Main.py --mode train --root_path ~/project/e2e/Few-Shot-NLG/input_dup/ --domain restaurants --gpt_model_name ../models/117M/ --output_path ~/project/e2e/Few-Shot-NLG/output/ &>train_dup_20.log
# dup_shuff_20
python3 ./Main.py --mode train --root_path ~/project/e2e/Few-Shot-NLG/input_shuff_dup/ --domain restaurants --gpt_model_name ../models/117M/ --output_path ~/project/e2e/Few-Shot-NLG/output/ &>train_shuff_dup_20.log
