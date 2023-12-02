# Automação na conferência de acúmulo de bolsas estudantis. 

O objetivo inicial deste projeto é desenvolver um algoritmo em Python para coletar despesas por favorecido no portal da transparência. Através dessa consulta, é realizada uma verificação se os bolsistas da folha de pagamentos da Pro Reitoria de Extensão acumulou o recebimento de auxílio financeiro a estudantes com outra unidade pagadora. A realização desta verificação é essencial devido à vigência de uma resolução do Conselho na UFPE que proíbe o acúmulo de auxílios financeiros a estudantes com recursos provenientes do Governo Federal. Caso seja identificado acúmulo, o setor financeiro deve suspender o pagamento da bolsa e solicitar a devolução do recurso do mês acumulado.

A origem deste projeto reside na ausência de um sistema integrado do Governo Federal para verificar acumulações. Essa lacuna obriga o setor financeiro da Pro Reitoria de Extensão a realizar consultas manuais no portal da transparência, abrangendo 500 bolsistas presentes na folha de pagamento. Contudo, essa abordagem manual revela-se morosa e repetitiva, demandando, em média, de um a dois dias para conclusão.

A solução proposta é automatizar a conferência usando a API do portal da transparência, que permite acessar os dados das despesas por favorecido de forma rápida e eficiente. Com o algoritmo em Python, é possível realizar a consulta em cerca de 10 minutos, gerando uma tabela de possíveis acúmulos ou situações de excepcionalidade na folha de pagamento, que devem ser analisadas pelo setor financeiro.

## Considerações finais

O projeto serviu de bastante aprendizado e para experenciar uma gama de ferramentas na Ciência de Dados, principalmente no processo de extração. No início do projeto, não contava com as dificuldades que serão listadas abaixo:

1. A Api do Portal da Transparência que estava sendo testada para uso ( inserir link da api) possuía uma limitação de requisições por segundo, o que pôde ser facilmente solucionado com a library rateLimiter do Python, que restringe o laço for para uma dada frequência delimitada;
2. O maior impecilho que tornou o uso da Api inviável foi um atraso nas respostas.
3.
