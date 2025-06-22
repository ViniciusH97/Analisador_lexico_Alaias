import re
from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Tuple

class TokenType(Enum):
    # Palavras reservadas
    INICIO = "als"
    TIPO_VAR = "tipo_var"
    VAR = "var"
    COND_SE = "cdt"
    COND_SENAO = "!cdt"
    COND_SENAOSE = "!cdt+"
    REP_PARA = "cycle"
    REP_ENQUANTO = "during"
    REP_RANGE = "repeat"
    WRT = "wrt"
    FUNCTION = "function"
    NOME_FUNCAO = "funcao"
    PULAR_LINHA = "brkln"
    
    # Operadores
    OPER_MATEMATICO = "oper_matematico"
    OPER_ATRIB = "op_atrib"
    OPER_LOGICO = "oper_logico"
    OP_REL = "op_rel"
    
    # Valores
    VALOR_LOGICO = "valor_logico"
    VALOR_TEXTO = "valor_texto"
    VALOR_INTEIRO = "valor_inteiro"
    VALOR_REAL = "valor_real"
    
    # Delimitadores
    ABRE_PARENT = "abre_parent"
    FECHA_PARENT = "fecha_parent"
    ABRE_COLCHETES = "abre_colchetes"
    FECHA_COLCHETES = "fecha_colchetes"
    VIRGULA = "virgula"
    
    # Outros
    COMENTARIO = "comentario"
    IDENTIFICADOR = "identificador"
    WHITESPACE = "whitespace"
    NEWLINE = "newline"
    EOF = "eof"
    ERRO = "erro"

@dataclass
class Token:
    tipo: TokenType
    lexema: str
    linha: int
    coluna: int
    descricao: str = ""

