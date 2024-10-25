import string

from . import get_spell_checker
from . import get_acceptability_checker


"""
Methods for evaluating the lexical quality of texts to refine label confidence scores.
"""


def spelling_accuracy(sentence: str) -> float:
    """
    Method uses a simple dictionary match to determine percentage of correctly spelled words in a sample sentence.
    Returns a percentage of correctly spelled words normalised between 0 and 1.

    * Currently the dictionary only uses English words, words in any other language will be flagged as misspelled. *
    """
    spell = get_spell_checker()
    words = [word.lower().strip(string.punctuation) for word in sentence.split(" ")] # A list of words, punctuation removed.
    misspelled = spell.unknown(words)
    correct = len(words) - len(misspelled)
    return correct / len(words)


def grammar_quality(sentence: str) -> float:
    """
    Method uses a BERT model fine-tuned on CoLA to determine an acceptability score for the sentence: https://huggingface.co/textattack/bert-base-uncased-CoLA
    CoLA: https://arxiv.org/abs/1805.12471

    Sentences that are incoherent, use poor grammar or are not readable score closer to 0.
    Correct, coherent sentences score closer to 1.
    """
    acceptability_checker = get_acceptability_checker()
    result = acceptability_checker(sentence)
    is_acceptable = result[0]["label"] == "LABEL_1"
    confidence_score = result[0]["score"]
    return confidence_score if is_acceptable else 1 - confidence_score
