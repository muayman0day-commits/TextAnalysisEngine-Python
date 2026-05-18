# Text Analysis Engine

This project is a simple text analysis engine built in Python.
It is made to handle common text tasks in a clean and easy way.

## Problem

You often have many texts like sentences or articles and you want to analyze them smartly.
The tasks include:

- Counting words
- Finding most repeated words
- Checking for similar words (anagrams)
- Extracting unique words
- Comparing two texts

## Solution

The project is split into small files so each part stays simple and clear.
This makes it easier to read and maintain.

## Project structure

- `text_analyzer/main.py`: A simple demo that shows how everything works.
- `text_analyzer/text_utils.py`: Text cleaning, splitting words, and anagram checks.
- `text_analyzer/statistics.py`: Word counting, top repeated words, and unique words.
- `text_analyzer/comparison.py`: Comparing two text blocks and showing common or unique words.
- `text_analyzer/tests.py`: Basic tests to make sure the main functions work.

## How to use

Run the demo example:

```bash
python text_analyzer/main.py
```

Run the tests:

```bash
python text_analyzer/tests.py
```

