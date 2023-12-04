
# ---------------------------------------------------------------------------- #
#                               Análise Sintática                              #
# ---------------------------------------------------------------------------- #

import ply.yacc as yacc

from c_min_min_lex import tokens, opcao

myVariables = []
# boolStack = []


def hasInArray(name):
    index = 0
    for v in myVariables:
        if v['name'] == name:
            return index
        index += 1

    return -1


precedence = (
    ('left', 'SOMA', 'SUBTRACAO'),
    ('left', 'MULTIPLICACAO', 'DIVISAO'),
    ('left', 'AND', 'OR'),
    ('right', 'NOT')
)


def p_main(p):
    'programa : MAIN INICIO_BLOCO exprs FIM_BLOCO'
    f = open("codigo_gerado.c", "w")
    f.write(f"#include <stdio.h>\n#include <stdbool.h>\n#include <math.h>\nint main(){{\n   {p[3]}\n   return 0;\n}}")
    f.close()


def p_exprs_void(p):
    '''
    exprs :  
    '''
    p[0] = ""

def p_exprs_newLine(p):
    '''
    exprs : expr 
    '''
    p[0] = p[1] + f";\n   "


def p_expr_varias(p):
    '''
        exprs : exprs expr  
    '''
    p[0] = p[1] + p[2] + f";\n   "


# =====================================================================
# FUNCOES PARA OUT (SAIDA)
# =====================================================================

def p_out_string(p):
    '''
    expr : OUT ABRE_PARENTESES TEXTO FECHA_PARENTESES
    '''
    # para diferenciar TEXTO e STRING e as saidas pularem linha sem
    # corretamente ao transfomar o código em C
    str = p[3]
    str = str[: len(str)-1] # remove as " finais do TEXTO para inserir o \n abaixo
    p[3] = str
    p[0] = f'printf({p[3]}\\n")'


def p_output_var(p):
    '''
    expr : OUT ABRE_PARENTESES VARIAVEL FECHA_PARENTESES
    '''
    if (hasInArray(p[3]) != -1):
        if (myVariables[hasInArray(p[3])]['type'] == 'int'):
            p[0] = f'printf("%d\\n",{p[3]})'
        elif (myVariables[hasInArray(p[3])]['type'] == 'float'):
            p[0] = f'printf("%f\\n",{p[3]})'
        elif (myVariables[hasInArray(p[3])]['type'] == 'char'):
            p[0] = f'printf("%c\\n",{p[3]})'
        if (myVariables[hasInArray(p[3])]['type'] == 'bool'):
            p[0] = f'printf("%s\\n", {p[3]} ? "true" : "false")' 


def p_input_var(p):
    '''
    expr : IN ABRE_PARENTESES VARIAVEL FECHA_PARENTESES
    '''
    if (hasInArray(p[3]) != -1):
        if (myVariables[hasInArray(p[3])]['type'] == 'int'):
            p[0] = f'scanf("%d", &{p[3]})'
        elif (myVariables[hasInArray(p[3])]['type'] == 'float'):
            p[0] = f'scanf("%f", &{p[3]})'
        if (myVariables[hasInArray(p[3])]['type'] == 'char'):
            p[0] = f'scanf(" %c", &{p[3]})'


# =====================================================================
# FUNCOES PARA INT
# =====================================================================

def p_declaracao_int(p):
    '''
    expr : INT VARIAVEL
    '''
    myVariables.append(
        {'name': p[2], 'type': 'int', 'value': None})
    p[0] = f'int {p[2]}'


def p_atribuicao_int(p):
    '''
    expr : INT VARIAVEL ATRIBUICAO NUMERO_INTEIRO
    '''
    myVariables.append(
        {'name': p[2], 'type': 'int', 'value': None})
    if hasInArray(p[2]) != -1:
        myVariables[hasInArray(p[2])]['value'] = p[4]
    
    #linha abaixo vai escrever a declaracao em C 
    #onde {p[2]} é o nome da variavel e {p[4]} o valor
    p[0] = f'int {p[2]} = {p[4]}' 

