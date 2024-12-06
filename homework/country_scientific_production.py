"""Taller Presencial Evaluable"""

import os

import folium  # type: ignore
import pandas as pd  # type: ignore


def load_affiliations():
    """Carga el archivo scopus-papers.csv y retorna un dataframe con la
    columna 'Affiliations'"""

    dataframe = pd.read_csv(
        (
            "https://raw.githubusercontent.com/jdvelasq/datalabs/"
            "master/datasets/scopus-papers.csv"
        ),
        sep=",",
        index_col=None,
    )[["Affiliations"]]
    return dataframe




def make_worldmap():
    """Función principal"""

    if not os.path.exists("files"):
        os.makedirs("files")

    affiliations = load_affiliations()

    print(affiliations.head())


if __name__ == "__main__":
    make_worldmap()








