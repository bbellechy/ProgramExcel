import pandas as pd
import string
import re
from tabulate import tabulate
show = None
# Input row and column
input_for_column = input("End column: ").upper()
while input_for_column not in list(string.ascii_uppercase[:26]):
    input_for_column = input("Repeat end column: ").upper()


input_for_rows = int(input("End row: "))
while input_for_rows > 100 or 1 > input_for_rows:
    input_for_rows = int(input("Repeat end row: "))


def for_cell(cell):
    result_cell = " ".join(cell).split(" ")
    return result_cell


def alph():
    return list(string.ascii_uppercase[:26])


def gettable():
    global show
    if show is None:
        show = pd.DataFrame(index=range(1, input_for_rows + 1), columns=alph()[:ord(input_for_column)-64])
    return show

# Get cell index
def getindex():
  while True:
    cell = input('Cell: ')
    list_of_cell = []
    if len(cell) > 2:
        dex = cell[1] + cell[2]
    else:
        dex = cell[1]
    for a in range(1, int(dex) + 1):
        list_of_cell.append(a)
    
    show = gettable()
    i = cell[0]
    data = input("Data: ")
    show.loc[list_of_cell[-1], i] = data
    print(tabulate(show.fillna(''), headers='keys', tablefmt='fancy_grid'))
    
    if data[0] == "=":
      cal = calculate(data, show)
      sum = Cal(cal, show)
      show.loc[list_of_cell[-1], i] = sum
    
    print(tabulate(show.fillna(''), headers='keys', tablefmt='fancy_grid'))
      
  return show


def calculate(data, show):
  if not str(data).startswith('='):
    return data

  chk_data = re.findall(r'[A-Z]\d+', data)
  for val in chk_data:
    col = ord(val[0]) - 64
    row = int(val[1:])
    pos = position(row, col, show)
    cell = (row, col)
    keep = set()
    if cell not in keep:
      keep.add(cell)
    if data.startswith('='):
        value = Cal(calculate(pos, show), show)
    else:
        value = pos
        print("เข้าelse")
    data = f"{data.replace(val, str(value))}"
    keep.remove(cell)
  return data[1:]

def Cal(data, show):
  sum = eval(str(data),{},show)
  return sum
def position(row, col, show):
  return show.loc[row, chr(ord('A') + col - 1)]

def table():
    return getindex()

print(table())