def p_atribuicao_int_negativo(p):
    '''
    expr : INT VARIAVEL ATRIBUICAO SUBTRACAO NUMERO_INTEIRO
    '''
    myVariables.append(
        {'name': p[2], 'type': 'int', 'value': None})
    if hasInArray(p[2]) != -1:
        myVariables[hasInArray(p[2])]['value'] = p[5]
    
    #linha abaixo vai escrever a declaracao em C 
    #onde {p[2]} é o nome da variavel e {p[4]} o valor
    p[0] = f'int {p[2]} = -{p[5]}' 


# =====================================================================
# FUNCOES PARA REAL
# =====================================================================

def p_declaracao_real(p):
    '''
    expr : REAL VARIAVEL
    '''
    myVariables.append(
        {'name': p[2], 'type': 'float', 'value': None})
    p[0] = f'float {p[2]}'


def p_atribuicao_real(p):
    '''
    expr : REAL VARIAVEL ATRIBUICAO NUMERO_REAL
    '''
    myVariables.append(
        {'name': p[2], 'type': 'float', 'value': None})
    if hasInArray(p[2]) != -1:
        myVariables[hasInArray(p[2])]['value'] = p[4]
    
    #linha abaixo vai escrever a declaracao em C 
    #onde {p[2]} é o nome da variavel e {p[4]} o valor
    p[0] = f'float {p[2]} = {p[4]}' 

def p_atribuicao_real_negativo(p):
    '''
    expr : REAL VARIAVEL ATRIBUICAO SUBTRACAO NUMERO_REAL
    '''
    myVariables.append(
        {'name': p[2], 'type': 'float', 'value': None})
    if hasInArray(p[2]) != -1:
        myVariables[hasInArray(p[2])]['value'] = p[5]
    
    #linha abaixo vai escrever a declaracao em C 
    #onde {p[2]} é o nome da variavel e {p[4]} o valor
    p[0] = f'float {p[2]} = -{p[5]}' 

# =====================================================================
# FUNCOES PARA CHAR
# =====================================================================

def p_declaracao_char(p):
    '''
    expr : CHAR VARIAVEL
    '''
    myVariables.append(
        {'name': p[2], 'type': 'char', 'value': None})
    p[0] = f'char {p[2]}'


def p_atribuicao_char(p):
    '''
    expr : CHAR VARIAVEL ATRIBUICAO LETRA 
    '''
    myVariables.append(
        {'name': p[2], 'type': 'char', 'value': None})
    if hasInArray(p[2]) != -1:
        myVariables[hasInArray(p[2])]['value'] = p[4]
    
    #linha abaixo vai escrever a declaracao em C 
    #onde {p[2]} é o nome da variavel e {p[4]} o valor
    p[0] = f'char {p[2]} = {p[4]}'

# =====================================================================
# FUNCOES PARA BOOL
# =====================================================================

def p_declaracao_bool(p):
    '''
    expr : BOOL VARIAVEL
    '''
    myVariables.append(
        {'name': p[2], 'type': 'bool', 'value': None})
    p[0] = f'bool {p[2]}'


def p_atribuicao_bool_true(p):
    '''
    expr : BOOL VARIAVEL ATRIBUICAO TRUE
    '''
    myVariables.append(
        {'name': p[2], 'type': 'bool', 'value': None})
    if hasInArray(p[2]) != -1:
        myVariables[hasInArray(p[2])]['value'] = True
    
    #linha abaixo vai escrever a declaracao em C 
    #onde {p[2]} é o nome da variavel e {p[4]} o valor
    p[0] = f'bool {p[2]} = {p[4]}'

def p_atribuicao_bool_false(p):
    '''
    expr : BOOL VARIAVEL ATRIBUICAO FALSE
    '''
    myVariables.append(
        {'name': p[2], 'type': 'bool', 'value': None})
    if hasInArray(p[2]) != -1:
        myVariables[hasInArray(p[2])]['value'] = False
    
    #linha abaixo vai escrever a declaracao em C 
    #onde {p[2]} é o nome da variavel e {p[4]} o valor
    p[0] = f'bool {p[2]} = {p[4]}'

