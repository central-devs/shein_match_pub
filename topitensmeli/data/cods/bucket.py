import pandas as pd
from fuzzywuzzy import fuzz
from data.cods.score import check_score

df_return = pd.DataFrame(
    columns=['Link meli', 'Meli id', 'Item Title meli', 'Shopname meli', 'Promo Price meli', 'Item Title shopee',
             'Shopname_shopee', 'Promo Price shopee', 'Shop ID', 'Item ID', 'link', 'score_string',
             'Score_unidade_medida'])


def buckt_process(df_bucket, name_meli, unidade_meli, loja_name_meli, incremento_nome_loja, metricas_meli, valores_meli,
                  metrica_unidade, _df_):
    for i, _bucket_ in df_bucket.iterrows():
        name_shopee = _bucket_['nome ajustado']
        loja_name_shopee = _bucket_['Shopname']
        unidade_shopee = _bucket_['type_class']
        metricas_shopee = _bucket_['metric']
        valores_shopee = _bucket_['value']

        score_string = fuzz.token_sort_ratio(name_meli, name_shopee)
        score_metrica = None

        if unidade_meli is not None and unidade_shopee is not None:
            if len(unidade_meli) == len(unidade_shopee):
                score_string, score_metrica = check_score(loja_name_shopee, loja_name_meli, incremento_nome_loja,
                                                          unidade_meli, metricas_meli, valores_meli, unidade_shopee,
                                                          valores_shopee, metrica_unidade, score_string, name_shopee,
                                                          name_meli)

        if score_string >= 80 and (score_metrica is None or score_metrica >= 0.5):
            df_return.loc[len(df_return.index)] = [_df_['Link'], _df_['Meli id'], name_meli, loja_name_meli,
                                                   _df_['Promo Price'], name_shopee, loja_name_shopee,
                                                   _bucket_['Promo Price'], _bucket_['Shop ID'], _bucket_['Item ID'],
                                                   _bucket_['link'], score_string, score_metrica]

    return len(df_return.index), df_return
