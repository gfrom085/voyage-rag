"""
Générateur de dataset contrôlé pour tests de granularité sémantique

Ce script génère un dataset minimal (20-30 docs) avec:
- Scores numériques explicites
- Labels hiérarchiques (TOP, MID, LOW, etc.)
- Domaines variés (tech, finance, legal, etc.)
- Variations linguistiques (FR/EN)
"""

import json
from pathlib import Path
from typing import List, Dict


def generate_ordinal_documents(num_docs: int = 30) -> List[Dict]:
    """
    Génère des documents avec gradation ordinale contrôlée

    Args:
        num_docs: Nombre de documents à générer

    Returns:
        Liste de documents avec scores/tiers
    """
    # TODO: À implémenter
    # - Créer docs avec scores de 50 à 95 (gradation fine)
    # - Assigner tiers selon score_ranges
    # - Varier les domaines (tech, finance, etc.)
    # - Varier FR/EN
    pass


def generate_test_queries() -> List[Dict]:
    """
    Génère les requêtes de test couvrant différents cas

    Returns:
        Liste de queries avec catégories
    """
    # TODO: À implémenter
    # Catégories:
    # - Superlatives: "meilleur", "top", "premium"
    # - Comparatives: "milieu de gamme", "balanced"
    # - Budget: "économique", "entry-level", "budget"
    # - Numeric: "score > 80", "entre 70 et 80"
    # - Multilingual: FR/EN variants
    pass


def generate_ground_truth(documents: List[Dict],
                         queries: List[Dict]) -> List[Dict]:
    """
    Génère le ground truth (expected rankings) pour chaque query

    Args:
        documents: Liste des documents
        queries: Liste des queries

    Returns:
        Ground truth avec ranked lists attendues
    """
    # TODO: À implémenter
    # Pour chaque query, déterminer le ranking attendu basé sur:
    # - Matching sémantique (superlatives → TOP tier)
    # - Scores numériques (ordre décroissant)
    # - Pertinence domaine
    pass


def save_datasets(output_dir: Path):
    """
    Génère et sauvegarde tous les datasets

    Args:
        output_dir: Répertoire de sortie
    """
    # TODO: À implémenter
    pass


if __name__ == "__main__":
    output_dir = Path(__file__).parent / "datasets"
    save_datasets(output_dir)
    print(f"✅ Datasets générés dans {output_dir}")
