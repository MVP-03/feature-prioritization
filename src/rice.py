from typing import Dict, List


def rice_score(feature: Dict) -> float:
    reach      = float(feature.get('reach', 0))
    impact     = float(feature.get('impact', 0))
    confidence = float(feature.get('confidence', 100)) / 100.0
    effort     = float(feature.get('effort', 1))
    if effort == 0:
        return 0.0
    return round((reach * impact * confidence) / effort, 2)


def annotate_rice(features: List[Dict]) -> List[Dict]:
    return [
        {**f, 'rice_score': rice_score(f)}
        for f in features
    ]


def rank_by_rice(features: List[Dict]) -> List[Dict]:
    annotated = annotate_rice(features)
    return sorted(annotated, key=lambda x: x['rice_score'], reverse=True)


def rice_tier(score: float) -> str:
    if score >= 1000:
        return 'must-have'
    if score >= 500:
        return 'high'
    if score >= 200:
        return 'medium'
    return 'low'
