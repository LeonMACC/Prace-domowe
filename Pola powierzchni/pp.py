inp =int(input("Czego pole chcesz obliczyc? (sześcianu [1], trójkąta [2], kuli [3], torusa [4]) "))

if inp == 1:
      s6 = float(input("podaj długosc boku szescianu "))
      wyniks6 = 6*s6**2
      print(wyniks6)

if inp == 2:
      st = float(input("podaj a "))
      sh = float(input("podaj h "))
      wynikst = (st * sh )/2
      print(wynikst)

if inp == 3:
      pi = 3.14
      r = float(input("podaj r "))
      wynikkul = 4*pi *r
      print(wynikkul)

if inp == 4:
      pi = 3.14
      r = float(input("podaj r "))
      R = float(input("podaj  "))
      wyniktor = ((4*pi)**2)*r*R
      print(wyniktor)

