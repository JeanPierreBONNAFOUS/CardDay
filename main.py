# Traitement CardDay LOG
# Ce script est sous controle de version
from logStat import E as logFile

def countX(l):
  L=l.count('X')
  return L

for i in logFile:
  h=countX(i)
  print("{0:02d}".format(h))