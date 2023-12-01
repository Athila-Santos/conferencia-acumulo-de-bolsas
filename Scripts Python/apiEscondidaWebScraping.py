import pandas as pd
import requests
import numpy as np

listaId = [] # inserir id dos favorecidos nesse campo

tabelaGeral = pd.DataFrame()

for i in range(0,len(listaId)):
    headers = {
        'authority': 'portaldatransparencia.gov.br',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'referer': f'https://portaldatransparencia.gov.br/despesas/favorecido?paginacaoSimples=true&tamanhoPagina=&offset=&direcaoOrdenacao=asc&colunasSelecionadas=data%2CdocumentoResumido%2ClocalizadorGasto%2Cfase%2Cespecie%2Cfavorecido%2CufFavorecido%2Cvalor%2Cug%2Cuo%2Corgao%2CorgaoSuperior%2Cgrupo%2Celemento%2Cmodalidade%2CplanoOrcamentario%2Cautor&de=01%2F10%2F2023&ate=30%2F11%2F2023&favorecido={listaId[i]}&faseDespesa=3&ordenarPor=valor&direcao=desc',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'x-requested-with': 'XMLHttpRequest'
    }

    params = {
        'paginacaoSimples': 'true',
        'tamanhoPagina': '15',
        'offset': '0',
        'direcaoOrdenacao': 'desc',
        'colunaOrdenacao': 'valor',
        'colunasSelecionadas': 'data,documentoResumido,localizadorGasto,fase,especie,favorecido,ufFavorecido,valor,ug,uo,orgao,orgaoSuperior,grupo,elemento,modalidade,planoOrcamentario,autor,subTitulo,funcao,subfuncao,programa,acao',
        'de': '01/10/2023',
        'ate': '30/11/2023',
        'favorecido': f'{listaId[i]}',
        'faseDespesa': '3',
        '_': '1701179305298'
    }

    print(listaId[i])
    response = requests.get(
        'https://portaldatransparencia.gov.br/despesas/favorecido/resultado',
        params=params,
        headers=headers
    )

    print(response)

    dicionario = response.json()
    dadosFavorecido = dicionario['data']

    tabelaDespesaIndividual = pd.DataFrame(dadosFavorecido)

    num_lines = tabelaDespesaIndividual.shape[0]
    arr = np.full(num_lines, listaId[i])
    tabelaDespesaIndividual = tabelaDespesaIndividual.set_index(arr)

    tabelaGeral = pd.concat([tabelaGeral, tabelaDespesaIndividual])

    print(listaId[i],'foi somado a tabelaGeral')


tabelaGeral.to_csv('tabelaGeral.csv', encoding='utf-8-sig', index=True)

filtroTabela = tabelaGeral[['data', 'nomeFavorecido', 'valor', 'ug', 'orgao']]
filtroTabela.to_csv('consultaGeral.csv',encoding='utf-8-sig',index=True)

#########

# filtro avancado

tabelaGeral_resumido = tabelaGeral[['data', 'documento',
                                    'acao', 'nomeFavorecido', 'valor',
                                    'ug', 'orgao']]

tabelaGeral_resumido = tabelaGeral_resumido.copy()

tabelaGeral_resumido.rename(columns={'nomeFavorecido': 'Nome',
                                     'valor': 'Valor',
                                     'ug': 'Unidade Gestora',
                                     'orgao': 'Unidade Orcamentaria'
                                     }, inplace=True)


# Filtro de acúmulos

fora_do_escopo = tabelaGeral_resumido.query("`Unidade Gestora` != ['PRO-REITORIA DE ASSUNTOS ESTUDANTIS - PROAES','PRO-REITORIA DE EXTENSAO']")

# Resta agora realizar uma conferência se os bolsistas acima de fato receberam bolsa da Proexc simultaneamente com outra

nomes = fora_do_escopo['Nome'].unique()
possivel_acumulo = tabelaGeral_resumido[tabelaGeral_resumido['Nome'].isin(nomes)]

possivel_acumulo.to_csv('possivel_acumulo.csv',encoding='utf-8-sig', index=True)