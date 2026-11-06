# NLP Lab Project

This repository contains a set of notebooks covering core topics in Natural Language Processing (NLP), including text preprocessing, n-grams, text representation, classification, deep learning, large language models, POS tagging, Named Entity Recognition (NER), machine translation, and attention-based RNN models.

## Contents

Each lab is stored in its own dedicated folder:

- [Lab1_Introduction_to_NLP](./Lab1_Introduction_to_NLP) — Introduction to NLP
- [Lab2_Text_Preprocessing_and_Regular_Expressions](./Lab2_Text_Preprocessing_and_Regular_Expressions) — Text preprocessing and regular expressions
- [Lab3_N_grams](./Lab3_N_grams) — N-grams
- [Lab4_Classification_and_Evaluation_in_NLP](./Lab4_Classification_and_Evaluation_in_NLP) — Text classification and evaluation
- [Lab5_Text_Representation](./Lab5_Text_Representation) — TF-IDF, embeddings, and similarity
- [Lab6_Deep_Learning_for_NLP](./Lab6_Deep_Learning_for_NLP) — Deep learning for NLP
- [Lab7_LLMs](./Lab7_LLMs) — Large language models
- [Lab8_POS_Tagging](./Lab8_POS_Tagging) — POS tagging
- [Lab9_Named_Entity_Recognition](./Lab9_Named_Entity_Recognition) — NER
- [Lab10_Introduction_to_Machine_Translation](./Lab10_Introduction_to_Machine_Translation) — Machine translation
- [Lab11_Attention_with_RNN](./Lab11_Attention_with_RNN) — Attention with RNN

The sample dataset is stored in [data/Amazon_Unlocked_Mobile.csv](./data/Amazon_Unlocked_Mobile.csv).

## How to run

1. Create and activate a Python environment.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Download or place the necessary CSV datasets in the project root or in the `data/` folder.
4. Run the setup helper to prepare Colab-style paths used by some notebooks:

```bash
python scripts/prepare_notebook_data.py
```

5. Open a notebook in Jupyter or VS Code and run the cells in order.

## Important note about the notebooks

Some labs were written originally for Google Colab and therefore reference files such as `/content/...`.
This is not portable by default. You may need to either:
- copy the data to the `/content` location, or
- update the notebook paths to a local path, such as `./data/filename.csv`

This project is designed to be run locally with a small amount of path adjustment.

## Project quality notes

- Use consistent file naming and dataset paths.
- Keep notebooks reproducible by storing required data locally.
- Add concluding interpretation for model results instead of only displaying outputs.
- Keep all documentation and setup steps in the repository so that another person can rerun the work.

## Dataset policy

Large external datasets should be stored outside the Git repository if they are not required to be version-controlled.
Use `data/README.md` as the record of which datasets are expected for this project.
