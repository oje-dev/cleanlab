from .metrics import grammar_quality, spelling_accuracy

"""
    A class to evaluate the lexical quality of a sentence based on spelling and grammar.

    Attributes:
        sentence (str): The sentence to be evaluated.
        spelling_weight (float): The weight given to spelling accuracy in the combined score.
        quality_weight (float): The weight given to grammar quality in the combined score.

"""


class LexicalQualityEvaluator:
    def __init__(self, sentence: str, spelling_weight: float = 0.5, quality_weight: float = 0.5):
        """
        Initializes the LexicalQualityEvaluator with a sentence and weights for spelling and grammar.

        Args:
            sentence (str): The sentence to be evaluated.
            spelling_weight (float): The weight given to spelling accuracy in the combined score. Default is 0.5.
            quality_weight (float): The weight given to grammar quality in the combined score. Default is 0.5.

        Raises:
            ValueError: If the sum of spelling_weight and quality_weight is not equal to 1.
        """
        if spelling_weight + quality_weight != 1:
            raise ValueError("Weights must add up to 1")

        self.sentence: str = sentence
        self.spelling_weight: float = spelling_weight
        self.quality_weight: float = quality_weight
        
        self._spelling_score: float | None = None
        self._quality_score: float | None = None
        self._combined_score: float | None = None

    def get_spelling_score(self) -> float:
        return self._spelling_score or spelling_accuracy(self.sentence)

    def get_quality_score(self) -> float:
        return self._quality_score or grammar_quality(self.sentence)

    def get_combined_quality_score(self) -> float:
        spelling_score: float = self._spelling_score or self.get_spelling_score()
        quality_score: float = self._quality_score or self.get_quality_score()
        return (self.spelling_weight * spelling_score) + (self.quality_weight * quality_score)
