import nltk
from nltk import pos_tag
from tqdm import tqdm
import pandas as pd


class Uni_Medida():
    # classe recebe df, coluna a ser trabalhada se add == False, classe retorna dic com metricas encontradas
    def __init__(self, df, columns_title='nome ajustado', add=True):
        # gerando df final a ser retornado
        df_final = pd.DataFrame(columns=['type_class', 'metric', 'value'])
        # salvando elemento add em objeto self
        self.add = add
        # salvando nome da coluna em objeto self
        self.columns_title = columns_title
        # salvando df em objeto self
        self.df = df

        ### dic medidas
        self.dic_med = {"Names": {
            "ram": "Memoria", "mega": "Memoria", "bts": "Memoria",
            "gb": "Espaco", "tb": "Espaco", "kb": "Espaco", "bt": "Espaco", "mb": "Espaco",
            "l": "Vol", "litro": "Vol", "ml": "Vol", "Ltrs": "Vol",
            "tonelada": "Peso", "kg": "Peso", "grama": "Peso", "gr": "Peso", "kilo": "Peso", "quilo": "Peso",
            "lb": "Peso", "mg": "Peso", "g": "Peso", "t": "Peso", "libros": "Peso",
            "w": "Eletrico", "v": "Eletrico", "kw": "Eletrico", "wts": "Eletrico", "watts": "Eletrico",
            "volts": "Eletrico", "kwh": "Eletrico",
            "un": "Quant", "unidade": "Quant", "uni": "Quant", "kit": "Quant", "volume": "Quant", "vol": "Quant",
            "unid": "Quant", "pcts": "Quant",
            "km": "Medida", "mm": "Medida", "m": "Medida", "polegadas": "Medida", "cm": "Medida", "metros": "Medida",
            "centimetro": "Medida", "ft": "Medida", "m2": "Medida", "largura": "Medida", "altura": "Medida"
        }, "data": {
            "Memoria": {"ram": 0.3, "mega": 0.3, "bts": 0.3},
            "Espaco": {"gb": 0.5, "tb": 0.5, "kb": 0.5, "bt": 0.5, "mb": 0.5},
            "Vol": {"l": 1, "litro": 1, "ml": 1, "Ltrs": 1},
            "Peso": {"tonelada": 0.9, "kg": 0.9, "grama": 0.9, "gr": 0.9, "kilo": 0.9, "quilo": 0.9, "lb": 0.9,
                     "mg": 0.9, "g": 0.9, "t": 0.9, "libros": 0.9},
            "Eletrico": {"w": 0.2, "v": 0.2, "kw": 0.2, "wts": 0.2, "watts": 0.2, "volts": 0.2, "kwh": 0.2},
            "Quant": {"un": 0.9, "unidade": 0.9, "uni": 0.9, "kit": 0.9, "volume": 0.9, "vol": 0.9, "unid": 0.9,
                      "pcts": 0.5},
            "Medida": {"km": 0.5, "mm": 0.5, "m": 0.5, "polegadas": 0.5, "cm": 0.5, "metros": 0.5, "centimetro": 0.5,
                       "ft": 0.5, "m2": 0.5, "largura": 0.7, "altura": 0.7}
        }
        }

        # criar lista vazia para armazenar os resultados
        results = []

        # iterar sobre as linhas do dataframe
        for index, row in tqdm(df.iterrows(), total=df.shape[0]):
            # salvando linha df em objeto self para indicar valor para a função find_med
            self._df_ = row
            # função para puxar unidade de medida presente no texto
            self.find_med()
            # checando se args da função find_med é None, isso para caso de não encontrar medidas. Nesse caso inserimos None no resultado
            if self.args == None:
                results.append({'type_class': None, 'metric': None, 'value': None})
                continue
            # lista para salvar medidas
            # iremos tentar localizar as medidas localizadas no df na lista de medidas da classe
            # lista utilizada na função self.getmed
            self.lista = []
            # gerando vetor char salvo em tupla
            self.char_vector_generator()
            # função recursiva que loc as medidas na nossa lista de medidas
            self.get_med(0)
            # se a lista estiver fazia não localizamos a medida na nossa lista de classe, então inserimos None no resultado
            if len(self.lista) == 0:
                results.append({'type_class': None, 'metric': None, 'value': None})
                continue
            # dicionario com a metrica das medidas localizadas na lista de medidas da classe
            dics_final = self.get_score_metric()
            # adicionar dicionario ao resultado
            results.append(dics_final)

        # concatenar todos os dicionários em um único DataFrame
        df_final = pd.DataFrame(results)

        # salvando df final em objeto self
        self.df_final = df_final

        # inserindo coluna nova no df
        if self.add == True:
            self.add_columns()

    def add_columns(self):
        # inserindo colunas
        for col in self.df_final.columns:
            self.df[col] = self.df_final[col].tolist()

    # função para retornar valores
    def get_response(self):
        if self.add == True:
            return self.df
        else:
            return self.df_final

    def find_med(self):
        import re

        # puxando nome do item e deixando tudo minusculo 
        item_name = str(self._df_[self.columns_title]).lower()

        # lista com o valor das medidas
        lista_val = []
        # lista com o tipo de medida
        lista_med = []

        # regex para extrair valor e unidade de medida
        pattern = r'(\d+\.?\d*)(\w+)'

        # extrair todos os valores e unidades de medida do nome do item
        valores = re.findall(pattern, item_name)

        # iterar sobre cada valor e unidade de medida encontrado
        for val, med in valores:
            # inserir valor e unidade de medida nas listas correspondentes
            lista_val.append(val)
            lista_med.append(med)

        # salvando lista de valores e unidades de medida em objeto self para retorno da classe
        self.lista_val = lista_val
        self.args = lista_med if len(lista_med) > 0 else None
        self.limit = len(self.args) - 1 if self.args else None

    ### Processo para tratar nome de medidas
    def char_vector_generator(self):
        final = []
        for name in self.args:
            final.append(list(name))
        self.args = tuple(final)

    def get_med(self, x, lev_limit=2):
        # onjeto que ira receber a media
        menor = [100]
        # rodando medidas da classe
        for med in self.dic_med['Names'].keys():
            # puxando distancia de lev entre a med do df e da lista da classe
            lev = nltk.edit_distance(self.args[x], med)
            # lev tem um limite de 2
            if lev > lev_limit:
                continue
            # puxando menor lev de todos
            elif menor[-1] > lev and lev < lev_limit:
                menor = [self.args[x], self.dic_med['Names'][med], med, lev]
        # se verdade encontramos uma medida proxima e insermos na lista, caso contrário, consideramos que não encontramos nd
        if not menor[-1] == 100:
            self.lista.append(menor)
        # função recursiva
        if x < self.limit:
            self.get_med(x + 1)

    def get_score_metric(self, view_list=False):
        # index para puxar da lista self.lista_val
        i = -1
        # listas a serem retornadas
        type_list = []
        metric_list = []
        value_list = []
        # processo para retornar dic final com visualização das medidas e metricas encontradas e inserir informação no df final
        for result in self.lista:
            i += 1
            if result[-1] == None:
                continue

            if view_list == True:
                lista = [{'name': str(result[0]),
                          "type": result[1],
                          "type_class": result[2],
                          "lev": result[3],
                          "metric": self.dic_med['data'][result[1]][result[2]]
                          }]
            type_list.append(result[2])
            metric_list.append(self.dic_med['data'][result[1]][result[2]])
            value_list.append(self.lista_val[i])

        dic_final = {"type_class": [type_list],
                     "metric": [metric_list],
                     "value": [value_list]
                     }
        # lista_final.append(lista_append)
        return dic_final
