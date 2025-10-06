from typing import Dict, List


def ice_score(feature: Dict) -> float:
    impact     = float(feature.get('impact', 0))
    confidence = float(feature.get('confidence', 0))
    ease       = float(feature.get('ease', 0))
    return round((impact + confidence + ease) / 3.0, 2)


def annotate_ice(features: List[Dict]) -> List[Dict]:
    return [
        {**f, 'ice_score': ice_score(f)}
        for f in features
    ]


def rank_by_ice(features: List[Dict]) -> List[Dict]:
    annotated = annotate_ice(features)
    return sorted(annotated, key=lambda x: x['ice_score'], reverse=True)


def ice_vs_rice_delta(feature: Dict, rice: float, ice: float) -> str:
    if abs(rice - ice) < 1:
        return 'aligned'
    return 'rice_higher' if rice > ice else 'ice_higher'
