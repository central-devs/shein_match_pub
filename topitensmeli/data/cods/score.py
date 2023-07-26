
def check_score(loja_name_shopee,loja_name_meli,incremento_nome_loja,unidade_meli,metricas_meli,valores_meli,
                unidade_shopee,valores_shopee,metrica_unidade,score_string,name_shopee,name_meli):
    # se o nome da loja for o mesmo faremos um incremento
    # if str(loja_name_shopee).lower() == str(loja_name_meli).lower():
    #     score_string = score_string+(score_string*incremento_nome_loja)

    # checando se a string possui kit ou conjunto e a outra tmb:
    if str(name_shopee).lower().count("kit")>0 and str(name_meli).lower().count("kit")==0:
        score_string=None
    elif str(name_shopee).lower().count("kit")==0 and str(name_meli).lower().count("kit")>0:
        score_string=None

    if str(name_shopee).lower().count("conjunto")>0 and str(name_meli).lower().count("conjunto")==0:
        score_string=None
    elif str(name_shopee).lower().count("conjunto")==0 and str(name_meli).lower().count("conjunto")>0:
        score_string=None

    igual = 0 
    for meli_unit, meli_value in zip(unidade_meli, valores_meli):
        for shopee_unit, shopee_value in zip(unidade_shopee, valores_shopee):
            if meli_unit == shopee_unit and meli_value == shopee_value:
                igual+=1

    # fazendo com menor valor de med unica
    if unidade_meli<unidade_shopee:
        score_metrica = igual/len(unidade_meli)
    else:
        score_metrica = igual/len(unidade_shopee)

    if score_string == None:
        return 0,score_metrica
    else:
        return score_string,score_metrica


    