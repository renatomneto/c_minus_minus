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
    'ASPAS',
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
t_EQUALS = r'=='
t_DIF = r'!='
t_BIGGER = r'>'
t_SMALLER = r'<'
t_BEQ = r'>='
t_SEQ = r'<='
t_TRUE = r'\btrue\b'
t_FALSE = r'\bfalse\b'
t_CHAR = r'\bCHAR\b'
t_INT = r'\bINT\b'
t_REAL = r'\bREAL\b'
t_BOOL = r'\bBOOL\b'
t_LETRA = r"'\w'"
# t_PALAVRA = r'[a-zA-Z][a-zA-Z_-]+'
t_DIGITO = r'[0-9]'
t_ASPAS = r'\"'
t_NUMERO_INTEIRO = t_SUBTRACAO + r'*' + t_DIGITO + r'+'
t_TIPO = t_BOOL + r'|' + t_CHAR + r'|' + t_INT + r'|' + t_REAL
t_NUMERO_REAL = t_NUMERO_INTEIRO + t_SEPARADOR + t_DIGITO + r'+'
# t_VARIAVEL = t_TIPO + r' ((' + t_PALAVRA + r'|' + t_LETRA + r')(' + t_DIGITO + r'|' + t_LETRA + r')*'

def t_VARIAVEL(t):
    r'[a-zA-Z]+([a-zA-Z_-]|[0-9])*' 
    t.type = reserved.get(t.value, 'VARIAVEL')

    return t

def t_TEXTO(t):
    r'[a-zA-Z]+(([a-zA-Z_-]|[0-9])|[ ])+' 
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
    ;
'''
# TESTE 2 -> Saida com Strings
data2 = '''
main:
    out("Hello World")
    out("Com duas linhas")
    ;
'''

data3 = '''
main:
    INT var1 = 1
    REAL var2 = 1.0
    BOOL var3 = true
    BOOL var4 = false
    CHAR var5 = 'a'
    out(var1)
    out(var2)
    out(var3)
    out(var4)
    out(var5)
    ;
'''

# entrada de teste para attr com operacao aritmetica
data4 = '''
main {
    let variavel_int: int;
    variavel_int = 3 + 4;
    output(variavel_int);
    let variavel_int2: int;
    variavel_int2 = (variavel_int * 4) + 3;
    output(variavel_int2);
}
'''

# entrada de teste para cond logical e relacional verdadeiro
data5 = '''
main {
    let variavel_int: int;
    variavel_int = 3 + 4;
    let variavel_char: char;
    variavel_char = '3';
    if(variavel_int == 7 && variavel_char == '3'){
        variavel_int = variavel_int - 7;
        output(variavel_int);
    }
}
'''

# entrada de teste para cond logical e relacional falso com else
data6 = '''
main {
    let variavel_int: int;
    variavel_int = 3 + 4;
    let variavel_char: char;
    variavel_char = '3';
    if(variavel_int == 7 && variavel_char == '2'){
        variavel_int = variavel_int - 7;
        output(variavel_int);
    }else{
        output(variavel_char);
    }
}
'''

# entrada de teste para while
data7 = '''
main {
    let variavel_int: int;
    variavel_int = 3;
    while(variavel_int > 0 ){
        output(variavel_int);
        variavel_int = variavel_int - 1;
    }
}
'''

# entrada de teste para for
data8 = '''
main {
    let variavel_int: int;
    variavel_int = 3;
    for(variavel_int = 3; variavel_int > 0; variavel_int = variavel_int - 1 ) {
        output(variavel_int);
        variavel_int = variavel_int + 1;
    }
}
'''

lexer.input(data3)

while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
