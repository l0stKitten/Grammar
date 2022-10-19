from runner import Runner
import mylexer

# scope
def buscar_id(nodo):
  if nodo.symbol == 'id':
    print("Variable encontrada: ", nodo.symbol, " - ", nodo.lexeme)
  for child in nodo.children:
    buscar_id(child)

def definicion_var(root):
  #print(root.symbol)
  if root.symbol == 'define':
    nodo_id = root.father.children[1]
    buscar_id(nodo_id)

  if root.symbol == 'EXPRES8':
    if root.children[0].symbol == 'id' and root.children[1].children[0].symbol == 'ini_parentesis':
      nodo = root.children[0]
      print("Función encontrada: ", nodo.symbol, " - ", nodo.lexeme)

  for child in root.children:
    definicion_var(child)

def uso_var(root):
  if root.symbol == 'define':
    nodo_id = root.father.children[1]
    buscar_id(nodo_id)

  for child in root.children:
    definicion_var(child)

data = mylexer.data_tokens
ejecucion = Runner(data)
ejecucion.run()

print("---- SCOPE -----")
definicion_var(ejecucion.root)