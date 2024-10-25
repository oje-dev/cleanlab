from typing import Callable

"""
This module provides singleton instances of SpellChecker and acceptability_checker.
"""

from spellchecker import SpellChecker
from transformers import pipeline

# Singleton instances
_spell: SpellChecker | None = None
_acceptability_checker: Callable | None = None


def get_spell_checker() -> SpellChecker:
    """
    Returns a singleton instance of SpellChecker.

    If the instance does not exist, it initializes it first.

    Returns:
        SpellChecker: The singleton instance of SpellChecker.
    """
    global _spell
    if _spell is None:
        _spell = SpellChecker()
    return _spell


def get_acceptability_checker() -> pipeline:
    """
    Returns a singleton instance of the acceptability checker pipeline.

    If the instance does not exist, it initializes it first.

    Returns:
        Pipeline: The singleton instance of the acceptability checker pipeline.
    """
    global _acceptability_checker
    if _acceptability_checker is None:
        _acceptability_checker = pipeline(
            "text-classification",
            model="textattack/bert-base-uncased-CoLA",
        )
    return _acceptability_checker
