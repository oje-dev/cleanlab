import pytest
import json
from cleanlab.lexical_quality.lexical_quality import LexicalQualityEvaluator

with open('tests/lexical_quality/test_cases.json', 'r') as file:
    test_cases = json.load(file)

@pytest.mark.parametrize("case", test_cases)
def test_get_spelling_score(case):
    evaluator = LexicalQualityEvaluator(case["sentence"])
    assert evaluator.get_spelling_score() == pytest.approx(case["expected_spelling_score"], 0.1)


@pytest.mark.parametrize("case", test_cases)
def test_get_quality_score(case):
    evaluator = LexicalQualityEvaluator(case["sentence"])
    assert evaluator.get_quality_score() == pytest.approx(case["expected_quality_score"], 0.1)


@pytest.mark.parametrize("case", test_cases)
def test_get_combined_quality_score(case):
    evaluator = LexicalQualityEvaluator(case["sentence"])
    assert evaluator.get_combined_quality_score() == pytest.approx(
        case["expected_combined_score"], 0.1
    )
