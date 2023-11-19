import requests
import pandas as pd
from ratelimiter import RateLimiter

# os.getcwd()
# os.chdir('*****')


# Importando relação de favorecidos

cpfs = pd.read_csv('codpessoa.csv', dtype = {'favorecido': str})

favorecidos = cpfs.values.tolist()

# Conexão *API* do Portal da Transparência

#url recurso recebido

url = "https://api.portaldatransparencia.gov.br/api-de-dados/despesas/recursos-recebidos"

#params

codigoFavorecido = favorecidos
mesAnoFim = '12/2023'
mesAnoInicio = '09/2023'
pagina = 1

# Monta o dicionário com as informações capturadas

params = {"codigoFavorecido": codigoFavorecido,
          "mesAnoFim": mesAnoFim,
          "mesAnoInicio": mesAnoInicio,
          "pagina": pagina
          }

#chave da API

headers = {"chave-api-dados":"1f580edc90fe43ea4a082e6ea3590ca6"}


# *Onde a mágica acontece*


soma_despesas = pd.DataFrame()
codigoFavorecido = favorecidos

# limitador de taxa para permitir no máximo x requisições por minuto
limite = RateLimiter(max_calls = 350, period = 60)

for i in range(0,len(codigoFavorecido)):
    # limitador de taxa em nosso loop
    with limite:
        params = {"codigoFavorecido": codigoFavorecido[i],
                  "mesAnoFim": mesAnoFim,
                  "mesAnoInicio": mesAnoInicio,
                  "pagina": pagina,
                  }
        resultado = requests.get(url, params = params, headers = headers)
        despesas = pd.DataFrame(resultado.json())
        soma_despesas = pd.concat([soma_despesas, despesas])


# *Tratamento dos dados obtidos*

soma_despesas_resumido = soma_despesas[['anoMes',
                                        'nomePessoa',
                                        'valor',
                                        'nomeUG',
                                        'nomeOrgao'
                                      ]]

soma_despesas_resumido = soma_despesas_resumido.copy()

soma_despesas_resumido.rename(columns={'anoMes':'Ano/Mes',
                                        'nomePessoa':'Nome',
                                        'valor':'Valor',
                                        'nomeUG':'Unidade Gestora',
                                        'nomeOrgao':'Unidade Orcamentaria'
                                        }, inplace=True)


# Filtro de acúmulos

fora_do_escopo = soma_despesas_resumido.query(" `Unidade Gestora` != ['PRO-REITORIA DE ASSUNTOS ESTUDANTIS - PROAES','PRO-REITORIA DE EXTENSAO'] and `Ano/Mes` == [202310, 202311] ")

# Resta agora realizar uma conferência se os bolsistas acima de fato receberam bolsa da Proexc simultaneamente com outra

nomes = fora_do_escopo['Nome'].unique()
possivel_acumulo = soma_despesas_resumido[soma_despesas_resumido['Nome'].isin(nomes)]

# Export to csv

possivel_acumulo.to_csv('possivel_acumulo.csv',encoding = 'utf-8-sig', index = False)


# hipótese de inserir todos os dados em um xlsx

# with pd.ExcelWriter('panorama.xlsx') as writer:  
#     possivel_acumulo.to_excel(writer, sheet_name='Acúmulo')
#     soma_despesas_resumido.to_excel(writer, sheet_name='Geral')
