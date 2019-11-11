# Une liste de tuple
# Ce script est sous controle de version
from Ext import a, augment
# On charge le fichier Evt.txt
E=[]
with open("Evt.txt","r") as fichier:
  E=fichier.readlines()

print(E[-1])
print(a)
print(augment(2))

M="123456"
j=0
print("i,j,M")
# on joue avec la focntion %
for i in range(10):
  if i%len(M) ==0:
    j=0
  else:
    j+=1
  print(i,j,M[j])
