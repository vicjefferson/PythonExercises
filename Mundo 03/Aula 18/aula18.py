galera = list()
data = list()
totmai = totmen = 0
for c in range(0, 3):
  data.append(str(input('Name: ')))
  data.append(int(input('Age: ')))
  galera.append(data[:]) # [:] para criar cópia, caso contrário próxima linha vai apagar e galera não recebe valores
  data.clear() # para não acumular e ficar algo como [['a', 1], ['a', 1, 's', 2], ['a', 1, 's', 2, 'd', 3]]

print()

for p in galera:
  print(f'{p[0]} tem {p[1]} anos de idade')

print()

for p in galera:
  if p[1] >= 21:
    print(f'{p[0]} é maior de idade e tem {p[1]} anos')
    totmai += 1
  else:
    print(f'{p[0]} é MENOR de idade')
    totmen += 1

print(totmai)