import numpy as np

# Crear un tablero de triqui 3x3
tablero = np.zeros((3,3))

# Funcion imprimir tablero ----------------------------------------------------------
def imprimirTablero():
  tableroImprimir = []

  for i in range (0,3):
    fila=[]
    for j in range(0,3):
      if tablero[i][j] == 0:
        fila.append(" ")
      elif tablero[i][j]== 1:
        fila.append("O")
      else:
        fila.append("X")
    tableroImprimir.append(fila)

  for i in range (0,3):
    print(tableroImprimir[i])


# Funcion marcar opcion ---------------------------------------------------------------
# Esta funcion pone en el tablero, en la ubicacion seleccionada, la x o el o respectivamente.
def marcarOpcion(x,y,opc):
  #x es la fila, y es la columna y opc es el caracter que se desea ubicar (2:'x' (usuario),1:'o'(computador))
  tablero[x][y]=opc


# Funcion verificar campeón -----------------------------------------------------------
def verificarCampeon(x):
  #Esta funcion verifica si existe en el momento un ganador, verificando tanto las columnas, filas y diagonales, para comprobar si existen tres caracteres (x) seguidos.
  if vertical(x)==True or horizontal(x)==True or diagonal(x)==True:
    if(x==2):
      print("Ha ganado el usuario")
    else:
      print("Ha ganado la maquina")
    return 1
  else:
    return 0
    
def vertical(x):
  #esta funcion verifica las columnas 
  for i in range(0,3):
    if tablero[0][i] == x and tablero[1][i]==x and tablero[2][i]==x:
      return True
  return False

def horizontal(x):
  #esta funcion verifica las filas 
  for i in range(0,3):
    if tablero[i][0] == x and tablero[i][1]==x and tablero[i][2]==x:
      return True
  return False

def diagonal(x):
  #esta funcion verifica las diagonales 
  if tablero[0][0] == x and tablero[1][1]==x and tablero[2][2]==x:
    return True
  if tablero [2][0]==x and tablero[1][1]==x and tablero[0][2]==x:
    return True
  return False

def espaciosEnBlanco():
  for i in range(0,3):
    for j in range(0,3):
      if tablero[i][j]==0:
        return False
  print("Se ha obtenido un empate")        
  return True

def juego():
  imprimirTablero()
  turno = 2
  x=0
  y=0
  seguirJugando = True
  while(seguirJugando):
    
    if(turno==1):
      print("Es turno de la maquina")
    else:
      print("Turno del usuario")
      imprimirTablero()
      print("En que fila desea ubicar su simbolo?")
      x=int(input())
      print("En que columna dese ubicar su simbolo?")
      y=int(input())
      marcarOpcion(x,y,turno)
      imprimirTablero()

    if(verificarCampeon(turno)==True or espaciosEnBlanco()==True):
      seguirJugando=False
      
      
    if(turno==1):
      turno=2
    else:
      turno=1
  print("Juego terminado")
 
juego()
