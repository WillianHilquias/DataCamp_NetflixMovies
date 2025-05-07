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
    # Força uso do backend Tk
    matplotlib.use('TkAgg')

def style():
    # 2. Aplique o estilo Seaborn
    sns.set_style('darkgrid')
    # (agora 'seaborn-darkgrid' já está registrado no matplotlib)
    matplotlib.use('TkAgg')  # força o uso do backend Tk

def info():
    # 3. Visão geral
    print(df.shape)  # printa linhas e colunas no dataframe
    print(df.dtypes)  # tipo de dado em cada coluna

def load_data(path: str) -> pd.DataFrame:
    """
    Carrega o dataset a partir de um arquivo CSV.
    """
    return pd.read_csv(path)


def rel_filmes_series(df: pd.DataFrame) -> None:
    # 4. Distribuição por tipo
    counts = df['type'].value_counts()  # conta a quantidade de cada 'type'
    counts.plot.bar()  # imprime cada 'type' em uma coluna, com sua respectiva quantidade
    plt.title('Filmes vs Séries')
    plt.show()
def analyze_top_actors(df: pd.DataFrame, top_n) -> None:
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
    top_actors.plot(kind='bar', stacked=True)
    plt.title(f'Top {top_n} Atores com Mais Filmes')
    plt.xlabel('Número de Filmes')
    # plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

def movies_90s(df: pd.DataFrame) -> None:
    df_90s = df[(df['type'] == 'Movie') & (df['release_year'].between(1990, 1999))]
    bins = list(range(1990, 2002, 2))  # [1990, 1992, 1994, 1996, 1998, 2000]
    plt.figure(figsize=(12, 6), dpi=100)   # 12″ de largura × 6″ de altura, 100 dpi
    plt.hist(
        df_90s['release_year'],
        bins=bins,
        edgecolor='blue'
    )
    plt.xticks(bins)
    plt.xlabel('Ano de Lançamento (faixas de 2 anos)')
    plt.ylabel('Quantidade de Filmes')
    plt.title('Lançamentos por Intervalo de Anos')
    plt.show()



def new_movies(df: pd.DataFrame) -> None:
    # Tendência da quantidade de lançamentos ao longo do tempo

    df_trend = df['release_year'].value_counts().sort_index().plot(kind='line')
    df_trend.set_title('Movie Trend')
    df_trend.set_xlabel('Year')
    df_trend.set_ylabel('Count')
    plt.show()


def main():
    # 1. Configuração de plotagem
    configure_plotting()

    # 2. Carregar dados
    data_path = '../data/raw/netflix_data.csv'
    df = load_data(data_path)

    # 3. Visão geral do dataset
    rel_filmes_series(df)
    analyze_top_actors(df, top_n=20)
    movies_90s(df)
    new_movies(df)


if __name__ == '__main__':
    main()