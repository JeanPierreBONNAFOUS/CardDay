# Une liste de tuple
from Ext import a, augment
E=[]
with open("Evt.txt","r") as fichier:
  E=fichier.readlines()
Text="strange quote"
print(E[-1])
print(a)
print(augment(2))

M="12345"
j=0
print("i,j,M")
for i in range(10):
  if i%len(M) ==0:
    j=0
  else:
    j+=1
  print(i,j,M[j])
