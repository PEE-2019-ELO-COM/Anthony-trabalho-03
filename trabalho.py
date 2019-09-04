notaVE1=float(input('Digite sua nota da VE1:'))
while(notaVE1<0 or notaVE1>10 ):
  print("Nota inválida")
  notaVE1=float(input('Digite sua nota da VE1:'))
notaVE2=float(input('Digite sua nota da VE2:'))
while(notaVE2<0 or notaVE2>10 ):
  print("Nota inválida")
  notaVE2=float(input('Digite sua nota da VE2'))
notaVC=float(input('Digite sua nota da VC:'))
while(notaVC<0 or notaVC>10):
  print("Nota inválida")
  notaVC=float(input('Digite sua nota da VC'))
notas = (notaVE1 + notaVE2)/2 + notaVC
notaextra = (20 - notas)/2
if notas>=12:
  print("Você precisa tirar 4.0 na VF")
else:
 print("Você precisa tirar " + '{}'.format(notaextra)) 
