#!/usr/bin/env python3
"""
Netflix Movies Data Analysis
Autor: Willian Hilquias
Data: 2025-04-30
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


def configure_plotting():
    """
    Configura parâmetros e estilo padrão para os gráficos.
    """
    # Ajustes gerais do Matplotlib
    plt.rcParams.update({
        'font.size':      12,
        'axes.titlesize': 14,
        'axes.labelsize': 12,
        'lines.linewidth':2,
        'figure.figsize': (8,5),
        'figure.dpi':     120
    })
    # Estilo do Seaborn
    sns.set_style('darkgrid')
    # Força uso do backend Tk (se necessário)
    matplotlib.use('TkAgg')


def load_data(path: str) -> pd.DataFrame:
    """
    Carrega o dataset a partir de um arquivo CSV.
    """
    return pd.read_csv(path)


def print_overview(df: pd.DataFrame) -> None:
    """
    Exibe forma e tipos de dados do DataFrame.
    """
    print(f"DataFrame shape: {df.shape}")
    print("Tipos de dados por coluna:")
    print(df.dtypes)


def analyze_top_actors(df: pd.DataFrame, top_n: int = 10) -> None:
    """
    Identifica e plota os top N atores com mais filmes.
    """
    # Filtrar apenas filmes e linhas sem cast vazio
    df_movies = df[df['type'] == 'Movie'].dropna(subset=['cast'])
    # Converter string de elenco em lista de nomes
    df_movies['cast_list'] = df_movies['cast'].str.split(', ')
    # Explodir lista em linhas separadas
    df_exploded = df_movies.explode('cast_list')
    # Contagem de aparições por ator
    actors_counts = df_exploded['cast_list'].value_counts()

    # Selecionar top N
    top_actors = actors_counts.head(top_n)

    # Plotagem
    plt.figure()
    top_actors.plot(kind='barh', stacked=True)
    plt.title(f'Top {top_n} Atores com Mais Filmes')
    plt.xlabel('Número de Filmes')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()


def main():
    # 1. Configuração de plotagem
    configure_plotting()

    # 2. Carregar dados
    data_path = '../data/raw/netflix_data.csv'
    df = load_data(data_path)

    # 3. Visão geral do dataset
    print_overview(df)

    # 4. Análise de top atores
    analyze_top_actors(df, top_n=10)


if __name__ == '__main__':
    main()