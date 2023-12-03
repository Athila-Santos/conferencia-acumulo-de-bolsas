# Automação na conferência de acúmulo de bolsas estudantis. 

O objetivo inicial deste projeto é desenvolver um algoritmo em Python para coletar despesas por favorecido no portal da transparência. Através dessa consulta, é realizada uma verificação se os bolsistas da folha de pagamentos da Pro Reitoria de Extensão acumulou o recebimento de auxílio financeiro a estudantes com outra unidade pagadora. A realização desta verificação é essencial devido à vigência de uma resolução do Conselho na UFPE que proíbe o acúmulo de auxílios financeiros a estudantes com recursos provenientes do Governo Federal. Caso seja identificado acúmulo, o setor financeiro deve suspender o pagamento da bolsa e solicitar a devolução do recurso do mês acumulado.

A origem deste projeto reside na ausência de um sistema integrado do Governo Federal para verificar acumulações. Essa lacuna obriga o setor financeiro da Pro Reitoria de Extensão a realizar consultas manuais no portal da transparência, abrangendo 500 bolsistas presentes na folha de pagamento. Contudo, essa abordagem manual revela-se morosa e repetitiva, demandando, em média, de um a dois dias para conclusão.

A solução proposta é automatizar a conferência usando a API do portal da transparência, que permite acessar os dados das despesas por favorecido de forma rápida e eficiente. Com o algoritmo em Python, é possível realizar a consulta em cerca de 10 minutos, gerando uma tabela de possíveis acúmulos ou situações de excepcionalidade na folha de pagamento, que devem ser analisadas pelo setor financeiro.

## Considerações finais

O projeto serviu de bastante aprendizado e para experenciar uma gama de ferramentas na Ciência de Dados, principalmente no processo de extração. Segue abaixo um breve relatório de como se deu o projeto até sua conclusão:

1. A Api do Portal da Transparência que estava sendo testada para uso ( inserir link da api) possuía uma limitação de requisições por segundo, o que pôde ser facilmente solucionado com a library rateLimiter do Python, que restringe o laço for para uma dada frequência delimitada;
2. O maior impecilho que tornou o uso da Api inviável foi o atraso na atualização das informações de pagamento. Ou seja, apenas se podia realizar a conferência referente ao mês de setembro em outubro, as informações não se atualizam na mesma frequência que o Portal da Transparência. Após descobrir isso, passei um tempo frustrado. No entanto, depois de alguns dias descobri o Web Scraping, que possibilita a raspagem de dados da própria página web.
3. Para pôr em prática o Web Scraping, precisei entender um pouquinho melhor como funciona uma página web, até que consegui consumir a Api que o Portal utiliza e é atualizada com mais frequência.
4. No meio do processo também desenvolvi um script de automação de teclado e mouse no Python, pois o parâmetro para consumo da Api é o id do favorecido no banco de dados do Portal e não o CPF. Automatizei a coleta dos ids no código fonte html, tendo em vista que eram 500 bolsistas.
5. Tudo estava perfeito. A Api escondida que o portal utilizava respondia as requisições sem restrições por minuto, a library Pandas do Python me possibilitou aplicar um filtro que me devolvia apenas pagamentos suspeitos de acúmulo. A única coisa que ainda me inquietava era implementação desse processo na rotina do setor financeiro. Apesar da solução otimizadora do processo de conferência de acúmulos, ainda restava tornar uma rotina acessível para todos os integrantes do ambiente organizacional.
6. Reescrevi o código Python para a linguagem VBA, pois desse modo a utilização encontra-se num software em que todos já estão mais familiarizados como o MS Excel.
7. Para isso, precisei instalar uma biblioteca vba para tratar arquivos Json. Resta apenas inserir os botões e as caixas de mensagem, assim tornarei a utilização da Api intuitiva e a implementação uma realidade.
