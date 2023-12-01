
# ---------------------------------------------------------------------------- #
#                               Análise Sintática                              #
# ---------------------------------------------------------------------------- #

import ply.yacc as yacc

from c_min_min_lex import tokens

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


def p_exprs_var(p):
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
    expr : OUT ABRE_PARENTESES ASPAS TEXTO ASPAS FECHA_PARENTESES
    '''
    if len(p) == 7:
        p[0] = f'printf("{p[4]}\\n")'


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

def p_expr_operacoesMat(p):
    '''
    expr : expr SOMA expr
         | expr SUBTRACAO expr
         | expr MULTIPLICACAO expr
         | expr DIVISAO expr
         | expr RESTO_DIVISAO expr
         | expr POTENCIACAO expr
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


# def p_expr_relationals(p):
#     '''
#     expr : expr EQUALS expr
#          | expr NOT_EQUALS expr
#          | expr GREATER expr
#          | expr SMALLER expr
#          | expr GREATER_EQUALS expr
#          | expr SMALLER_EQUALS expr
#     '''
#     match p[2]:
#         case '==':
#             p[0] = f"{p[1]} == {p[3]}"
#         case '!=':
#             p[0] = f"{p[1]} != {p[3]}"
#         case '>':
#             p[0] = f"{p[1]} > {p[3]}"
#         case '<':
#             p[0] = f"{p[1]} < {p[3]}"
#         case '>=':
#             p[0] = f"{p[1]} >= {p[3]}"
#         case '<=':
#             p[0] = f"{p[1]} <= {p[3]}"


# def p_expr_logicals(p):
#     '''
#     expr : expr AND expr
#          | expr OR expr
#          | NOT expr
#     '''

#     if p[1] == '!':
#         p[0] = f"!{p[2]}"

#     match p[2]:
#         case '&&':
#             p[0] = f"{p[1]} && {p[3]}"
#         case '||':
#             p[0] = f"{p[1]} || {p[3]}"


# def p_cond_if_only(p):
#     '''
#     expr : IF PAR_START exprs PAR_END BLOCK_START exprs BLOCK_END
#     '''
#     p[0] = f"if({p[3]}){{ \n {p[6]} \n }} "


# def p_cond_if_else(p):
#     '''
#     expr : IF PAR_START exprs PAR_END BLOCK_START exprs BLOCK_END ELSE BLOCK_START exprs BLOCK_END
#     '''
#     p[0] = f"if({p[3]}){{ \n {p[6]} \n }} else {{ \n {p[10]} }}"


# def p_while(p):
#     '''
#     expr : WHILE PAR_START exprs PAR_END BLOCK_START exprs BLOCK_END
#     '''
#     p[0] = f"while({p[3]}){{ \n {p[6]} \n }}"


# def p_exprs_for_no_semicolon(p):
#     '''
#     exprsfor : expr 
#     '''
#     p[0] = p[1]


# def p_exprs_for_no_breakline(p):
#     '''
#         exprsfor :  expr SEMICOLON exprsfor
#     '''
#     p[0] = p[1] + f"; " + p[3]


# def p_for(p):
#     '''
#     expr : FOR PAR_START exprsfor PAR_END BLOCK_START exprs BLOCK_END
#     '''
#     p[0] = f"for({p[3]}){{ \n {p[6]}  }}"


def p_expr_term(p):
    'expr : term'
    p[0] = p[1]


def p_term_char(p):
    'term : LETRA'
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


# def p_term_par_expr(p):
#     'term : PAR_START expr PAR_END'
#     p[0] = f'({p[2]})'


def p_error(t):
    if t is not None:
        print("Syntax error at '%s'" % t.value)


parser = yacc.yacc()

print('\n----- fim codigo -----\n')

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

# TESTE 5 -> Operacoes Matematicas Simples
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
    out(resultado1)
    out(resultado2)
    out(resultado3)
    out(resultado4)
    out(resultado5)
    ;
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

result = parser.parse(data5)
