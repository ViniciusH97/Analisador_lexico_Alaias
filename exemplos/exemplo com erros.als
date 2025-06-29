als

-- Este arquivo contém exemplos de erros para teste do analisador

-- Identificador mal formado (começa com número)
intn 498saida

-- Identificador com símbolo inválido
txt nome$%

-- Símbolo não pertencente à linguagem
intn valor $

-- Número mal formado
den preco <= 2.a3

-- String não fechada
wrt "Esta string não tem fechamento

-- Identificador muito longo
intn minha_variavel_com_nome_nome_nome_nome_longo_demais

-- Número muito longo
intn numero <= 123456789012345678901234567890

-- Exemplo com erros de input para teste
intn idade
txt nome

-- Erros de sintaxe do input
input idade -- Erro: falta parênteses
input() -- Erro: falta variável
input(naoDeclarada) -- Erro: variável não declarada
inp(idade) -- Erro: palavra reservada mal formada
in(nome) -- Erro: palavra reservada mal formada

-- Sintaxe correta
input(idade)
input(nome)

wrt "Dados coletados"