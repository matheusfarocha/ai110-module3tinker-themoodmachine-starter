# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an educational lab project for building and comparing two sentiment analysis approaches on social media posts:
1. A **rule-based classifier** (`mood_analyzer.py` / `main.py`)
2. A **machine learning classifier** (`ml_experiments.py`)

## Setup

```bash
pip install -r requirements.txt
```

## Running the Code

```bash
# Run rule-based model (evaluation + interactive demo)
python main.py

# Run ML model (train, evaluate, interactive demo)
python ml_experiments.py
```

There is no formal test suite — evaluation is done through batch comparison against `TRUE_LABELS` in `dataset.py`.

## Architecture

**Shared data layer (`dataset.py`):** Defines `POSITIVE_WORDS`, `NEGATIVE_WORDS`, `SAMPLE_POSTS`, and `TRUE_LABELS`. Both models draw from this shared dataset.

**Rule-based pipeline (`mood_analyzer.py` → `main.py`):**
- `MoodAnalyzer.preprocess()` tokenizes and normalizes text
- `MoodAnalyzer.score_text()` counts positive/negative word matches and returns a numeric score
- `MoodAnalyzer.predict_label()` maps the score to `"positive"` / `"negative"` / `"neutral"` / `"mixed"`
- `main.py` runs evaluation against `TRUE_LABELS` and an interactive demo

**ML pipeline (`ml_experiments.py`):**
- Uses `CountVectorizer` (bag-of-words) + `LogisticRegression` from scikit-learn
- Trains and evaluates on the same `SAMPLE_POSTS` / `TRUE_LABELS` from `dataset.py`
- Includes an interactive demo matching the rule-based interface

**Lab intent:** Students expand the word lists and dataset, implement missing classifier logic, train the ML model, and document findings in `model_card.md`.
