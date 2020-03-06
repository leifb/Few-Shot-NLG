#!/bin/bash

# 500_20
python3 ./Main.py --mode test --saved_model_path ~/project/e2e/Few-Shot-NLG/output/model_500_20/ --root_path ~/project/e2e/Few-Shot-NLG/input/ --domain restaurants --gpt_model_name ../models/117M/ --output_path ~/project/e2e/Few-Shot-NLG/output/ &>test_500_20.log
# shuff_20
python3 ./Main.py --mode test --saved_model_path ~/project/e2e/Few-Shot-NLG/output/model_shuff_20/ --root_path ~/project/e2e/Few-Shot-NLG/input/ --domain restaurants --gpt_model_name ../models/117M/ --output_path ~/project/e2e/Few-Shot-NLG/output/ &>test_shuff_20.log
# dup_20
python3 ./Main.py --mode test --saved_model_path ~/project/e2e/Few-Shot-NLG/output/model_dup_20/ --root_path ~/project/e2e/Few-Shot-NLG/input/ --domain restaurants --gpt_model_name ../models/117M/ --output_path ~/project/e2e/Few-Shot-NLG/output/ &>test_dup_20.log
# dup_shuff_20
python3 ./Main.py --mode test --saved_model_path ~/project/e2e/Few-Shot-NLG/output/model_dup_shuff_20/ --root_path ~/project/e2e/Few-Shot-NLG/input/ --domain restaurants --gpt_model_name ../models/117M/ --output_path ~/project/e2e/Few-Shot-NLG/output/ &>test_dup_shuff_20.log

