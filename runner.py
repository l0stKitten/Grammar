import pandas as pd
import graphviz
from all_nodes import node_stack
from all_nodes import node_parser
import time

class Runner:
  #global stack, tokens, root
  def __init__(self, tokens):
    self.syntax_table = pd.read_csv("latabla.csv", index_col=0)
    
    self.terminales = list( self.syntax_table.columns.values )[:-1]
    
    self.stack = []
    self.stack.append( node_stack('$', True) )# symbol 1
    self.stack.append( node_stack('PGR', False) ) #Symbol 2

    # main id ini_llave id igual bool punto_coma fin_llave
    '''self.tokens = [   
            {'type':'main', 'lexeme':'Algoritmo', 'line':1}, 
            {'type':'id', 'lexeme':'prueba', 'line':1},
            {'type':'ini_llave', 'lexeme':'{', 'line':1},
            {'type':'id', 'lexeme':'x', 'line':1},
            {'type':'igual', 'lexeme':'=', 'line':1},
            {'type':'bool', 'lexeme':'true', 'line':1},
            {'type':'punto_coma', 'lexeme':';', 'line':1},
            {'type':'fin_llave', 'lexeme':'}', 'line':1},
            {'type':'$', 'lexeme':'$', 'line':1}
        ]'''
    self.tokens = tokens

    self.root = node_parser( self.stack[-1].value, self.tokens[0]['lexeme'], [] )

    self.grafico = graphviz.Digraph('graficoGRAMAR')
    
    self.temp = self.root

  #-------------------Funciones  
  def is_terminal(self, value):
    return value in self.terminales

  def isNaN(self, string):
    return string == ''

  def print_stack(self, stack):
    for a in stack:
      print(a.value, "-", a.terminal)

  def print_input(self):
    print("\nInput:")
    for t in self.tokens:
      print(t['type'], ",", t['lexeme'])
    print()

  def dfs(self, root, elem):
    #DFS
    stack = []
    stack.insert(0,root)
    vista = []
    vista.append(root)
  
    while stack:
      n = stack.pop(0)
      #print(n.symbol, "->", end=" ")
      adyacentes = n.children

      if n.symbol == elem and len(adyacentes) == 0 and n.lexeme != 'hoja':
        print('Encontrado: ', n.symbol)
        return n
  
      for i in adyacentes:
        if i not in vista:
          stack.insert(0,i)

  def print_tree(self, root, grafico):
    for i in root.children:
      grafico.edge(str(i.father.symbol), str(i.symbol))

  def update(self, stack_value, token_type, stack, root):
    #print("-----------------------------------")
    print(stack_value, "----------", token_type)
    #print("-----------------------------------")
    production = self.syntax_table.loc[stack_value][token_type]
    print(production, "///////")
    if self.isNaN(production):
      print("Error sintáctico: no hay con qué reemplazar")
      return
    else:
      elem = production.split(" ")
      if elem[0] == "ep":
        
        buscar = stack.pop()

        #--------------------Añadir ep en el árbol
        print('Hay que buscar ', buscar.value)
        tree_nodo_temp = self.dfs(root, buscar.value)
        self.grafico.node(str(tree_nodo_temp.id), tree_nodo_temp.symbol)
        print(tree_nodo_temp.symbol)
        tree_nodo =  node_parser('ep', 'hoja', [], tree_nodo_temp, 1)
        self.grafico.node(str(tree_nodo.id), tree_nodo.symbol)
        tree_nodo_temp.children.insert(0, tree_nodo)
        self.grafico.edge(str(tree_nodo_temp.id), str(tree_nodo.id), ordering="out")
        return
      
      #------Pila
      elem = elem[::-1]
  
      buscar = stack.pop()
      print('Hay que buscar ', buscar.value)
      tree_nodo_temp = self.dfs(root, buscar.value)
      self.grafico.node(str(tree_nodo_temp.id), tree_nodo_temp.symbol)
      print(tree_nodo_temp.symbol)
      
      for i in elem:
        is_term = self.is_terminal(i)
        nodo = node_stack(i, is_term)
        stack.append(nodo)
      
      #------Árbol
      elem = elem[::-1]
      for i in elem:
        is_term = self.is_terminal(i)
        if is_term == True:
          tree_nodo =  node_parser(i, 'hoja', [], tree_nodo_temp, 1)
          self.grafico.node(str(tree_nodo.id), tree_nodo.symbol)
        else:
          tree_nodo =  node_parser(i, 'prueba', [], tree_nodo_temp, 1)
          self.grafico.node(str(tree_nodo.id), tree_nodo.symbol)
        
        tree_nodo_temp.children.append(tree_nodo)
        self.grafico.edge(str(tree_nodo_temp.id), str(tree_nodo.id), ordering="out")
  
      #for i in tree_nodo_temp.children:
        #print(i.symbol, ' hijo de ', tree_nodo_temp.symbol)
  
  def run(self):
    print(self.tokens)
    while True:
      print("\nITERATION ...")
      self.print_stack(self.stack)
      self.print_input()
      
      print(self.stack[-1].value, '-', self.tokens[0]['type'])
      if self.stack[-1].value == '$' and self.tokens[0]['type'] == '$':
        print("Todo bien!")
        break
      # cuando son terminales
      if self.stack[-1].terminal:
        print("terminales")
        if self.stack[-1].value == self.tokens[0]['type']:
          self.stack.pop()
          self.tokens.pop(0)
        else:
          print("ERROR sintáctico")
          break
        continue
      self.update(self.stack[-1].value, self.tokens[0]['type'], self.stack, self.root)
      #time.sleep(0.5)
    self.grafico.render(directory='doctest-output').replace('\\', '/')