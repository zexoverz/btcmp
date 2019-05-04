def cetak_gambar(x):
  if (x%2 == 1):
    for i in range(x):
      if (i == x//2):
        for j in range(x):
          print('*', end=" ")
      else:
        for j in range(x):
          if (j == 0) or (j == x-1):
            print('*', end=" ")
          else:
            print('=', end=" ")
      print("\n")
  else:
    print("Failed")

cetak_gambar(5)
