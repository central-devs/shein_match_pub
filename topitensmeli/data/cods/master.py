from tqdm import tqdm
from data.cods.bucket import buckt_process
import pandas as pd
import concurrent.futures


class process():
    def __init__(self, lista_dfs) -> None:
        # puxando dfs
        df_meli = lista_dfs[0]
        self.df_shopee = lista_dfs[1]
        # gerando df a ser retornado
        self.df_return = pd.DataFrame(
            columns=['Link meli', 'Meli id', 'Item Title meli', 'Shopname meli', 'Promo Price meli',
                     'Item Title shopee', 'Shopname_shopee', 'Promo Price shopee', 'Shop ID', 'Item ID', 'link',
                     'score_string', 'Score_unidade_medida'])

        # em porcentagem decimal
        self.incremento_nome_loja = 0.3

        # metrica unidade
        self.metrica_unidade = 0.4

        # delta price
        self.delta_price = 0.2

        # dicionario de erros
        self.dic_erro = {}
        lista_func = []
        for index, _df_ in tqdm(df_meli.iterrows(), total=df_meli.shape[0]):
            self.rodar_linha(_df_)

    def rodar_linha(self, _df_):
        # metrica para sabermos se o item tem algum match
        achou = 0
        self._df_ = _df_
        # puxando info do _df_ meli
        self.meli_get_info(_df_)

        # função para gerar bucket de itens, se bucket for vazio função retorna None, else retorna backup e bucket
        response = self.bucket_create()
        if response == None:
            return None
        else:
            df_bucket = response[0]
            df_bucket_backup = response[1]

        # tentando puxar matchs com o bucket com todos os filtros
        count, df_get = buckt_process(df_bucket, self.name_meli, self.unidade_meli,
                                      self.loja_name_meli, self.incremento_nome_loja, self.metricas_meli,
                                      self.valores_meli, self.metrica_unidade, _df_)
        # se localizamos algum match iremos inserir isso no df return
        if not count == 0:
            self.df_return = pd.concat([self.df_return, df_get], ignore_index=True)
        # Caso contrário iremos tentar fazer um novo matching utilizando o bucket sem o filtro de categoria
        else:
            # print('tentando dnv')
            count, df_get = buckt_process(df_bucket_backup, self.name_meli, self.unidade_meli,
                                          self.loja_name_meli, self.incremento_nome_loja, self.metricas_meli,
                                          self.valores_meli, self.metrica_unidade, _df_)
        # se localizamos algum match iremos inserir no df return
        if not count == 0:
            self.df_return = pd.concat([self.df_return, df_get], ignore_index=True)
        # caso contrario iremos inserir o item no dic de erro e dar continuidade no looping
        else:
            # print('nn foi msm')
            self.dic_erro[_df_['Meli id']] = "no match"
            return None

    def response_cod(self):
        '''
            Função para retornar valores da classe
        '''
        return self.df_return, self.dic_erro

    def meli_get_info(self, _df_):
        '''
            Função para puxar dados do meli
        '''
        # puxando dados do item meli
        self.name_meli = _df_['nome ajustado']
        self.category_meli = _df_['L1 Category']
        self.loja_name_meli = _df_['Shopname']
        self.preco_meli = _df_['Promo Price']

        # unidade de medida meli
        self.unidade_meli = _df_['type_class']
        self.metricas_meli = _df_['metric']
        self.valores_meli = _df_['value']

    def bucket_create(self):
        '''
            Função para criar bucket 
        '''

        # gerando bucket pelo bucket de preço
        df_bucket = self.df_shopee[(self.df_shopee['Promo Price'].astype(float) >= (
                    float(self.preco_meli) - (float(self.preco_meli) * self.delta_price))) &
                                   (self.df_shopee['Promo Price'].astype(float) <= (
                                               float(self.preco_meli) * self.delta_price) + float(self.preco_meli))]

        # se ainda vazio iremos retornar erro
        if df_bucket.shape[0] == 0:
            self.dic_erro[self.name_meli] = "no bucket"
            return None

        # gerando bucket com categoria em modelo para não alterar o valor do bucket original
        df_modelo = df_bucket.loc[df_bucket['L1 Category'] == self.category_meli]

        if df_modelo.shape[0] != 0:
            return df_modelo, df_bucket
        else:
            return df_bucket, df_bucket
