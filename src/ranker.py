from typing import List, Dict
from .rice import rice_score
from .ice import ice_score


def combined_score(feature: Dict, rice_weight: float = 0.6, ice_weight: float = 0.4) -> float:
    r = rice_score(feature)
    i = ice_score(feature)
    r_norm = min(r / 1000.0, 1.0)
    i_norm = min(i / 10.0, 1.0)
    return round(r_norm * rice_weight + i_norm * ice_weight, 4)


def rank_features(features: List[Dict]) -> List[Dict]:
    result = []
    for feat in features:
        result.append({
            **feat,
            'rice_score':     rice_score(feat),
            'ice_score':      ice_score(feat),
            'combined_score': combined_score(feat),
        })
    return sorted(result, key=lambda x: x['combined_score'], reverse=True)


def top_features(features: List[Dict], n: int = 5) -> List[Dict]:
    return rank_features(features)[:n]


def backlog_candidates(features: List[Dict], threshold: float = 0.2) -> List[Dict]:
    ranked = rank_features(features)
    return [f for f in ranked if f['combined_score'] < threshold]
