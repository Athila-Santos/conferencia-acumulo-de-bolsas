import pandas as pd
import time
import requests
import pyautogui
import clipboard

# obstaculo do script: conseguir realizar a consulta do id dos favorecidos
# tempo estimado de 3h30min

favorecido = [ "09005533404",
                "05276599165",
                "02102878295",
                "07767347419",
                "03981297466",
                "09804700484",
                "09967237490",
                "03331777544",
                "08808916456",
                "09919206431",
                "09173108456",
                "08754811406",
                "06536274407",
                "01483740420",
                "05541470331",
                "09913293413",
                "09717675481",
                "07358531426",
                "07471790423",
                "06871324526",
                "07204097300",
                "06499950580",
                "08687571445",
                "06528747385",
                "06337018400",
                "09783662473",
                "09789474440",
                "09733082490",
                "08567825482",
                "09893382408",
                "08282046400",
                "05754572360",
                "08750772341",
                "03180779497",
                "08356716403",
                "09639752428",
                "08579574498",
                "05409103416",
                "08781920423",
                "08738088436",
                "05473963412",
                "09728103409",
                "05369872546",
                "09564797403",
                "06753570470",
                "04367702537",
                "07128980423",
                "05776782481",
                "07777778439",
                "07436231340",
                "09903601484",
                "08097900416",
                "03614754464",
                "09442788418",
                "08353592479",
                "01379247470",
                "09855359461",
                "08747575336",
                "09299822409",
                "09639138401",
                "09795926403",
                "09096629590",
                "09783661400",
                "06591314474",
                "09397637452",
                "08467695498",
                "09233668495",
                "09794505439",
                "08756924437",
                "08018830401",
                "05624493452",
                "07921057454",
                "06708853124",
                "09716703406",
                "09312895486",
                "01767789181",
                "05074131480",
                "04442572410",
                "08090461484",
                "06662263427",
                "05131658438",
                "05351593408",
                "05077500479",
                "08285778460",
                "09803728440",
                "08076288401",
                "09558453439",
                "08381727413",
                "08396758441",
                "09903750480",
                "04560042462",
                "01171471416",
                "06922933451",
                "07241584481"
                ]
idFavorecido = []
barra = 'id="favorecido"'

pyautogui.hotkey('alt','tab')

for i in range(0,len(favorecido)):

    # clicar no no botão favorecido
    time.sleep(2)
    pyautogui.click(218, 605)

    # clicar na guia favorecido

    time.sleep(1)
    pyautogui.click(431, 303)

    # colar cpf

    time.sleep(1)
    pyautogui.write(favorecido[i])

    # esperar e clicar na lista suspensa

    time.sleep(3)
    pyautogui.click(433,334)

    # clicar no botão confirmar

    time.sleep(1)
    pyautogui.click(446,449)

    # clicar no botão atualizar

    time.sleep(1)
    pyautogui.click(1106,227)

    # a partir daqui será ctrl+u

    time.sleep(5)
    pyautogui.hotkey('ctrl','u')

    # ctrl+f

    time.sleep(3)
    pyautogui.hotkey('ctrl','f')

    # paste(id="favorecido"

    time.sleep(1)
    pyautogui.write(barra)

    # copiar trecho de id

    time.sleep(1)
    pyautogui.moveTo(207,432)
    pyautogui.mouseDown()
    pyautogui.moveTo(286,432)
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl','c')

    # salvar na lista

    termo = clipboard.paste()
    idFavorecido.append(termo)

    # ctrl+w

    pyautogui.hotkey('ctrl','w')

    # limpar filtro

    time.sleep(1.5)
    pyautogui.click(1217,98)

    time.sleep(1.5)
    pyautogui.click(1210, 458)

    time.sleep(1)
    pyautogui.hotkey('ctrl','home')

#########

print(idFavorecido)
# remover " da lista

caractere_para_remover = '"'

# Nova lista com o caractere removido
listaId = [item.replace(caractere_para_remover, '') for item in idFavorecido]

idList = pd.DataFrame(listaId)

idList.to_csv('id.csv', index= False)

tabelaCoringa = pd.DataFrame()

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

    dicionario = response.json()
    print("o tipo do response é",type(dicionario))
    dadosFavorecido = dicionario['data']
    print("agora se tornou", type(dadosFavorecido))

    tabelaDespesaIndividual = pd.DataFrame(dadosFavorecido)
    print("Nesse momento é", type(tabelaDespesaIndividual))

    tabelaGeral = pd.concat([tabelaCoringa, tabelaDespesaIndividual])

    filtroTabela = tabelaGeral[['data','favorecido','valor','ug','orgao','planoOrcamentario']]


tabelaGeral.to_csv('consultaGeral.csv',encoding = 'utf-8-sig',index=False)

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

fora_do_escopo = tabelaGeral_resumido.query(" `Unidade Gestora` != ['PRO-REITORIA DE ASSUNTOS ESTUDANTIS - PROAES','PRO-REITORIA DE EXTENSAO'] and `Ano/Mes` == [202310, 202311] ")

# Resta agora realizar uma conferência se os bolsistas acima de fato receberam bolsa da Proexc simultaneamente com outra

nomes = fora_do_escopo['Nome'].unique()
possivel_acumulo = tabelaGeral_resumido[tabelaGeral_resumido['Nome'].isin(nomes)]

possivel_acumulo.to_csv('possivel_acumulo.csv',encoding = 'utf-8-sig', index = False)