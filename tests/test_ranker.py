import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ranker import combined_score, rank_features, top_features, backlog_candidates
from ice import ice_score

FEATURES = [
    {'name': 'SSO',       'reach': 5000, 'impact': 3, 'confidence': 80, 'effort': 2},
    {'name': 'Dark Mode', 'reach': 800,  'impact': 1, 'confidence': 90, 'effort': 1, 'ease': 8},
    {'name': 'Bulk Export','reach': 200, 'impact': 1, 'confidence': 50, 'effort': 3, 'ease': 3},
]


def test_rank_features_returns_all():
    ranked = rank_features(FEATURES)
    assert len(ranked) == 3
    assert all('combined_score' in f for f in ranked)


def test_top_features_count():
    top = top_features(FEATURES, n=2)
    assert len(top) == 2


def test_backlog_candidates():
    candidates = backlog_candidates(FEATURES, threshold=0.1)
    assert isinstance(candidates, list)


def test_ice_score_basic():
    f = {'impact': 8, 'confidence': 6, 'ease': 7}
    assert ice_score(f) == pytest.approx(7.0, abs=0.1)


try:
    import pytest
except ImportError:
    pass
