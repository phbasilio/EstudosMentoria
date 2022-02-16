import pandas as pnd

#Formtar o campo de data
def ajustar_dt(df):

    df['data_pregao'] = pnd.to_datetime(df['data_pregao'], format='%Y%m%d')

    return df
#Fim Formatar Data

#Formtar campos númericos
def ajustar_valores(df, coluna):

    df[coluna] = (df[coluna]/100).astype(float)

    return df[coluna]
#Fim Formatar campos númericos

    #df['Preço_Abertura'] = (df['Preço_Abertura']/100).astype(float)
    #df['Preço_Máximo'] = (df['Preço_Máximo']/100).astype(float)
    #df['Preço_Mínimo'] = (df['Preço_Mínimo']/100).astype(float)
    #df['Preço_Fechamento'] = (df['Preço_Fechamento']/100).astype(float)


# """ df['Preço_Fechamento'] = df['Preço_Fechamento'].apply(
#         lambda x: str(x).replace('.', ',')) """

# # df['Preço_Fechamento'].apply(substituir)
