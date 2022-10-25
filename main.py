from runner import Runner
import mylexer
import all_nodes

# scope
def buscar_id(nodo, texto):
  if nodo.symbol == 'id':
    print(texto, nodo.symbol, " - ", nodo.lexeme)
    
  for child in nodo.children:
    buscar_id(child, texto)

def definicion_var(root):
  if root.symbol == 'define':
    nodo_id = root.father.children[1]
    buscar_id(nodo_id, "Variable definida: ")

  if root.symbol == 'EXPRES8':
    if root.children[0].symbol == 'id' and root.children[1].children[0].symbol == 'ini_parentesis':
      nodo = root.children[0]
      print("Función encontrada: ", nodo.symbol, " - ", nodo.lexeme)
      
  for child in root.children:
    definicion_var(child)

def uso_var(root):
  if root.symbol == 'EXPRES8':
    if root.children[0].symbol == 'id' and root.children[1].children[0].symbol == 'ep':
      print("Variable usada: ", root.children[0].symbol, " - ", root.children[0].lexeme)

  for child in root.children:
    uso_var(child)

def fin_funcion(root):
  if root.symbol == 'fin_llave' and root.father.symbol == 'FUN':
    nodo = root.father.children[3]
    print("Función: ", nodo.lexeme, " terminó")
  for child in root.children:
    fin_funcion(child)

def funcion(root):
  if root.symbol == "FUN":
    print("Funcion encontrada: ", root.children[3].symbol, " - ", root.children[3].lexeme)
    print("Symbol:", root.children[0].symbol, root.children[1].symbol, root.children[2].symbol, root.children[3].symbol)
    print("Lexema:", root.children[0].lexeme, root.children[1].lexeme, root.children[2].lexeme, root.children[3].lexeme)

  for child in root.children:
    funcion(child)

def scope(root):
  print("estamos en el main")
  # Buscamos dentro del main
  # Si encuentra definición insertar en la tabla de símbolos 
  # Si encuentra asignación buscar en la tabla y colocar la asignación
    # Si la asignación no está definida anteriormente dentro de su scope dar error
  #Si encuentra una función debe buscar la función
      # Dentro de la función agregar las variables definidas
      # Si se encuentra una asignación buscar en la tabla y colocar la asignación
        # Si la asignación no está definida anteriormente dentro de su scope dar error
  #Si la función encontrada ha terminado quitar las variables que tienen ese scope de la tabla de símbolos
  for child in root.children:
    scope(child)

data = mylexer.data_tokens
ejecucion = Runner(data)
ejecucion.run()

#print("---- SCOPE -----")
#print("....... Variables Declaradas .......")
#definicion_var(ejecucion.root)
#print("\n....... Variables Usadas .......")
#uso_var(ejecucion.root)
#print("\n....... Término de Funciones .......")
#fin_funcion(ejecucion.root)

'''print("Funcionamiento de la pila")
tabla_sim = all_nodes.tabla_simbolos()
print(tabla_sim.pila)
tabla_sim.insertar(1)
tabla_sim.insertar(2)
tabla_sim.insertar(3)
tabla_sim.insertar(4)

tabla_sim.imprimir()

tabla_sim.eliminar()
tabla_sim.imprimir()'''