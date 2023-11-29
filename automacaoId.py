import pandas as pd
import time
import pyautogui
import clipboard

# obstaculo do script: conseguir realizar a consulta do id dos favorecidos
# tempo estimado de 3h30min

favorec = ["06647828419",
           "70414023471",
           "14370712440",
           "70476790492",
           "12329982496",
           "13586782438",
           "12406582493",
           "11811113400",
           "12863654497",
           "14909761403",
           "13237114499",
           "11387457403",
           "11448524474",
           "43145151800",
           "70055818498",
           "14402127408",
           "70418405492",
           "11636381456",
           "12016972475",
           "11802496408",
           "11346808481",
           "14498407440",
           "12212150431",
           "13510158423",
           "70741245400",
           "11404955429",
           "10465778402",
           "11798183420",
           "70191232440",
           "71497183456",
           "70506927431",
           "11772400416",
           "70263142469",
           "10456310436",
           "70674730470",
           "22916737855",
           "11869945417",
           "10418688478",
           "71126222470",
           "14246840483",
           "70902513494",
           "70259567400",
           "70553783467",
           "13600735403",
           "71157151493",
           "15389492455",
           "13339971404",
           "12009860403",
           "70920554407",
           "71141062461",
           "14416717490",
           "10977383458",
           "11344672493",
           "70588700479",
           "10154439401",
           "71397101474",
           "12037878478",
           "08979853467",
           "11439694486",
           "11724917471",
           "71368877478",
           "10004569431",
           "11267888482",
           "11150128437",
           "11225075424",
           "70611146495",
           "11943210462",
           "10785335471",
           "70359351425",
           "71492595454",
           "12651025461",
           "70447093460",
           "48475430848",
           "10346851475",
           "13335309430",
           "46556096806",
           "16238444444",
           "13362294464",
           "71837731403",
           "09393959404",
           "71560253410",
           "70602448409",
           "12180263406",
           "13707578402",
           "70615852424",
           "14015025474",
           "70407097406",
           "10897614496",
           "71197505423",
           "70619606479",
           "11430483423",
           "05106873002",
           "70548990409",
           "12626523402",
           "70931599407",
           "70957737424",
           "71345437498",
           "13842227400",
           "10510719414",
           "08288209459",
           "11392679494",
           "12520582413",
           "13465405439",
           "71235053440",
           "13072395446",
           "14292504458",
           "12095013417",
           "70790992426",
           "10688115446",
           "70305041436",
           "11974748464",
           "11481346466",
           "12811527494",
           "12572855488",
           "71533347425",
           "70616489455",
           "11774547422",
           "13395291499",
           "13678296408",
           "14462359470",
           "11118485483",
           "13277662489",
           "11568098430",
           "10698674464",
           "70571730400",
           "11463803486",
           "13922563481",
           "70235523402",
           "12735743462",
           "71143385462",
           "13769452402",
           "12641883406",
           "15117515412",
           "13451893460",
           "11784928429",
           "10251539440",
           "13055553411",
           "12236471459",
           "11356983413",
           "70598182438",
           "10518721469",
           "71696781442",
           "10740816411",
           "03305378220",
           "12267029456",
           "70948717408",
           "13222513473",
           "10792381408",
           "13891188439",
           "14168515427",
           "13608994483",
           "71028632410",
           "11336763400",
           "10851705430",
           "11970123460",
           "15933618403",
           "15091707409",
           "13243397480",
           "12449267441",
           "12631844483",
           "70183361474",
           "10728964430",
           "10624318478",
           "12864847400",
           "13774955409",
           "70494440490",
           "70978054474",
           "11743797400",
           "09796481499",
           "13328915435",
           "12527288405",
           "11105229408",
           "11427479488",
           "14681182427",
           "13461340499",
           "12214777490",
           "11333728484",
           "10350914451",
           "11751737462",
           "14546568401",
           "12918842460",
           "04144741982",
           "36031780410",
           "12175356400",
           "14207879420",
           "11924007479",
           "10942766423",
           "14511725403",
           "70582352444",
           "11243630418",
           "11687337403",
           "70798987499",
           "12398943410",
           "12311718479",
           "11740478444",
           "13600845411",
           "70865724466",
           "11754318428",
           "11390564410",
           "70427432456",
           "13696279471",
           "11198492414",
           "11925818497",
           "70612452476",
           "10318762439",
           "17184429478",
           "70639011411",
           "46498003820",
           "12796745473",
           "71138766410",
           "14683649446",
           "70471739430",
           "12794491440",
           "14066928404",
           "10651584400",
           "70544703464",
           "08454306455",
           "10355512416",
           "70416430422",
           "11931840458",
           "07695767450",
           "11831523450",
           "70614690480",
           "70877984484",
           "13484409452",
           "11645959465",
           "11134136463",
           "71156309417",
           "11224676483",
           "70654198276",
           "71408732408",
           "71583473467",
           "04492410333",
           "71257961179",
           "13454983495",
           "13166691499",
           "13697991442",
           "13558647475",
           "12975112475",
           "13763851470",
           "13693068496",
           "71372531483",
           "70317571427",
           "52848958863",
           "11416210458",
           "12756292451",
           "11964749409",
           "14512722432",
           "71513347454"
]
idFavorecido = []
barra = 'id="favorecido"'

