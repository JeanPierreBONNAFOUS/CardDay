# Une liste de tuple
# Ce script est sous controle de version
from Ext import a, augment
import logStat

def countX(l):
  L=l.split(':')
  return L[1].count('X')

for i in logStat.E:
  h=countX(i)
  print("{0:02d}".format(h))