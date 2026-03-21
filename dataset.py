"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    # slang / colloquial positives
    "sick",
    "fire",
    "wicked",
    "lit",
    "dope",
    "proud",
    "obsessed",
    "hyped",
    "stoked",
    "blessed",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    # colloquial negatives
    "rough",
    "exhausted",
    "miserable",
    "annoyed",
    "frustrated",
    "jealous",
    "drained",
    "overwhelmed",
    "gutted",
    "ugh",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    # --- added posts ---
    "lowkey obsessed with this song rn 🎵",                          # slang + emoji, clear positive
    "I absolutely love sitting in traffic for 2 hours 🙃",           # sarcasm → actually negative
    "ngl I'm stressed af but at least it's Friday 😅",               # mixed: negative + positive
    "💀💀💀 bro really said that out loud",                          # emoji-heavy, amused/neutral reaction
    "been a rough week not gonna lie",                               # understated negative, no strong keywords
    "vibes are immaculate today no cap 🔥",                          # slang, clearly positive
    "I dunno, kinda meh about the whole thing",                      # ambiguous/neutral
    "so proud of my friend but also lowkey jealous 😬",              # mixed emotions
    "this homework is literally destroying me but I got it done 💪",  # mixed: negative process, positive outcome
    "ok not bad I guess",                                            # subtle positive with hedging
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    # --- added labels ---
    "positive",  # lowkey obsessed with this song rn 🎵
    "negative",  # sarcastic love of traffic
    "mixed",     # stressed but it's Friday
    "neutral",   # 💀💀💀 amused reaction, no clear valence
    "negative",  # been a rough week
    "positive",  # vibes are immaculate today no cap 🔥
    "neutral",   # kinda meh about the whole thing
    "mixed",     # proud but lowkey jealous
    "mixed",     # homework destroying me but got it done
    "positive",  # ok not bad I guess
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