pyautogui.hotkey('alt','tab')

for i in range(0,len(favorec)):

    # clicar no no botão favorecido
    time.sleep(2)
    pyautogui.click(94,679)

    # clicar na guia favorecido

    time.sleep(1)
    pyautogui.click(311, 306)

    # colar cpf

    time.sleep(1)
    pyautogui.write(favorec[i])

    # esperar e clicar na lista suspensa

    time.sleep(3)
    pyautogui.click(309,330)

    # clicar no botão confirmar

    time.sleep(1)
    pyautogui.click(313,456)

    # clicar no botão atualizar

    time.sleep(1)
    pyautogui.click(814,228)

    # a partir daqui será ctrl+u

    time.sleep(4)
    pyautogui.hotkey('ctrl','u')

    # ctrl+f

    time.sleep(5)
    pyautogui.hotkey('ctrl','f')

    # paste(id="favorecido"

    time.sleep(2)
    pyautogui.write(barra)

    # copiar trecho de id

    time.sleep(2)
    pyautogui.moveTo(164,434)
    pyautogui.mouseDown()
    pyautogui.moveTo(246,434)
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl','c')

    # salvar na lista

    termo = clipboard.paste()
    idFavorecido.append(termo)

    # ctrl+w

    pyautogui.hotkey('ctrl','w')

    # limpar filtro

    time.sleep(1.5)
    pyautogui.click(929,99)

    time.sleep(1.5)
    pyautogui.click(919, 505)

    time.sleep(1)
    pyautogui.hotkey('ctrl','home')
    print(termo, 'adicionado ao favorecido', favorec[i])

#########

print(idFavorecido)
# remover " da lista

caractere_para_remover = '"'

# Nova lista com o caractere removido
listaId = [item.replace(caractere_para_remover, '') for item in idFavorecido]

idList = pd.DataFrame(listaId)

idList.to_csv('id.csv', index= False)


