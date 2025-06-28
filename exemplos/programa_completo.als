als

-- Programa completo demonstrando recursos da linguagem ALAIAS

-- Declaração de variáveis
intn idade
txt nome
bln adulto
den salario

-- Declaração de variáveis
nome <= "João Silva"
idade <= 25
salario <= 3500.75

-- Estrura condicional
cdt [ idade ge 18 ]
    adulto <= valid
    wrt "Pessoa adulta"
    
    cdt [ salario gt 3000.0 ]
        wrt "Salário bom"
    !cdt+ [ salario gt 1500.0 ]
        wrt "Salário médio"
    !cdt
        wrt "Salário baixo"
!cdt
    adulto <= invalid
    wrt "Pessoa menor de idade"

-- Estrutura de repetição
intn contador
contador <= 1

during [ contador le 5 ]
    wrt "Contador: "
    wrt contador
    contador <= contador + 1
    brkln

-- Repetição com range fixo
repeat contador in 3
    wrt "Repetição número "
    wrt contador
    brkln

wrt "Programa finalizado"
