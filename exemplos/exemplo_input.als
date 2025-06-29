als

-- Exemplo demonstrando o uso do comando input
intn numero
txt nome
den valor

-- Comandos input corretos
input(numero)
input(nome)
input(valor)

-- Processamento dos dados
cdt [ numero gt 0 ]
    wrt "Número positivo"
!cdt
    wrt "Número negativo ou zero"

wrt "Nome digitado: nome"
wrt "Valor digitado: valor"

-- Exemplos de erros com input (comentados para não gerar erro)
-- input numero -- Erro: falta parênteses
-- input() -- Erro: falta variável
-- input(naoDeclarada) -- Erro: variável não declarada
-- inp(numero) -- Erro: palavra reservada mal formada
