import pandas as pd
import requests

listaId = ['45639659',
'365917710',
'373617529',
'34090144',
'43639794',
'29797041',
'604869978',
'604869573',
'66702811',
'66702811',
'204642847',
'226868161',
'219651196',
'191209177',
'194451999',
'469817633',
'224433916',
'191716863',
'38294839',
'352918090',
'571820306',
'217535017',
'217050751',
'329517163',
'32488665',
'594916877',
'192116876',
'5195855',
'198298650',
'211864243',
'212664279',
'363717314',
'4461282',
'576917348',
'564919561',
'566219496',
'584318512',
'560419465',
'432616701',
'405318324',
'306921686',
'410018217',
'42820544',
'47111619',
'11936678',
'98218390',
'35796023',
'32196315',
'220567454',
'45243913',
'163917370',
'31091345',
'585216911',
'33688766',
'203180295',
'572619693',
'590018411',
'602517379',
'95037589',
'194538574',
'211179264',
'32391387',
'556020178',
'598618491',
'604821245',
'42719938',
'29994225',
'584818492',
'564919992',
'604820560',
'210788656',
'426116971',
'99518361',
'203602566',
'584818490',
'41212147',
'199036178',
'33398064',
'90229404',
'480217693',
'209994895',
'368417514',
'589418371',
'40537540',
'42116557',
'529116884',
'197066204',
'600518456',
'580218356',
'40918542',
'215855015']
tabelaGeral = pd.DataFrame()

for i in range(0,len(listaId)):
    cookies = {
        '_hjSessionUser_3454957': 'eyJpZCI6ImM2OWQ5N2E4LWM4NTgtNTBjOS1iYmVjLWFhM2FlYWE3YWJjZiIsImNyZWF0ZWQiOjE2OTEyNDE0MjQ2NTMsImV4aXN0aW5nIjp0cnVlfQ==',
        '_vwo_uuid_v2': 'D67FC3A67EC90F143FD5BD33A63188D75|57cf0bd2944d5b0c3ed6c0b7d88f8a5c',
        'SESSION': 'NDk5Nzg3NmItNjFkZC00ZTI2LWJiZTAtZWM2NDk4MWRlM2U1',
        '_gid': 'GA1.3.232959128.1700943668',
        '_clck': '1ghpgkz%7C2%7Cfh0%7C0%7C1312',
        '_hjIncludedInSessionSample_3454957': '0',
        '_hjSession_3454957': 'eyJpZCI6IjAyNzlkMWNkLWY0NzEtNDBmYS1iMDU0LTNkNWFmOGQxOTFjNCIsImNyZWF0ZWQiOjE3MDA5NDM2Njg0MjcsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=',
        '_hjAbsoluteSessionInProgress': '0',
        '_ga': 'GA1.3.786739927.1691241425',
        '_clsk': 'sobwmk%7C1700943811598%7C5%7C1%7Cr.clarity.ms%2Fcollect',
        '_gat_gtag_UA_1665737_25': '1',
        '_ga_1W47Q0QRQW': 'GS1.1.1700943667.8.1.1700943815.57.0.0',
    }

    headers = {
        'authority': 'portaldatransparencia.gov.br',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'referer': f'https://portaldatransparencia.gov.br/despesas/favorecido?paginacaoSimples=true&tamanhoPagina=&offset=&direcaoOrdenacao=asc&colunasSelecionadas=data%2CdocumentoResumido%2ClocalizadorGasto%2Cfase%2Cespecie%2Cfavorecido%2CufFavorecido%2Cvalor%2Cug%2Cuo%2Corgao%2CorgaoSuperior%2Cgrupo%2Celemento%2Cmodalidade%2CplanoOrcamentario%2Cautor&de=01%2F10%2F2023&ate=22%2F11%2F2023&favorecido={listaId[i]}&faseDespesa=3&ordenarPor=valor&direcao=desc',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'paginacaoSimples': 'true',
        'tamanhoPagina': '15',
        'offset': '0',
        'direcaoOrdenacao': 'desc',
        'colunaOrdenacao': 'valor',
        'colunasSelecionadas': 'data,documentoResumido,localizadorGasto,fase,especie,favorecido,ufFavorecido,valor,ug,uo,orgao,orgaoSuperior,grupo,elemento,modalidade,planoOrcamentario,autor,subTitulo,funcao,subfuncao,programa,acao',
        'de': '01/10/2023',
        'ate': '26/11/2023',
        'favorecido': f'{listaId[i]}',
        'faseDespesa': '3',
        '_': '1700943815693',
    }

    response = requests.get(
        'https://portaldatransparencia.gov.br/despesas/favorecido/resultado',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    print(response)

    dicionario = response.json()
    dadosFavorecido = dicionario['data']

    tabelaDespesaIndividual = pd.DataFrame(dadosFavorecido)
    tabelaGeral = pd.concat([tabelaGeral, tabelaDespesaIndividual])

    print(listaId[i],'foi somado a tabelaGeral')

print(tabelaGeral)

filtroTabela = tabelaGeral[['data','favorecido','valor','ug','orgao','planoOrcamentario']]

filtroTabela.to_csv('consultaGeral.csv',encoding = 'utf-8-sig',index=False)

#########

# filtro avancado

tabelaGeral_resumido = tabelaGeral[['data', 'documento', 'observacao',
                                    'acao', 'nomeFavorecido', 'valor',
                                    'ug', 'orgao','planoOrcamentario'
                                  ]]

tabelaGeral_resumido = tabelaGeral_resumido.copy()

tabelaGeral_resumido.rename(columns={'nomeFavorecido': 'Nome',
                                     'valor':'Valor',
                                     'ug':'Unidade Gestora',
                                     'orgao':'Unidade Orcamentaria'
                                     }, inplace=True)


# Filtro de acúmulos

fora_do_escopo = tabelaGeral_resumido.query(" `Unidade Gestora` != ['PRO-REITORIA DE ASSUNTOS ESTUDANTIS - PROAES','PRO-REITORIA DE EXTENSAO']")

# Resta agora realizar uma conferência se os bolsistas acima de fato receberam bolsa da Proexc simultaneamente com outra

nomes = fora_do_escopo['Nome'].unique()
possivel_acumulo = tabelaGeral_resumido[tabelaGeral_resumido['Nome'].isin(nomes)]

possivel_acumulo.to_csv('possivel_acumulo.csv',encoding = 'utf-8-sig', index = False)