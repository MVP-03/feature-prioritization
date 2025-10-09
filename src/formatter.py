from typing import List, Dict


def format_feature_row(feature: Dict) -> str:
    name  = feature.get('name', 'Untitled')[:30]
    rice  = feature.get('rice_score', 0)
    ice   = feature.get('ice_score', 0)
    combo = feature.get('combined_score', 0)
    return f"{name:<32} RICE:{rice:>8.1f}  ICE:{ice:>5.1f}  Combined:{combo:>6.4f}"


def format_ranking(features: List[Dict]) -> str:
    lines = [
        f"{'#':<3} {'Feature':<32} {'RICE':>8}  {'ICE':>5}  {'Score':>8}",
        '-' * 62,
    ]
    for i, feat in enumerate(features, 1):
        lines.append(f"{i:<3} {format_feature_row(feat)}")
    return '\n'.join(lines)


def format_top_n(features: List[Dict], n: int = 5) -> str:
    lines = [f'Top {n} Features to Ship Next', '=' * 40]
    for i, feat in enumerate(features[:n], 1):
        lines.append(f"{i}. {feat.get('name', 'Untitled')} (RICE: {feat.get('rice_score', 0):.1f})")
    return '\n'.join(lines)
