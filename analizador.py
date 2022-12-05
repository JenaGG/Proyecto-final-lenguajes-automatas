import ply.lex as lex


#establecen el codigo que se desea analizar
program = '''
    
lenguaje = "Python"

if lenguaje == "Python":
    print("Estoy de acuerdo, Python es el mejor")
elif lenguaje == "Java":
    print("No me gusta, Java no mola")
else:
    print("Ningún otro lenguaje supera a Python")

# Salida: Estoy de acuerdo, Python es el mejor

x = 0
while x < 3:
    print(x)
    x += 1

# Salida: 0, 1, 2

for i in range(3):
    print(i)

# Salida: 0, 1, 2

for i in range(3):
    if i == 1:
        continue
    print(i)

# Salida: 0, 2

x = 0
while True:
    print(x)
    if x == 2:
        break
    x += 1

# Salida: 0, 1, 2

def funcion_suma(a, b):
    return a + b

suma = funcion_suma(3, 5)
print("La suma es", suma)

# Salida: La suma es 8

def generador():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

for i in generador():
    print(i)

# Salida: 1, 2, 3

x = "10"

valor = None
try:
    valor = int(x)
except Exception as e:
    print("Hubo un error:", e)
finally:
    print("El valor es", valor)

# Salida: El valor es 10

a = 0

def suma_uno():
    global a
    a = a + 1

suma_uno()
print(a)

# Salida: 1

def funcion_a():
    x = 10

    def funcion_b():
        nonlocal x
        x = 20
        print("funcion_b", x)

    funcion_b()
    print("funcion_a", x)


funcion_a()

# Salida:
# funcion_b 20
# funcion_a 20

with open('fichero.txt', 'r') as file:
    print(file.read())

import asyncio

async def proceso(id_proceso):
    print("Empieza proceso:", id_proceso)
    await asyncio.sleep(10)
    print("Acaba proceso:", id_proceso)

async def main():
    await asyncio.gather(proceso(1), proceso(2), proceso(3))

asyncio.run(main())

# Salida:
# Empieza proceso: 1
# Empieza proceso: 2
# Empieza proceso: 3
# Acaba proceso: 1
# Acaba proceso: 2
# Acaba proceso: 3
'''

reservadas = ['as',
              'assert',
              'async',
              'await',
              'break',
              'class',
              'continue',
              'def',
              'del',
              'elif',
              'else',
              'except',
              'false',
              'finally',
              'for',
              'from',
              'global',
              'if',
              'import',
              'in',
              'is',
              'lamdba',
              'none',
              'nonlocal',
              'pass',
              'raise',
              'return',
              'true',
              'try',
              'while',
              'with',
              'yield']

tokens = ['ID',
          'NUMBER',
          'PLUS',
          'MINUS',
          'TIMES',
          'DIVIDE',
          'ODD',
          'ASSIGN',
          'NE',
          'LT',
          'LTE',
          'GT',
          'GTE',
          'LPARENT', 
          'RPARENT',
          'COMMA',
          'SEMMICOLOM',
          'DOT',
          'UPDATE',
          'QUOTES',
          'MOD',
          'AND',
          'OR',
          'NOT',
          'DDOT'
          ]

tokens = tokens+reservadas

#se agrega en PALABRA a tokens y a continuacion se establece
#el simbolo utilizado iniciando con t_PALABRA
t_ignore = '\t '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='
t_QUOTES = r'\"' 
t_MOD = r'\%'
##Modificaciones propias
t_AND = r'\and'
t_OR = r'\or'
t_NOT = r'\not'
t_DDOT = r'\:'

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value in reservadas:
		#t.value = t.value.upper()
		#reservadas.get(t.value,'ID')
		t.type = t.value

	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    #para comentarios con #
    r'\#.*'
    #para comentarios con //
    #r'\//.*'
    pass

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
	print("caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)



analizador = lex.lex()

analizador.input(program)

while True:
	tok = analizador.token()
	if not tok : break
	print(tok)
