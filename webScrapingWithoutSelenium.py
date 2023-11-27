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
                "07241584481",
                "03305378220",
                "05106873002",
                "04144741982",
                "08454306455",
                "04492410333",
                "07695767450",
                "08288209459",
                "12681757495",
                "71059282470",
                "10825731402",
                "70552693421",
                "47893319895",
                "10030348455",
                "10816691444",
                "14179556430",
                "62549103491",
                "70612680428",
                "12632664446",
                "70372752470",
                "70285260464",
                "13317838442",
                "13445554463",
                "13826693485",
                "71704432448",
                "10580814467",
                "11595664459",
                "13594415490",
                "11363283430",
                "10785845402",
                "70444381481",
                "70815103450",
                "71123501408",
                "12338344448",
                "71395109460",
                "13132260410",
                "13365000429",
                "71372775439",
                "71526283433",
                "70976908441",
                "10295757469",
                "12832948421",
                "71489809414",
                "10286137410",
                "12991070447",
                "11858717485",
                "13173902459",
                "19393083487",
                "70789931443",
                "14470421405",
                "70171443411",
                "13646372435",
                "70436291444",
                "13151133410",
                "71143875478",
                "70696885476",
                "70871617412",
                "12485427461",
                "71845910460",
                "71539993450",
                "71479907499",
                "13294222440",
                "70591685400",
                "11696367484",
                "14326489421",
                "12187512401",
                "13576624406",
                "71597447480",
                "70560799462",
                "23755592827",
                "16001773440",
                "13368101498",
                "70971183422",
                "70243679467",
                "13314613407",
                "11802957499",
                "71104711443",
                "13899051440",
                "10648511421",
                "13325830404",
                "13262519456",
                "13275393499",
                "71551100436",
                "15045920421",
                "13438802465",
                "13551251460",
                "50224294890",
                "13962214410",
                "70624699471",
                "71599192462",
                "71625877471",
                "14449391497",
                "15518945485",
                "11035167441",
                "71123356475",
                "15705646470",
                "70246668466",
                "11969278471",
                "70809078457",
                "12011520460",
                "71209977427",
                "12058690427",
                "12866930479",
                "15327910466",
                "71053932464",
                "14639037406",
                "13367571407",
                "14482137464",
                "15256218409",
                "11630988413",
                "70501757490",
                "14092966440",
                "18577654788",
                "14887082401",
                "70794897410",
                "13204189457",
                "13877047459",
                "70424221470",
                "71033654400",
                "14564563424",
                "12871247471",
                "70557617430",
                "16476293494",
                "13011799490",
                "15912893430",
                "13286155454",
                "70386237450",
                "13452055469",
                "15506103417",
                "12611871485",
                "13810956406",
                "13355461466",
                "12297552416",
                "16587830420",
                "14635598446",
                "71144750474",
                "15306833438",
                "14685211448",
                "12428682407",
                "70414896475",
                "14450641469",
                "13441126416",
                "16184096460",
                "14389291459",
                "15760255436",
                "15132070400",
                "14687491456",
                "14431559426",
                "71512288489",
                "13207590411",
                "14785440406",
                "14885393400",
                "16455522419",
                "16974983450",
                "15149687464",
                "71310271461",
                "13979866467",
                "11140715445",
                "70296512435",
                "11141066408",
                "48077519806",
                "11272037460",
                "11621146499",
                "70929668413",
                "11382464410",
                "70292593430",
                "70621356409",
                "10841925437",
                "70411887440",
                "70785826408",
                "71043409475",
                "14370712440",
                "70476790492",
                "70414023471",
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
                "14498407440",
                "11798183420",
                "70191232440",
                "71497183456",
                "10465778402",
                "12212150431",
                "12016972475",
                "11802496408",
                "11346808481",
                "70741245400",
                "11404955429",
                "13510158423",
                "70506927431",
                "11772400416",
                "70263142469",
                "10456310436",
                "22916737855",
                "11869945417",
                "10418688478",
                "13545460401",
                "71126222470",
                "14246840483",
                "70259567400",
                "70553783467",
                "13600735403",
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
                "11439694486",
                "11724917471",
                "71368877478",
                "11932029494",
                "10004569431",
                "11267888482",
                "11150128437",
                "11225075424",
                "70611146495",
                "11943210462",
                "10785335471",
                "70359351425",
                "71492595454",
                "13469730407",
                "13324678498",
                "48475430848",
                "10346851475",
                "46556096806",
                "13895964433",
                "13362294464",
                "70285740407",
                "71560253410",
                "70602448409",
                "12180263406",
                "13707578402",
                "70615852424",
                "14015025474",
                "70407097406",
                "14683649446",
                "71028632410",
                "12735743462",
                "13454983495",
                "10318762439",
                "10518721469",
                "70305041436",
                "70416430422",
                "71197505423",
                "71138766410",
                "70183361474",
                "70494440490",
                "70957737424",
                "12520582413",
                "11751737462",
                "11390564410",
                "71372531483",
                "14546568401",
                "14066928404",
                "13769452402",
                "10698674464",
                "13461340499",
                "13451893460",
                "10851705430",
                "10726873489",
                "10740816411",
                "10651584400",
                "11925818497",
                "11481346466",
                "12095013417",
                "70619606479",
                "12214777490",
                "12975112475",
                "11333728484",
                "17184429478",
                "12449267441",
                "13922563481",
                "70798987499",
                "11416210458",
                "71143385462",
                "13072395446",
                "46498003820",
                "70948717408",
                "12641883406",
                "11831523450",
                "70317571427",
                "10728964430",
                "70612452476",
                "13328915435",
                "70598182438",
                "11224676483",
                "11774547422",
                "71345437498",
                "11105229408",
                "13243397480",
                "70978054474",
                "70427432456",
                "12918842460",
                "10624318478",
                "10251539440",
                "13222513473",
                "12796745473",
                "70471739430",
                "12175356400",
                "14681182427",
                "71744335451",
                "70616489455",
                "15933618403",
                "70582352444",
                "10792381408",
                "71235053440",
                "11974748464",
                "11743797400",
                "12398943410",
                "13277662489",
                "11134136463",
                "14168515427",
                "12811527494",
                "14292504458",
                "11687337403",
                "12626523402",
                "52848958863",
                "11356983413",
                "70790992426",
                "11568098430",
                "12864847400",
                "14511725403",
                "12311718479",
                "70548990409",
                "13166691499",
                "70877984484",
                "11336763400",
                "13696279471",
                "70544703464",
                "70931599407",
                "13763851470",
                "11198492414",
                "11392679494",
                "11243630418",
                "10350914451",
                "12267029456",
                "14207879420",
                "12631844483",
                "10510719414",
                "70571730400",
                "13697991442",
                "13558647475",
                "11463803486",
                "71696781442",
                "13693068496",
                "10942766423",
                "11740478444",
                "11427479488",
                "71408732408",
                "11430483423",
                "12794491440",
                "70614690480",
                "70654198276",
                "11784928429",
                "13484409452",
                "10265214408",
                "13395291499",
                "11970123460",
                "10897614496",
                "15091707409",
                "13055553411",
                "13614372430",
                "36031780410",
                "13774955409",
                "71533347425",
                "15117515412",
                "11924007479",
                "11931840458",
                "13842227400",
                "71583473467",
                "70235523402",
                "12756292451",
                "11645959465",
                "12572855488",
                "71513347454",
                "12236471459",
                "13608994483",
                "13678296408",
                "70639011411",
                "13600845411",
                "71257961179",
                "10355512416",
                "11964749409",
                "14462359470",
                "11118485483"
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

    time.sleep(1)
    pyautogui.click(1217,98)

    time.sleep(0.5)
    pyautogui.click(1210, 458)

    time.sleep(1)
    pyautogui.hotkey('ctrl','home')

#########

# remover " da lista

caractere_para_remover = '"'

# Nova lista com o caractere removido
listaId = [item.replace(caractere_para_remover, '') for item in idFavorecido]

idList = pd.DataFrame(listaId)

idList.to_csv('id.csv', index= False)
#########

# Requisicao com id de parametro

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

    dicionario = response.json()
    dadosFavorecido = dicionario['data']

    tabelaDespesaIndividual = pd.DataFrame(dadosFavorecido)
    tabelaGeral = pd.concat([tabelaGeral, tabelaDespesaIndividual])

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

fora_do_escopo = tabelaGeral_resumido.query(" `Unidade Gestora` != ['PRO-REITORIA DE ASSUNTOS ESTUDANTIS - PROAES','PRO-REITORIA DE EXTENSAO']")

# Resta agora realizar uma conferência se os bolsistas acima de fato receberam bolsa da Proexc simultaneamente com outra

nomes = fora_do_escopo['Nome'].unique()
possivel_acumulo = tabelaGeral_resumido[tabelaGeral_resumido['Nome'].isin(nomes)]

possivel_acumulo.to_csv('possivel_acumulo.csv',encoding = 'utf-8-sig', index = False)