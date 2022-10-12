counter = 0
node_count = 0
class node_stack:
  def __init__(self, value, terminal):
    global counter
    self.id = counter
    self.value = value
    self.terminal = terminal # boolean

    counter += 1

class node_parser:
  def __init__(self, symbol, lexeme = None, children = [], father = None, line=None):
    global node_count
    self.symbol = symbol
    self.lexeme = lexeme
    self.line = line
    self.children = children
    self.father = father
    self.vista = False
    self.id = node_count

    node_count += 1