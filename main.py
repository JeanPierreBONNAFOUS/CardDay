# Traitement CardDay LOG
# Ce script est sous controle de version
from logStat import E as logFile

def countX(l):
  L=l.count('X')
  return L

def pourcentage(x):
  return int(x/12*100)

for i in logFile:
  h=countX(i)
  p=pourcentage(h)
  print("{0}{1:d}%".format(i[:3],p))

