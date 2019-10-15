from random import randint
chislo_popitok = 1
ochko = 1
ochki=[]
while chislo_popitok <=5:
  chislo_popitok += 1
  g = int(input("Введите число от 1 до 6  ? "))
  j = randint(1,6)
  difference = abs(g - j)

  if difference == 0:
      ochko = 6
      ochki.append(ochko)
  elif difference == 1:
      ochko = 5
      ochki.append(ochko)
  elif difference == 2:
      ochko = 4
      ochki.append(ochko)
  elif difference == 3:
      ochko = 3
      ochki.append(ochko)
  elif difference == 4:
      ochko = 2
      ochki.append(ochko)
  elif difference == 5:
     ochko = 1
     ochki.append(ochko)

  print("ваш балл" , ochko)

  all_ochkos = sum(ochki)
print("количество очков", all_ochkos)

if all_ochkos < 25:
  print("вы проиграли(")
else:
  print("вы выиграли) ")