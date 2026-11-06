# Dataset setup

This folder is intended for datasets used by the NLP lab notebooks.

The notebooks in this project were originally written for Google Colab and may reference files under `/content/...`.
For local or VS Code use, place the required CSV files in this folder and then run the setup script:

```bash
python scripts/prepare_notebook_data.py
```

Required datasets may include:
- Amazon_Unlocked_Mobile.csv
- DisneylandReviews.csv
- True.csv
- Fake.csv
- simpsons_script_lines.csv
- eng_-french.csv
- Lab_11_QnA_Dataset.csv
- apple_twitter_sentiment_texts.csv
- tweets.csv
- Dataset.csv

If a dataset is not available locally, download it first from the original source and save it here.
Do not leave notebook code pointing to a Colab-only path when a local path is available.
