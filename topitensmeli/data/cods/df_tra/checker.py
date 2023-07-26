from data.cods.df_tra._utils.stopwords import string_validate
from data.cods.df_tra._utils.uni_med import Uni_Medida

class df_checker():
    def __init__(self,df,name_column='Item Title',column_response='nome ajustado') -> None:
        print("Validando strings")
        df_final_e1 = string_validate(df,name_column,column_response).get_response()
        print("Validando strings---------------> OK")
        print("validando Unidades de medida")
        self.df_final = Uni_Medida(df_final_e1,column_response,add=True).get_response()
        print("validando Unidades de medida ---> OK")
    
    def response(self):
        return self.df_final


def buckt(x):
    if x<=80:
        return "<80"
    elif 80<x<=120:
        return "80->120"
    elif 120<x<=250:
        return "120->250"
    elif 250<x<=500:
        return "250->500"
    elif 500<x<=1000:
        return "500->1000"
    elif 1000<x<=1500:
        return "1000->1500"
    elif 1500<x<=2000:
        return "1500->2000"
    else:
        return ">2000"
                