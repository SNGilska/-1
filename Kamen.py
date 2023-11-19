rost = input()
a = 0
b = 0
while rost != '!':
      if int(rost) > 160 and int(rost) < 180:
         print('podhodit')
         a += 1
      else:
         b += 1
         print('ne podhodit')
      rost = input()
print(a, b)

   