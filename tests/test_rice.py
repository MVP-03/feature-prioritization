import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from rice import rice_score, annotate_rice, rank_by_rice, rice_tier

FEATURES = [
    {'name': 'Auth',    'reach': 5000, 'impact': 3, 'confidence': 80, 'effort': 2},
    {'name': 'Dark Mode','reach': 2000,'impact': 1, 'confidence': 90, 'effort': 1},
    {'name': 'Webhooks','reach': 1000, 'impact': 2, 'confidence': 70, 'effort': 3},
]


def test_rice_score_basic():
    f = {'reach': 1000, 'impact': 2, 'confidence': 100, 'effort': 1}
    assert rice_score(f) == 2000.0


def test_rice_score_zero_effort():
    f = {'reach': 1000, 'impact': 2, 'confidence': 100, 'effort': 0}
    assert rice_score(f) == 0.0


def test_rank_by_rice_order():
    ranked = rank_by_rice(FEATURES)
    assert ranked[0]['name'] == 'Auth'


def test_annotate_rice():
    annotated = annotate_rice(FEATURES)
    assert all('rice_score' in f for f in annotated)


def test_rice_tier():
    assert rice_tier(1500) == 'must-have'
    assert rice_tier(300) == 'medium'
    assert rice_tier(50) == 'low'
