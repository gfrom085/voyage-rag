"""
Métriques d'évaluation pour tests de granularité sémantique

Ce module implémente les métriques suivantes:
- nDCG@k (Normalized Discounted Cumulative Gain)
- MRR (Mean Reciprocal Rank)
- Kendall's Tau (corrélation de rang)
- Marges de similarité cosinus
"""

import numpy as np
from typing import List, Dict, Tuple
from scipy.stats import kendalltau


def ndcg_at_k(predicted_ranking: List[str],
              ground_truth: Dict[str, int],
              k: int = 5) -> float:
    """
    Calcule le nDCG@k (Normalized Discounted Cumulative Gain)

    Args:
        predicted_ranking: Liste ordonnée des doc_ids prédits
        ground_truth: Dict mapping doc_id -> relevance_score (0-3)
        k: Position jusqu'où évaluer

    Returns:
        Score nDCG@k entre 0 et 1
    """
    # TODO: À implémenter
    pass


def mean_reciprocal_rank(predicted_ranking: List[str],
                         relevant_docs: List[str]) -> float:
    """
    Calcule le MRR (Mean Reciprocal Rank)

    Args:
        predicted_ranking: Liste ordonnée des doc_ids prédits
        relevant_docs: Liste des doc_ids pertinents

    Returns:
        Score MRR (1/rank du premier doc pertinent)
    """
    # TODO: À implémenter
    pass


def kendall_tau_correlation(predicted_ranking: List[str],
                            expected_ranking: List[str]) -> Tuple[float, float]:
    """
    Calcule la corrélation de Kendall's Tau entre deux rankings

    Args:
        predicted_ranking: Liste ordonnée des doc_ids prédits
        expected_ranking: Liste ordonnée des doc_ids attendus

    Returns:
        (tau, p_value): Coefficient de corrélation et p-value
    """
    # TODO: À implémenter
    pass


def cosine_margin(similarities: List[float]) -> Dict[str, float]:
    """
    Calcule les marges entre rangs consécutifs

    Args:
        similarities: Liste des similarités cosinus triées (descendant)

    Returns:
        Dict avec statistiques des marges
    """
    # TODO: À implémenter
    pass


def tier_accuracy(predicted_docs: List[Dict],
                 expected_tier: str) -> float:
    """
    Calcule le % de docs du bon tier dans le top-k

    Args:
        predicted_docs: Liste de docs avec leur 'tier'
        expected_tier: Tier attendu (TOP, MID, LOW)

    Returns:
        Accuracy entre 0 et 1
    """
    # TODO: À implémenter
    pass
