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