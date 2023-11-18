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
    'FECHA_PARENTESES'
] + list(reserved.values()) # adiciona os tokens das palavras reservadas

# regex para os tokens
# t_MAIN_START = r'main'
t_FIM_BLOCO = r';'
t_SUM = r'\+'
t_SUB = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_RESTO_DIVISAO = r'%'
t_ATTR = r'='
t_COLON = r':'
t_BLOCK_START = r'{'
t_BLOCK_END = r'}'
t_PAR_START = r'\('
t_PAR_END = r'\)'
t_SEPARATOR = r','
t_LIT_INT = r'-?\d+'
t_LIT_FLOAT = r'-?\d+.\d+'
t_LIT_CHAR = r"'\w'"
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_GREATER = r'>'
t_SMALLER = r'<'
t_GREATER_EQUALS = r'>='
t_SMALLER_EQUALS = r'<='
t_ASP = r'"'


def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VAR')

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

# entrada de teste para output de string comum
data0 = '''
    main {
        output("Hello");
        output("World");
    }
'''

# entrada de teste para decl attr e output de variavel inteiras
data1 = '''
main {
    let variavel_int: int;
    variavel_int = 3;
    output(variavel_int);
    const constante_int: int = 2;
    output(constante_int);
    let variavel_int2: int = 5;
    output(variavel_int2);
}
'''

# entrada de teste para decl attr e output de variavel float
data2 = '''
main {
    let variavel_float: float;
    variavel_float = 3;
    output(variavel_float);
    const constante_float: float = 2.0;
    output(constante_float);
    let variavel_float2: float;
    input(variavel_float2);
    output(variavel_float2);
}
'''

# entrada de teste para decl attr e output de variavel char
data3 = '''
main {
    let variavel_char: char;
    variavel_char = '3';
    output(variavel_char);
    const constante_char: char = 'a';
    output(constante_char);
    let variavel_char2: char;
    input(variavel_char2);
    output(variavel_char2);
}
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

lexer.input(data8)

while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
