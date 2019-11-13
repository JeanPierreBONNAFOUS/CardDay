# Traitement CardDay LOG
# Ce script est sous controle de version
from logStat import E as logFile
import os, time

def fileInfo(f):
  I=os.stat(f)
  print(time.ctime(I.st_ctime))
  print(time.ctime(I.st_atime))
  print(time.ctime(I.st_mtime))

def countX(l):
  L=l.count('X')
  return L

def pourcentage(x):
  return int(x/12*100)

for i in logFile:
  h=countX(i)
  p=pourcentage(h)
  print("{0}{1:d}%".format(i[:3],p))

fileInfo('IR_LOG314.txt')
# ZUT