class AnalisadorLexico:
    def __init__(self):
        # Definindo os padrões de tokens com base na tabela fornecida
        self.token_patterns = [
            # Comentários (deve vir primeiro para evitar conflitos)
            (TokenType.COMENTARIO, r'--.*', "Comentário"),
              # Palavras reservadas (ordem específica para evitar conflitos)
            (TokenType.INICIO, r'\bals\b', "Palavra reservada para início"),
            (TokenType.COND_SENAOSE, r'!cdt\+', "Palavra reservada para senãose"),
            (TokenType.COND_SENAO, r'!cdt(?!\+)', "Palavra reservada para senão"),
            (TokenType.COND_SE, r'\bcdt\b', "Palavra reservada para se"),
            (TokenType.REP_PARA, r'\bcycle\b', "Palavra reservada para estrutura de repetição para"),
            (TokenType.REP_ENQUANTO, r'\bduring\b', "Palavra reservada para estrutura de repetição enquanto"),
            (TokenType.REP_RANGE, r'\brepeat\b', "Palavra reservada para repetição com contador fixo"),
            (TokenType.WRT, r'\bwrt\b', "Palavra reservada para saída"),
            (TokenType.FUNCTION, r'\bfunction\b', "Palavra reservada para criação de funções"),
            (TokenType.PULAR_LINHA, r'\bbrkln\b', "Palavra reservada para quebra de linha"),
            
            # Tipos de variáveis
            (TokenType.TIPO_VAR, r'\b(intn|den|txt|bln|crt)\b', "Tipos de variáveis"),
            
            # Declaração de variável
            (TokenType.VAR, r'\bvar\b', "Palavra reservada para declaração de variável"),
            
            # Valores lógicos
            (TokenType.VALOR_LOGICO, r'\b(valid|invalid)\b', "Valor booleano"),
            
            # Operadores relacionais
            (TokenType.OP_REL, r'\b(gt|eq|ne|lt|ge|le)\b', "Operadores relacionais"),
            
            # Operadores lógicos
            (TokenType.OPER_LOGICO, r'\b(and|or)\b', "Operadores lógicos"),
            
            # Operador de atribuição
            (TokenType.OPER_ATRIB, r'<=', "Operador de atribuição"),
            
            # Operadores matemáticos
            (TokenType.OPER_MATEMATICO, r'[+\-*/]', "Operadores matemáticos"),
            
            # Valores numéricos (reais devem vir antes dos inteiros)
            (TokenType.VALOR_REAL, r'\b\d+\.\d+\b', "Valor real"),
            (TokenType.VALOR_INTEIRO, r'\b\d+\b', "Valor inteiro"),
            
            # Strings (valores de texto)
            (TokenType.VALOR_TEXTO, r'"[^"]*"', "Valor de texto"),
            
            # Delimitadores
            (TokenType.ABRE_PARENT, r'\(', "Abertura de parênteses"),
            (TokenType.FECHA_PARENT, r'\)', "Fechamento de parênteses"),
            (TokenType.ABRE_COLCHETES, r'\[', "Abertura de colchetes"),
            (TokenType.FECHA_COLCHETES, r'\]', "Fechamento de colchetes"),
            (TokenType.VIRGULA, r',', "Vírgula"),
            
            # Identificadores (nomes de funções e variáveis)
            (TokenType.NOME_FUNCAO, r'\bfuncao\s+([a-zA-Z][a-zA-Z0-9]*)', "Declaração de função"),
            (TokenType.IDENTIFICADOR, r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', "Identificador"),
            
            # Whitespace e quebras de linha
            (TokenType.NEWLINE, r'\n', "Quebra de linha"),
            (TokenType.WHITESPACE, r'[ \t]+', "Espaço em branco"),
        ]
        
        # Compilar os padrões regex
        self.compiled_patterns = [
            (token_type, re.compile(pattern), desc) 
            for token_type, pattern, desc in self.token_patterns
        ]
    
    def analisar(self, codigo: str) -> List[Token]:
        """
        Analisa o código fonte e retorna uma lista de tokens.
        """
        tokens = []
        linhas = codigo.split('\n')
        
        for num_linha, linha in enumerate(linhas, 1):
            coluna = 0
            
            while coluna < len(linha):
                token_encontrado = False
                
                # Tenta fazer match com cada padrão
                for token_type, pattern, desc in self.compiled_patterns:
                    match = pattern.match(linha, coluna)
                    
                    if match:
                        lexema = match.group(0)
                        
                        # Pula whitespace (mas não quebras de linha)
                        if token_type != TokenType.WHITESPACE:
                            token = Token(
                                tipo=token_type,
                                lexema=lexema,
                                linha=num_linha,
                                coluna=coluna + 1,
                                descricao=desc
                            )
                            tokens.append(token)
                        
                        coluna = match.end()
                        token_encontrado = True
                        break
                
                if not token_encontrado:
                    # Caractere não reconhecido
                    token = Token(
                        tipo=TokenType.ERRO,
                        lexema=linha[coluna],
                        linha=num_linha,
                        coluna=coluna + 1,
                        descricao=f"Caractere não reconhecido: '{linha[coluna]}'"
                    )
                    tokens.append(token)
                    coluna += 1
        
        # Adiciona token EOF
        tokens.append(Token(
            tipo=TokenType.EOF,
            lexema="",
            linha=len(linhas) + 1,
            coluna=1,
            descricao="Fim do arquivo"
        ))
        
        return tokens
    
    def imprimir_tokens(self, tokens: List[Token]) -> None:
        """
        Imprime os tokens de forma formatada.
        """
        print(f"{'Token':<20} {'Lexema':<15} {'Linha':<6} {'Coluna':<7} {'Descrição'}")
        print("-" * 80)
        
        for token in tokens:
            if token.tipo != TokenType.EOF:
                print(f"{token.tipo.value:<20} {token.lexema:<15} {token.linha:<6} {token.coluna:<7} {token.descricao}")
    
    def analisar_arquivo(self, caminho_arquivo: str) -> List[Token]:
        """
        Analisa um arquivo e retorna os tokens.
        """
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                codigo = arquivo.read()
            return self.analisar(codigo)
        except FileNotFoundError:
            print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
            return []
        except Exception as e:
            print(f"Erro ao ler arquivo: {e}")
            return []

def main():
    """
    Função principal para testar o analisador léxico.
    """
    analisador = AnalisadorLexico()
    
    # Exemplo 1 do enunciado
    exemplo1 = """als

intn idade -- Variável idade
idade <= 20

cdt [ idade ge 18 ]
    wrt "Maior de idade"
!cdt
    wrt "Menor de idade"

wrt "Sua idade é: idade"
"""
    
    # Exemplo 2 do enunciado
    exemplo2 = """als

intn i

repeat i in 5
    wrt "Executando i vezes"
brkln
"""
    
    # Exemplo 3 do enunciado
    exemplo3 = """als
wrt "Hello, World"
"""
    
    print("=== ANALISADOR LÉXICO - LINGUAGEM ALAIAS ===\n")
    
    # Testa o exemplo 1
    print("EXEMPLO 1:")
    print(exemplo1)
    tokens1 = analisador.analisar(exemplo1)
    analisador.imprimir_tokens(tokens1)
    print("\n" + "="*80 + "\n")
    
    # Testa o exemplo 2
    print("EXEMPLO 2:")
    print(exemplo2)
    tokens2 = analisador.analisar(exemplo2)
    analisador.imprimir_tokens(tokens2)
    print("\n" + "="*80 + "\n")
    
    # Testa o exemplo 3
    print("EXEMPLO 3:")
    print(exemplo3)
    tokens3 = analisador.analisar(exemplo3)
    analisador.imprimir_tokens(tokens3)
    
    # Opção para analisar arquivo
    print("\n" + "="*80)
    print("Para analisar um arquivo, use:")
    print("analisador = AnalisadorLexico()")
    print("tokens = analisador.analisar_arquivo('caminho_do_arquivo.als')")
    print("analisador.imprimir_tokens(tokens)")

if __name__ == "__main__":
    main()