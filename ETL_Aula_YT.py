# Importar as bibliotecas

# from dataclasses import replace
import pandas as pd
import Transformacoes as trf


def ler_arquivo_ibov(pasta: str, nome_aquivo: str, ano: str, tipo_arquivo: str) -> pd.DataFrame:

    _arquivo = f'{pasta}{nome_aquivo}{ano}.{tipo_arquivo}'

    cols = [(2, 10),
            (10, 12),
            (12, 24),
            (24, 39),
            (56, 69),
            (69, 82),
            (82, 95),
            (108, 121),
            (152, 170),
            (170, 188)
            ]

    cols_names = ['data_pregao', 'cod_bdi', 'Sigla_Ação', 'Nome_Ação', 'Preço_Abertura',
                  'Preço_Máximo', 'Preço_Mínimo', 'Preço_Fechamento', 'Qtd_Tit_Negociados', 'Volume_Negociado']

    # df = pd.read_fwf('C://Users//DTI Digital//Documents//Trabalho//Mentoria//Mentoria Atual - Engenharia de Dados//Bases e  Programas//COTAHIST_A2020//COTAHIST_A2020.TXT',
    #                 colspecs=cols, names=cols_names, skiprows=1)

    df = pd.read_fwf(_arquivo, colspecs=cols, names=cols_names, skiprows=1)

    return df

    #pd.DataFrame.groupby('data_pregao').agg({'Qtd_Tit_Negociados': sum})


"""     lista_soma = list(map(lambda x: sum(x), cols))

    lst_soma = []

    for x in cols:
        lst_soma.append(sum(x)) """

#df_teste = pd.DataFrame([(1,2),(2,2)],columns=['Coluna1','Coluna2'])

# [{'Coluna1':1,'Coluna2':2},{'Coluna1':2,'Coluna2':2}]


# filtrar
def filtrar_arq(df):
    df = df[df['cod_bdi'] == 2]
    df = df.drop(['cod_bdi'], 1)

    return df


def substituir(vlr_fechamento):

    vlr_fechamento = str(vlr_fechamento).replace('.', ',')

    return vlr_fechamento


def unificar_arqs(pasta, nm_arquivo, ano_dt: list, tipo_arq, arq_unico):

    for i, y in enumerate(ano_dt):
        arq_df = ler_arquivo_ibov(pasta, nm_arquivo, y, tipo_arq)
        arq_df = filtrar_arq(arq_df)
        # ajustar campos de data
        arq_df = trf.ajustar_dt(arq_df)
        # Formatar campos númericos
        arq_df['Preço_Abertura'] = trf.ajustar_valores(
            arq_df, 'Preço_Abertura')
        arq_df['Preço_Máximo'] = trf.ajustar_valores(arq_df, 'Preço_Máximo')
        arq_df['Preço_Mínimo'] = trf.ajustar_valores(arq_df, 'Preço_Mínimo')
        arq_df['Preço_Fechamento'] = trf.ajustar_valores(
            arq_df, 'Preço_Fechamento')

        if i == 0:
            df_unificado = arq_df
        else:
            df_unificado = pd.concat([df_unificado, arq_df])

    var_caminho = '{}//{}'.format(pasta, arq_unico)

    df_unificado.to_csv(var_caminho, index=False)
    #df_unificado.to_csv(f'{pasta}//{arq_unico}', index=False)


# Rodar etl
ano = ['2018', '2019', '2020']
pasta = f'C://Users//DTI Digital//Documents//Trabalho//Mentoria//Mentoria Atual - Engenharia de Dados//Bases e  Programas//Bases_Bovespa//'
nome_aquivo = 'COTAHIST_A'
tipo_arquivo = 'txt'

arq_unico = 'arquivos_unificados.csv'

unificar_arqs(pasta, nome_aquivo, ano, tipo_arquivo, arq_unico)

# df['Preço_Abertura'].replace('.',',')

# print(df.dtypes)
