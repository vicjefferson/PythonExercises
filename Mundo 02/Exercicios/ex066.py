s = digt = 0

while True:
  num = int(input('Digite um valor [999 para parar]: '))
  if num == 999:
    break
  else:
    s += num
    digt += 1

print(f'A soma dos {digt} valores foi {s}')