# =====================================================================
# FUNCOES PARA OPERAÇÕES MATEMÁTICAS
# =====================================================================

def p_attr(p):
    '''
    expr :  VARIAVEL ATRIBUICAO expr
    '''
    if hasInArray(p[1]) != -1:
        myVariables[hasInArray(p[1])]['value'] = p[3]
    p[0] = f'{p[1]} = {p[3]}'

def p_expr_operacoesMat1(p):
    '''
    expr : expr SOMA expr
         | expr SUBTRACAO expr
         | expr MULTIPLICACAO expr
         | expr DIVISAO expr
         | expr RESTO_DIVISAO expr
         | expr POTENCIACAO expr
         | VARIAVEL SOMA expr
         | VARIAVEL SUBTRACAO expr
         | VARIAVEL MULTIPLICACAO expr
         | VARIAVEL DIVISAO expr
         | VARIAVEL RESTO_DIVISAO expr
         | VARIAVEL POTENCIACAO expr
         | VARIAVEL SOMA VARIAVEL
         | VARIAVEL SUBTRACAO VARIAVEL
         | VARIAVEL MULTIPLICACAO VARIAVEL
         | VARIAVEL DIVISAO VARIAVEL
         | VARIAVEL RESTO_DIVISAO VARIAVEL
         | VARIAVEL POTENCIACAO VARIAVEL
         | expr SOMA VARIAVEL
         | expr SUBTRACAO VARIAVEL
         | expr MULTIPLICACAO VARIAVEL
         | expr DIVISAO VARIAVEL
         | expr RESTO_DIVISAO VARIAVEL
         | expr POTENCIACAO VARIAVEL
    '''
    match p[2]:
        case '+':
            p[0] = f"{p[1]} + {p[3]}"
        case '-':
            p[0] = f"{p[1]} - {p[3]}"
        case '*':
            p[0] = f"{p[1]} * {p[3]}"
        case '/':
            p[0] = f"{p[1]} / {p[3]}"
        case '%':
            p[0] = f"{p[1]} % {p[3]}"
        case '^':
            p[0] = f"pow({p[1]},{p[3]})"


# =====================================================================
# FUNCOES PARA OPERACOES RELACIONAIS
# =====================================================================

def p_expr_relationals(p):
    '''
    expr : expr EQUALS expr
         | expr DIF expr
         | expr BIGGER expr
         | expr SMALLER expr
         | expr BEQ expr
         | expr SEQ expr
         | VARIAVEL EQUALS expr
         | VARIAVEL DIF expr
         | VARIAVEL BIGGER expr
         | VARIAVEL SMALLER expr
         | VARIAVEL BEQ expr
         | VARIAVEL SEQ expr
    '''
    match p[2]:
        case 'equals':
            p[0] = f"{p[1]} == {p[3]}"
        case "dif":
            p[0] = f"{p[1]} != {p[3]}"
        case 'bigger':
            p[0] = f"{p[1]} > {p[3]}"
        case 'smaller':
            p[0] = f"{p[1]} < {p[3]}"
        case 'beq':
            p[0] = f"{p[1]} >= {p[3]}"
        case 'seq':
            p[0] = f"{p[1]} <= {p[3]}"


# =====================================================================
# FUNCOES PARA OPERACOES LOGICAS
# =====================================================================

def p_expr_logicals(p):
    '''
    expr : expr AND expr
         | expr OR expr
         | NOT expr
         | termcond AND termcond
         | termcond OR termcond
         | NOT termcond
    '''

    if p[1] == 'not':
        p[0] = f"!{p[2]}"

    match p[2]:
        case 'and':
            p[0] = f"{p[1]} && {p[3]}"
        case 'or':
            p[0] = f"{p[1]} || {p[3]}"


