counter = 0
node_count = 0
class node_stack:
  def __init__(self, value, terminal, lex = None):
    global counter
    self.id = counter
    self.value = value
    self.terminal = terminal # boolean
    self.lexeme = lex

    counter += 1

class node_parser:
  def __init__(self, symbol, type = None, children = [], father = None, line=None, lex=None):
    global node_count
    self.symbol = symbol
    self.type = type
    self.line = line
    self.children = children
    self.father = father
    self.lexeme = lex
    self.id = node_count

    node_count += 1

class node_scope:
  def __init__(self, var, token, linea, var_type, scope, asignacion = None):
    self.var = var
    self.token = token
    self.linea = linea
    self.var_type = var_type
    self.scope = scope
    self.asignacion = asignacion

class tabla_simbolos:
  def __init__(self):
    self.pila = []

  def insertar(self, elem):
    self.pila.append(elem)

  def eliminar(self):
    self.pila.pop()

  def buscar(self, elem):
    for i in self.pila:
      if i.nodo.symbol == elem:
        return i
  def imprimir(self):
    for i in self.pila:
      print(i, " -> ", end=" ")
    print()
