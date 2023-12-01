# Automação na conferência de acúmulo de bolsas estudantis. 

O objetivo deste projeto é desenvolver um algoritmo em Python para consultar o portal da transparência e verificar se há acúmulo de bolsas de auxílio financeiro a estudantes na Universidade Federal de Pernambuco (UFPE). Essa verificação é necessária porque a resolução da Consad/UFPE proíbe o acúmulo de auxílios financeiros a estudantes com recursos provenientes do Governo Federal. Caso seja identificado algum acúmulo, o setor financeiro deve suspender o pagamento da bolsa e solicitar a devolução do recurso do mês acumulado.

O problema que motivou este projeto é a falta de um sistema integrado entre as unidades que concedem auxílios financeiros a estudantes na UFPE, o que obriga o setor financeiro a realizar uma consulta manual no portal da transparência para cada um dos quase 500 bolsistas pagos. Essa consulta manual é demorada e repetitiva, levando em média de um a dois dias para ser concluída.

A solução proposta neste projeto é automatizar essa consulta usando a API do portal da transparência, que permite acessar os dados das despesas por favorecido de forma rápida e eficiente. Com o algoritmo em Python, é possível realizar a consulta em cerca de 10 minutos, gerando uma tabela de possíveis acúmulos ou situações de excepcionalidade na folha de pagamento, que devem ser analisadas pelo setor financeiro.

Este projeto é um exemplo de como a programação pode tornar o ambiente organizacional mais eficiente por meio da automação de tarefas.

O código em Python é simples, mas que pode servir de base para outros projetos que tenham como parte o consumo de API´s do Portal da Transparência.
