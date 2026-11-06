from __future__ import annotations

import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / 'data'
TARGET_ROOT = Path('/content') if os.name != 'nt' else Path('C:/content')

REQUIRED_FILES = [
    'Amazon_Unlocked_Mobile.csv',
    'DisneylandReviews.csv',
    'True.csv',
    'Fake.csv',
    'simpsons_script_lines.csv',
    'eng_-french.csv',
    'Lab_11_QnA_Dataset.csv',
    'apple_twitter_sentiment_texts.csv',
    'tweets.csv',
    'Dataset.csv',
]


def find_file(name: str) -> Path | None:
    candidates = [
        ROOT / name,
        DATA_DIR / name,
        ROOT / 'data' / name,
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def make_link(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() or target.is_symlink():
        return
    try:
        target.symlink_to(source)
    except OSError:
        shutil.copy2(source, target)


def main() -> None:
    print(f'Project root: {ROOT}')
    print(f'Data folder: {DATA_DIR}')
    print(f'Colab-style target: {TARGET_ROOT}')

    found = []
    missing = []

    for name in REQUIRED_FILES:
        file_path = find_file(name)
        if file_path is not None:
            found.append((name, file_path))
            make_link(file_path, TARGET_ROOT / name)
        else:
            missing.append(name)

    if found:
        print('\nFiles prepared:')
        for name, file_path in found:
            print(f'  - {name} -> {file_path}')

    if missing:
        print('\nMissing data files:')
        for name in missing:
            print(f'  - {name}')
        print('\nDownload them and place them in the project root or in the data/ folder, then rerun this script.')
    else:
        print('\nAll expected datasets were found and linked/copied.')


if __name__ == '__main__':
    main()
