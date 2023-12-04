# ---------------------------------------------------------------------------- #
#                                Análise Léxica                                #
# ---------------------------------------------------------------------------- #

import ply.lex as lex

# TOKENS: PALAVRAS RESERVADAS
reserved = {
    'main': 'MAIN',
    'REAL': 'REAL',
    'INT': 'INT',
    'CHAR': 'CHAR',
    'BOOL': 'BOOL',
    'while': 'WHILE',
    'for': 'FOR',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'smaller': 'SMALLER',
    'bigger': 'BIGGER',
    'beq': 'BEQ',
    'seq': 'SEQ',
    'equals': 'EQUALS',
    'dif': 'DIF',
    'if': 'IF',
    'else': 'ELSE',
    'in': 'IN',
    'out': 'OUT',
    'true': 'TRUE',
    'false': 'FALSE'
}

# TOKENS
tokens = [
    # 'MAIN',
    'OPERACOES',
    'CONDICAO',
    'VARIAVEL',
    'CONDICIONAL1',
    'NUMERO_REAL',
    'NUMERO_INTEIRO',
    'PALAVRA',
    'COMPARACAO',
    'OPERACAO_MATEMATICA1',
    'OPERACAO_MATEMATICA2',
    'OPERACAO_MATEMATICA3',
    'ENQUANTO_BLOCO',
    'PARA_BLOCO',
    'BLOCO',
    'ENTRADA',
    'INICIO_BLOCO',
    'FIM_BLOCO',
    'DIGITO',
    'LETRA',
    'SEPARADOR',
    'VIRGULA',
    'ATRIBUICAO',
    'SOMA',
    'SUBTRACAO',
    'DIVISAO',
    'MULTIPLICACAO',
    'RESTO_DIVISAO',
    'POTENCIACAO',
    'ABRE_PARENTESES',
    'FECHA_PARENTESES',
    'TIPO', 
    'TEXTO'
] + list(reserved.values()) # adiciona os tokens das palavras reservadas

# regex para os tokens
t_MAIN = r'\bmain\b'
t_FIM_BLOCO = r';'
t_SOMA = r'\+'
t_SUBTRACAO = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'
t_RESTO_DIVISAO = r'%'
t_POTENCIACAO = r'\^'
t_ATRIBUICAO = r'='
t_INICIO_BLOCO = r':'
t_SEPARADOR = r'\.'
t_ABRE_PARENTESES = r'\('
t_FECHA_PARENTESES = r'\)'
t_VIRGULA = r','
t_AND = r'\band\b'
t_OR = r'\bor\b'
t_NOT = r'\bnot\b'
t_DIF = r'\bdif\b'
t_TRUE = r'\btrue\b'
t_FALSE = r'\bfalse\b'
t_CHAR = r'\bCHAR\b'
t_INT = r'\bINT\b'
t_REAL = r'\bREAL\b'
t_BOOL = r'\bBOOL\b'
t_LETRA = r"'\w'"
# t_PALAVRA = r'[a-zA-Z][a-zA-Z_-]+'
t_DIGITO = r'[0-9]'
t_NUMERO_INTEIRO = t_DIGITO + r'+'
t_TIPO = t_BOOL + r'|' + t_CHAR + r'|' + t_INT + r'|' + t_REAL
t_NUMERO_REAL = t_NUMERO_INTEIRO + t_SEPARADOR + t_DIGITO + r'+'


def t_VARIAVEL(t):
    r'[a-zA-Z]+([a-zA-Z_]|[0-9])*' 
    t.type = reserved.get(t.value, 'VARIAVEL')

    return t

def t_TEXTO(t):
    r'\"([a-zA-Z]+[ ])+(([a-zA-Z_-]|[0-9])|\.|[ ])*\"' 
    t.type = reserved.get(t.value, 'TEXTO')

    return t

t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# constroi o analisador lexico
lexer = lex.lex()

# TESTE 1 -> Declarando varaiveis
data1 = '''
main:
    INT var1 = 1
    REAL var2 = 1.0
    BOOL var3 = true
    BOOL var4 = false
    CHAR var5 = 'a'
    INT var6 = -10
    REAL var7 = -4.56
;
'''
# TESTE 2 -> Saida com Strings
data2 = '''
main:
    out("Hello World")
    out("Com duas linhas")
;
'''
# TESTE 3 -> Saida com Variáveis
data3 = '''
main:
    INT var1 = 1
    REAL var2 = 1.0
    BOOL var3 = true
    BOOL var4 = false
    CHAR var5 = 'a'
    out("Texto antes das variaveis")
    out(var1)
    out(var2)
    out(var3)
    out(var4)
    out(var5)
;
'''

# TESTE 4 -> Entrada de dados
data4 = '''
main:
    INT var1
    REAL var2
    CHAR var3
    in(var1)
    in(var2)
    in(var3)
;
'''

# TESTE 5 -> Operacoes Matematicas1 
# OBS: potenciacao não pode ser feita como
#   REAL resultado4 = 5.0^4.0
# é necessário separar como no exemplo abaixo
data5 = '''
main:
    INT resultado1 = 5+4
    REAL resultado2 = 5.0-4.0
    REAL resultado3 = 5.0*4.0
    REAL resultado4 = 5.0/4.0
    REAL resultado5 
    resultado5 = 5.0^4.0
    INT resultado6 = 4%3
    out(resultado1)
    out(resultado2)
    out(resultado3)
    out(resultado4)
    out(resultado5)
    out(resultado6)
;
'''

# TESTE 6 -> Operacoes Matematicas1 com variáveis
data6 = '''
main:
    INT var1 = 2
    INT var2 = 3
    INT resultado1
    resultado1 = var1+var2
    out(resultado1)
    resultado1 = var1-var2
    out(resultado1)
    resultado1 = var2 % var1
    out(resultado1)
    REAL resultado2
    resultado2 = var1*var2
    out(resultado2)
    resultado2 = var1/var2
    out(resultado2)
    resultado2 = var1^var2
    out(resultado2)
;
'''

# TESTE 7 -> Operacoes Matematicas2 e 3 
data7 = '''
main:
    INT var1 = 1
    INT var2 = 2
    INT resultado
    resultado = (var1+var2)
    out(resultado)
    INT resultado2
    resultado2 = (var1+var2)*(var1+var2)
    out(resultado2)
;
'''

# TESTE 8 -> While
data8 = '''
main:
    INT var = 0
    while(var dif 2):
        out(var)
        var = var + 1
    ;
;
'''

# TESTE 9 -> for
data9 = '''
main:
    INT i = 0
    for(i, i smaller 10, i = i + 1):
        out(i)
    ;
;
'''

# TESTE 10 -> if / else simples
data10 = '''
main:
    INT var = 20
    if(var smaller 10):
        out("var menor que 10")
    else
        out("var maior que 10")
    ;
;
'''

# TESTE 11 -> if com 2 condiçoes / else 
data11 = '''
main:
    INT var = 15
    if((var bigger 10) and (var smaller 20)):
        out("Maior que 10 e menor que 20")
    ; 

;
'''
# if((var smaller 10) or (var bigger 20)):
#         out("Pode ser menor que 10 ou maior que 20")
#     ;
lexer.input(data11)

while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
