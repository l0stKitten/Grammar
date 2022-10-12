# INTEGRANTES:
#
# - Johanna Garate Cardenas
# - Daria Lopez Franco
# - Kristhyan A. Kurt Lazarte Zubia
#

# Ver 2.0 - Se han agregado nuevas palabras clave, se están ignorando los comentarios

import ply.lex as lex

# r'atring' -> r significa que la cadena es tradada sin caracteres de escape,
# es decir r'\n' seria un \ seguido de n (no se interpretaria como salto de linea)

reserved = {
    'algoritmo': 'MAIN',
    'funcion': 'FUNCTION',
    'definir': 'DEFINE',
    'como': 'AS',
    'entero': 'INT',
    'real': 'FLOAT',
    'caracter': 'CHAR',
    'cadena': 'STRING',
    'logico': 'BOOL_TYPE',
    'array': 'DIMENSION',
    'imprimir': 'PRINT',
    'leer': 'SCAN',
    'mientras': 'WHILE',
    'para': 'FOR',
    'hasta': 'UNTIL',
    'conpaso': 'SALTO',
    'si': 'IF',
    'entonces': 'THEN',
    'sino': 'ELSE',
    'sinosi': "ELSEIF",
    'segun': 'SWITCH',
    'predeterminado': 'DEFAULT_SWITCH',
    'y': 'AND',
    'o': 'OR',
    'no': 'NEGACION',
    'mod': 'MOD',
    'dimension': 'ARRAY'
}

# List of token names.   This is always required
tokens = [
    'COMENTARIO', 'COMENTARIO_LARGO', 'DIGITO', 'DOUBLE',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'INI_PARENTESIS', 'FIN_PARENTESIS',
    'INI_LLAVE', 'FIN_LLAVE', 'INI_CORCHETE', 'FIN_CORCHETE', 'PUNTO_COMA',
    'COMA', 'DOS_PUNTOS', 'COMILLAS_DOBLE', 'COMILLAS_SIMPLE', 'IGUAL',
    'NO_IGUAL',
    'IGUAL_DOBLE', 'RETURN', 'MAYOR', 'MENOR', 'MAYOR_IGUAL', 'MENOR_IGUAL',
    'POTENCIA', 'id', 'BOOL', 'CADENA', 'CARACTER'
]  # + list(reserved.values())

tokens += reserved.values()
# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
#t_COMENTARIO = r'\/\/.+'
#t_COMENTARIO_LARGO = r'\/\*.+\*\/'
t_INI_PARENTESIS = r'\('
t_FIN_PARENTESIS = r'\)'
t_INI_LLAVE = r'\{'
t_FIN_LLAVE = r'\}'
t_INI_CORCHETE = r'\['
t_FIN_CORCHETE = r'\]'
t_PUNTO_COMA = r'\;'
t_COMA = r'\,'
t_DOS_PUNTOS = r'\:'
t_COMILLAS_DOBLE = r'\"'
t_COMILLAS_SIMPLE = r'\''
t_IGUAL = r'\='
t_NO_IGUAL = r'\!\='
t_IGUAL_DOBLE = r'\=\= '
t_RETURN = r'\<\-'
t_MAYOR = r'\>'
t_MENOR = r'\<'
t_MAYOR_IGUAL = r'\>\='
t_MENOR_IGUAL = r'\<\='
t_POTENCIA = r'\^'

# A regular expression rule with some action code


def t_COMMENT(t):
    r'\/\/.*'
    pass


def t_COMENTARIO_LARGO(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    pass


def t_DIGITO(t):
    r'\d+'
    t.value = int(t.value)  # guardamos el valor del lexema
    #print("se reconocio el numero")
    return t


def t_DOUBLE(t):
    '[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'
    return t


#Identificamos los id
def t_id(t):
    r'(\_ | [a-zA-Z])+ ( \_ | [0-9a-zA-Z] )*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t


# Booleanos
def t_BOOL(t):
    r'verdadero|falso'
    return t


def t_CADENA(t):
    r'\".*\"'
    return t


def t_CARACTER(t):
    r"\'.*\'"
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''

funcion variableDevolver <- miFuncion1 ( a, b ){
	variableDevolver = a + b;
}

algoritmo mi_Algoritmo{
	definir a, b, c como entero;
	//definir z como caracter entero logico real
	a = 3;
	b = 5;
	c = a + b;
	imprimir "El valor de c es: ", c;
	imprimir "Usando la funcion: ", miFuncion1(a,b);
	leer c;
	imprimir "El valor leido en c es: ", c;
	
	definir i como entero;
	i = 0;
	imprimir "Bucle mientras";
	mientras i < 3 {
		imprimir i;
		i = i + 1;
	}
	
	imprimir "Bucle para";
	para j = 0 hasta 40 conpaso 10 {
		Imprimir j;
	}
  // Estructura if elif y else
  
	si 1 == 1 entonces {
		imprimir "Verdadero";
    }
	sinosi 2 == 'H' entonces {
		imprimir "Imposible";
	}
  sino{
    imprimir "Else";
  }
	
	segun c {
		0:
			imprimir "Cero";
		1:
			imprimir "Uno";
		2:
			imprimir "Dos";
		predeterminado:
			imprimir "Es otro numero";
	}
	
	dimension unArreglo[2];
	unArreglo[0] = 20;
	unArreglo[1] = 50;
	
	imprimir (1 > 0) y (4 == 4)
	imprimir (3 < 9) o (7 == 17)
	
}

'''

data1 = '''

algoritmo mi_Algoritmo{
	definir a, b, c como entero;
	//definir z como caracter entero logico real
	a = 3;
	b = 5;
	c = a + b;
	imprimir "El valor de c es: ", c;
	leer c;
	imprimir "El valor leido en c es: ", c;	
}

'''

data2 = '''

algoritmo mi_Algoritmo{

	definir i como entero;
	i = 0;
	imprimir "Bucle mientras";
	mientras i < 3 {
		imprimir i;
		i = i + 1;
	}
	
	imprimir "Bucle para";
	para j = 0 hasta 40 conpaso 10 {
		Imprimir j;
	}
  // Estructura if elif y else
  
	si 1 == 1 entonces {
		imprimir "Verdadero";
    }
	sinosi 2 == 'H' entonces {
		imprimir "Imposible";
	}
  sino{
    imprimir "Else";
  }	
}

'''
data3 = '''

funcion variableDevolver <- miFuncion1 ( a, b ){
	variableDevolver = a + b;
}

algoritmo mi_Algoritmo{
	definir unArreglo como dimension;
	unArreglo[2];
	imprimir "Hola Mundo";
    miFuncion1(c);
}
'''

# Give the lexer some input
lexer.input(data2)

data_tokens = []
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    #print(tok)
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
    my_dict = {'type':tok.type.lower(), 'lexeme':tok.value, 'line':tok.lineno}
    data_tokens.append(my_dict)

my_dict2 ={'type':'$', 'lexeme':'$', 'line':0}
data_tokens.append(my_dict2)

print(data_tokens)
