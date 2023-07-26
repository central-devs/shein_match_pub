#!/usr/bin/env python
# coding: utf-8
from IPython.core.display_functions import display
from data.cods.google import get_dfs, upload_dataframe_to_gcs, load_data_from_gcs
import pandas as pd
from data.cods.df_tra.checker import *
from data.cods.master import process
from fuzzywuzzy import fuzz
from tqdm import tqdm
import pandas as pd
from data.cods.score import *
from data.cods.bucket import *

# ### fuzzy

# tem um limbo na analise das medidas:
#
# de 0 até 0.5 temos menor prioridade
#
# limbo de >0.5 a <0.9
#
# de >0.9 até 1 maior prioridade
#

NUM_PROC = 4


def main(lista_dfs):
    df_final, dic_erro = process(lista_dfs).response_cod()

    listaa = []
    lista = []
    linha = {}
    df_eita = pd.DataFrame(columns=['Link', 'Item Title', 'Shopname', 'L2 Category', 'ADO', 'ADGMV',
                                    'Promo Price', 'Cluster', 'L1 Category', 'Shopee ID', 'Is MS',
                                    'Meli id', 'nome ajustado', 'type_class', 'metric', 'value', 'bucket'])
    for key in dic_erro:
        lin = lista_dfs[0].loc[lista_dfs[0]['Meli id'] == key]
        df_eita = pd.concat([df_eita, lin])

    df_eita.to_csv("error.csv", index=False)

    display(df_return)
    upload_dataframe_to_gcs('uat-shein-scraper', df_final, 'df_final_shein_map.csv', prefix=None,
                            project_id='shopee-brazil-seller')

    upload_dataframe_to_gcs('uat-shein-scraper', df_return, 'df_retorno_shein_map.csv', prefix=None,
                            project_id='shopee-brazil-seller')

    # df_return.to_csv("teste_retorno_parte3.csv", index=False, encoding="utf-8-sig")


if __name__ == "__main__":

    import multiprocessing

    jobs = []

    lista_dfs = get_dfs(
        df=pd.read_csv('gs://uat-shein-scraper/top_1k_l2.csv', encoding="utf-8-sig").rename(
            {'item_price': 'Promo Price'}, axis=1),
        dfmeli=pd.read_csv('gs://uat-shein-scraper/sheinitems_2.csv', encoding="utf-8-sig"))
    # ### Classe para tratar df

    for df in lista_dfs:
        # tratando dfs dentro da lista
        df = df_checker(df).response()
        # gerando bucket
        df['bucket'] = df["Promo Price"].astype(float).apply(lambda x: buckt(x))

    for i in range(NUM_PROC):
        process = multiprocessing.Process(
            target=main,
            args=lista_dfs
        )
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

main(lista_dfs)
