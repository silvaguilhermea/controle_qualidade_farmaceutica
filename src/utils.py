"""
utils.py — Funções auxiliares para o projeto de QC Farmacêutico
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def resumo_dataset(df: pd.DataFrame) -> None:
    """Imprime um resumo rápido do DataFrame."""
    print(f"Shape: {df.shape}")
    print(f"Período: {df['data_producao'].min().date()} → {df['data_producao'].max().date()}")
    print(f"\nStatus dos lotes:")
    print(df['status_lote'].value_counts().to_string())
    print(f"\nValores ausentes:\n{df.isnull().sum()[df.isnull().sum() > 0].to_string() or 'Nenhum'}")


def plot_boxplot_por_status(df: pd.DataFrame, variavel: str, ax=None) -> None:
    """Boxplot de uma variável segmentada por status do lote."""
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=df, x='status_lote', y=variavel,
                palette={'APROVADO': '#2ecc71', 'REPROVADO': '#e74c3c'}, ax=ax)
    ax.set_title(f'{variavel.replace("_", " ").title()} por Status', fontweight='bold')
    ax.set_xlabel('')


def taxa_reprovacao_por_grupo(df: pd.DataFrame, coluna: str) -> pd.DataFrame:
    """Calcula taxa de reprovação agrupada por uma coluna categórica."""
    return (
        df.groupby(coluna)
        .agg(total=('lote', 'count'), reprovados=('status_lote', lambda x: (x == 'REPROVADO').sum()))
        .assign(taxa_reprovacao=lambda x: (x['reprovados'] / x['total'] * 100).round(1))
    )
