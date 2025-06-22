als

-- Este arquivo contém exemplos de erros para teste do analisador

-- Identificador mal formado (começa com número)
intn 1abc

-- Identificador com símbolo inválido
txt nome@

-- Símbolo não pertencente à linguagem
intn valor @

-- Número mal formado
den preco <= 2.a3

-- String não fechada
wrt "Esta string não tem fechamento

-- Identificador muito longo
intn minha_variavel_com_nome_muito_muito_muito_longo_demais

-- Número muito longo
intn numero <= 123456789012345678901234567890
