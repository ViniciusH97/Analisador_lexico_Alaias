# Analisador Léxico - Linguagem ALAIAS

## Descrição

Este projeto implementa um analisador léxico completo para a linguagem de programação ALAIAS, desenvolvido em Python com interface gráfica usando Tkinter.

## IDE Utilizada

**IDE:** Visual Studio Code (VSCode)
**Versão Python:** 3.8 ou superior
**Bibliotecas:** Todas são nativas do Python (tkinter, re, enum, dataclasses, typing)

## Estrutura do Projeto

```
Analisador_lexico_Alaias/
├── analisador.py          # Código principal do analisador
├── README.md              # Este arquivo com instruções
└── exemplos/              # (opcional) Arquivos de exemplo .als
```

## Como Executar o Projeto

### Pré-requisitos
1. Python 3.8 ou superior instalado
2. Tkinter (geralmente incluído com Python)

### Passo a Passo para Execução

#### 1. Verificar Instalação do Python
Abra o Prompt de Comando (cmd) e execute:
```cmd
python --version
```
Deve retornar algo como "Python 3.x.x"

#### 2. Navegar para o Diretório do Projeto
```cmd
cd ".\Analisador_lexico_Alaias"
```

#### 3. Executar o Analisador (Interface Gráfica)
```cmd
python analisador.py
```

#### 4. Executar em Modo Console (Opcional)
```cmd
python analisador.py --console
```

## Interface Gráfica

A interface gráfica possui as seguintes funcionalidades:

### Área Principal
- **Código Fonte (Esquerda)**: Editor de texto para inserir código ALAIAS
- **Resultados (Direita)**: Três abas com informações da análise

### Abas de Resultado
1. **Tokens**: Lista todos os tokens identificados
2. **Erros**: Lista apenas os erros encontrados
3. **Estatísticas**: Mostra estatísticas da análise

### Botões Disponíveis
- **Abrir Arquivo**: Carrega arquivo .als ou .txt
- **Salvar Arquivo**: Salva o código atual
- **Limpar**: Limpa editor e resultados
- **ANALISAR CÓDIGO**: Executa a análise léxica

## Funcionalidades do Analisador

### Tokens Reconhecidos
- Palavras reservadas: `als`, `cdt`, `!cdt`, `!cdt+`, `cycle`, `during`, etc.
- Tipos de variáveis: `intn`, `den`, `txt`, `bln`, `crt`
- Operadores: matemáticos, lógicos, relacionais, atribuição
- Valores: inteiros, reais, strings, booleanos
- Delimitadores: parênteses, colchetes, vírgulas
- Identificadores e comentários

### Detecção de Erros
O analisador detecta os seguintes tipos de erro:

1. **Símbolos inválidos**: Caracteres não pertencentes à linguagem (ex: `@`)
2. **Identificadores mal formados**: 
   - Começando com número (ex: `1abc`)
   - Contendo caracteres inválidos (ex: `var@`)
3. **Identificadores muito longos**: Mais de 30 caracteres
4. **Números mal formados**: (ex: `2.a3`)
5. **Números muito longos**: Mais de 15 dígitos
6. **Strings não fechadas**: (ex: `"hello world`)
7. **Caracteres não reconhecidos**

### Formato de Saída
```
Linha: xx - Coluna: xx - Token: <TipoToken, Lexema>
```

Exemplo:
```
Linha: 1 - Coluna: 1 - Token: <als, als>
Linha: 3 - Coluna: 1 - Token: <tipo_var, intn>
```

## Exemplos de Código ALAIAS

### Exemplo Básico
```alaias
als

intn idade -- Variável idade
idade <= 20

cdt [ idade ge 18 ]
    wrt "Maior de idade"
!cdt
    wrt "Menor de idade"
```

### Exemplo com Estrutura de Repetição
```alaias
als

intn i

repeat i in 5
    wrt "Executando i vezes"
brkln
```

### Exemplo com Erros (Para Teste)
```alaias
als

intn 1abc -- Identificador mal formado
txt nome @ -- Símbolo inválido
intn numero <= 2.a3 -- Número mal formado
wrt "string não fechada
```

## Solução de Problemas

### Erro: "Python não é reconhecido"
1. Verifique se Python está instalado
2. Adicione Python ao PATH do sistema
3. Reinicie o prompt de comando

### Erro: "tkinter não encontrado"
- No Windows: Reinstalar Python marcando "tcl/tk and IDLE"
- No Linux: `sudo apt install python3-tk`

### Interface não abre
1. Verifique se está executando `python analisador.py` (sem --console)
2. Verifique se tkinter está funcionando: `python -c "import tkinter; tkinter.Tk()"`

## Comandos Resumidos

```cmd
# Navegar para o projeto
cd ".\Analisador_lexico_Alaias"

# Executar interface gráfica
python analisador.py

# Executar em modo console
python analisador.py --console
```

## Recursos da Interface

- **Syntax highlighting**: Código colorido para melhor visualização
- **Abas organizadas**: Separação clara entre tokens, erros e estatísticas
- **Contadores**: Estatísticas em tempo real da análise
- **Status bar**: Feedback visual do estado da análise
- **Gerenciamento de arquivos**: Abrir/salvar arquivos .als
- **Exemplo integrado**: Código de exemplo carregado automaticamente

## Estatísticas Fornecidas

- Total de tokens encontrados
- Número de tokens válidos
- Número de erros
- Taxa de sucesso da análise
- Distribuição por tipo de token
- Contagem detalhada de cada tipo

---
