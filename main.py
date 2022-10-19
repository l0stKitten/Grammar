from runner import Runner
import mylexer

# scope
def buscar_id(nodo):
  if nodo.symbol == 'id':
    print("Variable encontrada: ", nodo.symbol, " - ", nodo.lexeme)
  for child in nodo.children:
    buscar_id(child)

def definicion_var(root):
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