# tabelaCoringa = pd.DataFrame()
#
# # for i in range(0,len(listaId)):
# #
# #     cookies = {
# #         '_hjSessionUser_3454957': 'eyJpZCI6ImM2OWQ5N2E4LWM4NTgtNTBjOS1iYmVjLWFhM2FlYWE3YWJjZiIsImNyZWF0ZWQiOjE2OTEyNDE0MjQ2NTMsImV4aXN0aW5nIjp0cnVlfQ==',
# #         '_vwo_uuid_v2': 'D67FC3A67EC90F143FD5BD33A63188D75|57cf0bd2944d5b0c3ed6c0b7d88f8a5c',
# #         'SESSION': 'NDk5Nzg3NmItNjFkZC00ZTI2LWJiZTAtZWM2NDk4MWRlM2U1',
# #         '_gid': 'GA1.3.232959128.1700943668',
# #         '_clck': '1ghpgkz%7C2%7Cfh0%7C0%7C1312',
# #         '_hjIncludedInSessionSample_3454957': '0',
# #         '_hjSession_3454957': 'eyJpZCI6IjAyNzlkMWNkLWY0NzEtNDBmYS1iMDU0LTNkNWFmOGQxOTFjNCIsImNyZWF0ZWQiOjE3MDA5NDM2Njg0MjcsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=',
# #         '_hjAbsoluteSessionInProgress': '0',
# #         '_ga': 'GA1.3.786739927.1691241425',
# #         '_clsk': 'sobwmk%7C1700943811598%7C5%7C1%7Cr.clarity.ms%2Fcollect',
# #         '_gat_gtag_UA_1665737_25': '1',
# #         '_ga_1W47Q0QRQW': 'GS1.1.1700943667.8.1.1700943815.57.0.0',
# #     }
# #
# #     headers = {
# #         'authority': 'portaldatransparencia.gov.br',
# #         'accept': 'application/json, text/javascript, */*; q=0.01',
# #         'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
# #         'referer': f'https://portaldatransparencia.gov.br/despesas/favorecido?paginacaoSimples=true&tamanhoPagina=&offset=&direcaoOrdenacao=asc&colunasSelecionadas=data%2CdocumentoResumido%2ClocalizadorGasto%2Cfase%2Cespecie%2Cfavorecido%2CufFavorecido%2Cvalor%2Cug%2Cuo%2Corgao%2CorgaoSuperior%2Cgrupo%2Celemento%2Cmodalidade%2CplanoOrcamentario%2Cautor&de=01%2F10%2F2023&ate=22%2F11%2F2023&favorecido={listaId[i]}&faseDespesa=3&ordenarPor=valor&direcao=desc',
# #         'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
# #         'sec-ch-ua-mobile': '?0',
# #         'sec-ch-ua-platform': '"Windows"',
# #         'sec-fetch-dest': 'empty',
# #         'sec-fetch-mode': 'cors',
# #         'sec-fetch-site': 'same-origin',
# #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
# #         'x-requested-with': 'XMLHttpRequest',
# #     }
# #
# #     params = {
# #         'paginacaoSimples': 'true',
# #         'tamanhoPagina': '15',
# #         'offset': '0',
# #         'direcaoOrdenacao': 'desc',
# #         'colunaOrdenacao': 'valor',
# #         'colunasSelecionadas': 'data,documentoResumido,localizadorGasto,fase,especie,favorecido,ufFavorecido,valor,ug,uo,orgao,orgaoSuperior,grupo,elemento,modalidade,planoOrcamentario,autor,subTitulo,funcao,subfuncao,programa,acao',
# #         'de': '01/10/2023',
# #         'ate': '26/11/2023',
# #         'favorecido': f'{listaId[i]}',
# #         'faseDespesa': '3',
# #         '_': '1700943815693',
# #     }
# #
# #     response = requests.get(
# #         'https://portaldatransparencia.gov.br/despesas/favorecido/resultado',
# #         params=params,
# #         cookies=cookies,
# #         headers=headers,
# #     )
# #
# #     dicionario = response.json()
# #     print("o tipo do response é",type(dicionario))
# #     dadosFavorecido = dicionario['data']
# #     print("agora se tornou", type(dadosFavorecido))
# #
# #     tabelaDespesaIndividual = pd.DataFrame(dadosFavorecido)
# #     print("Nesse momento é", type(tabelaDespesaIndividual))
# #
# #     tabelaGeral = pd.concat([tabelaCoringa, tabelaDespesaIndividual])
# #
# #     filtroTabela = tabelaGeral[['data','favorecido','valor','ug','orgao','planoOrcamentario']]
#
#
# tabelaGeral.to_csv('consultaGeral.csv',encoding = 'utf-8-sig',index=False)
#
# #########
#
# # filtro avancado
#
# tabelaGeral_resumido = tabelaGeral[['data', 'documento', 'observacao',
#                                     'acao', 'nomeFavorecido', 'valor',
#                                     'ug', 'orgao','planoOrcamentario'
#                                   ]]
#
# tabelaGeral_resumido = tabelaGeral_resumido.copy()
#
# tabelaGeral_resumido.rename(columns={'nomeFavorecido': 'Nome',
#                                      'valor':'Valor',
#                                      'ug':'Unidade Gestora',
#                                      'orgao':'Unidade Orcamentaria'
#                                      }, inplace=True)
#
#
# # Filtro de acúmulos
#
# fora_do_escopo = tabelaGeral_resumido.query(" `Unidade Gestora` != ['PRO-REITORIA DE ASSUNTOS ESTUDANTIS - PROAES','PRO-REITORIA DE EXTENSAO'] and `Ano/Mes` == [202310, 202311] ")
#
# # Resta agora realizar uma conferência se os bolsistas acima de fato receberam bolsa da Proexc simultaneamente com outra
#
# nomes = fora_do_escopo['Nome'].unique()
# possivel_acumulo = tabelaGeral_resumido[tabelaGeral_resumido['Nome'].isin(nomes)]
#
# possivel_acumulo.to_csv('possivel_acumulo.csv',encoding = 'utf-8-sig', index = False)