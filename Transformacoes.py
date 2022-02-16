import pandas as pd


def ajustar_dt(df):

    df['data_pregao'] = pd.to_datetime(df['data_pregao'], format='%Y%m%d')

    return df


def ajustar_valores(df, coluna):

    df[coluna] = (df[coluna]/100).astype(float)

    return df[coluna]

    #df['Preço_Abertura'] = (df['Preço_Abertura']/100).astype(float)
    #df['Preço_Máximo'] = (df['Preço_Máximo']/100).astype(float)
    #df['Preço_Mínimo'] = (df['Preço_Mínimo']/100).astype(float)
    #df['Preço_Fechamento'] = (df['Preço_Fechamento']/100).astype(float)


# """ df['Preço_Fechamento'] = df['Preço_Fechamento'].apply(
#         lambda x: str(x).replace('.', ',')) """

# # df['Preço_Fechamento'].apply(substituir)
