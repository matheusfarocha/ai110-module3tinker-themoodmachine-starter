# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

You may complete this model card for whichever version you used, or compare both if you explored them.

## 1. Model Overview

**Model type:**  
I used only the rule model.

**Intended purpose:**  
The model is trying to classify social media posts as 'neutral', 'positive', 'negative'

**How it works (brief):**
Each word gets checked against a positive and negative word list. Positive words add 1 to the score, negative words subtract 1. Negators like "not" flip the sign. Final score maps to a label.



## 2. Data

**Dataset description:**  
16, I asked AI to do so diversly. 

**Labeling process:**  
AI classification + manual overview 

**Important characteristics of your dataset:**  
Examples you might include:  

- Contains slang ("lowkey," "no cap," "fire," "sick") and emojis (🔥, 😅, 💀)
- Includes one sarcastic post ("I absolutely love sitting in traffic for 2 hours 🙃")
- Several posts express mixed feelings
- Some posts are short and tonally ambiguous

**Possible issues with the dataset:**
Only 16 posts total, all written by one person, so it doesn't reflect how diverse real language is. There's also only one sarcasm example, and the mixed/neutral labels can be hard to agree on.

## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**
- Positive word → +1, negative word → -1
- Negators ("not", "never", "don't", etc.) flip the sign of the next sentiment word
- score > 0 → positive, score < 0 → negative, score == 0 → neutral

**Strengths of this approach:**
Works well on straightforward posts with clear sentiment words. Easy to debug since you can see exactly which words triggered the score.

**Weaknesses of this approach:**
Completely misses sarcasm, slang not in the word list, and can't distinguish neutral from mixed emotions (both score 0).

## 4. How the ML Model Works (if used)

Not used.

## 5. Evaluation

**How you evaluated the model:**
Ran predictions on all 16 posts and compared to TRUE_LABELS. Got 10/16 correct (62%).

**Examples of correct predictions:**
- "I love this class so much" → positive. "love" matched.
- "I am not happy about this" → negative. Negation flipped "happy" to -1.
- "This is fine" → neutral. No matches, score stayed 0.

**Examples of incorrect predictions:**
- "I absolutely love sitting in traffic 🙃" → positive, should be negative. Sarcasm, model just saw "love."
- "Feeling tired but kind of hopeful" → negative, should be mixed. "hopeful" isn't in the word list.
- "vibes are immaculate today no cap 🔥" → neutral, should be positive. Pure slang, no matches.

## 6. Limitations

- Only 16 posts, all from one person
- Can't detect sarcasm
- Can't distinguish neutral from mixed emotions
- Heavily dependent on the word lists — anything not in the list is ignored

## 7. Ethical Considerations

- Could miss distress signals if phrased in slang or sarcasm
- Works worse for language communities not represented in the word lists
- Analyzing personal messages without consent is a privacy issue

## 8. Ideas for Improvement

- Add more labeled posts from real social media
- Make emojis affect the score
- Add a "mixed" output path when both positive and negative words appear
- Use a pretrained model that understands context and sarcasm