# =====================================================================
# FUNCOES PARA IF / ELSE
# =====================================================================

def p_cond_if(p):
    '''
    expr : IF ABRE_PARENTESES expr FECHA_PARENTESES INICIO_BLOCO exprs FIM_BLOCO
    '''
    p[0] = f"if({p[3]}){{ \n   {p[6]} \n   }} "


def p_cond_if_else(p):
    '''
    expr : IF ABRE_PARENTESES expr FECHA_PARENTESES INICIO_BLOCO exprs ELSE exprs FIM_BLOCO
    '''
    p[0] = f"if({p[3]}){{ \n    {p[6]} \n   }} else {{ \n     {p[8]} \n   }}"


# =====================================================================
# FUNCOES PARA WHILE
# =====================================================================

def p_while(p):
    '''
    expr : WHILE ABRE_PARENTESES expr FECHA_PARENTESES INICIO_BLOCO exprs FIM_BLOCO
    '''
    p[0] = f"while({p[3]}){{\n   {p[6]} \n   }}"


# =====================================================================
# FUNCOES PARA FOR
# =====================================================================
def p_for(p):
    '''
    expr : FOR ABRE_PARENTESES expr VIRGULA expr VIRGULA expr FECHA_PARENTESES INICIO_BLOCO exprs FIM_BLOCO
    '''
    p[0] = f"for({p[3]}; {p[5]}; {p[7]}){{ \n   {p[10]}  \n   }}"


# =====================================================================
# FUNCOES PARA TERM
# =====================================================================
def p_expr_term(p):
    'expr : term'
    p[0] = p[1]


def p_term_char(p):
    'term : LETRA'
    p[0] = p[1]

def p_term_digito(p):
    'term : DIGITO'
    p[0] = p[1]


def p_term_bool_true(p):
    'term : TRUE'
    p[0] = p[1]

def p_term_bool_false(p):
    'term : FALSE'
    p[0] = p[1]

def p_term_int(p):
    'term : NUMERO_INTEIRO'
    p[0] = p[1]


def p_term_real(p):
    'term : NUMERO_REAL'
    p[0] = p[1]

def p_term_variavel(p):
    'term : VARIAVEL'
    p[0] = p[1]

def p_term_parenteses_expr(p):
    'term : ABRE_PARENTESES expr FECHA_PARENTESES'
    p[0] = f'({p[2]})'

def p_term_parenteses_exprcond(p):
    'termcond : ABRE_PARENTESES exprs FECHA_PARENTESES'
    p[0] = f'({p[2]})'
    

def p_error(t):
    if t is not None:
        print("Syntax error at '%s'" % t.value)


parser = yacc.yacc()

print('\n----- fim codigo -----\n')


# =====================================================================
# CODIGOS EXEMPLOS 
# =====================================================================

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
    out("Digite as variaveis")
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

# # TESTE 8 -> While
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
    INT var = 10
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

# TESTE 12 -> Fibonacci
data12 = '''
main:
    INT a=0
    INT b=1
    INT entrada
    INT aux=0
    INT i=0

    out("Entar com o numero de fibonacci desejado: ")
    in(entrada)

    out(a)
    out(b)

    while(i smaller (entrada-2)):
        i = i+1
        aux = a+b
        a = b
        b = aux
        out(b)
    ;
;
'''

# TESTE 13 -> Precedence
data13 = '''
main:
    INT aa=5
    INT bb=2
    REAL pi=3.1415

    REAL res
    res = aa+bb*pi
    out(res)
    res = (aa+bb)*pi
    out(res)
    res = bb*pi+aa
    out(res)
    res = bb*(pi+aa)
    out(res)
;

'''

# Exemplo codigo alvo para a linguagem
objetivo = '''
main:
    INT num = 5
    if(num smaller 10 and num bigger 1):
        out("Hello World")
    ;  
;
'''
# result = parser.parse(data12)
match opcao:
        case 1:
            result = parser.parse(data12)
        case 2:
            result = parser.parse(data13)
