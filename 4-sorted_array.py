data=[['a','c','b','e','d'],['g','e','f'],['h','i','j','k']]

def sort_1st_elements(input):
  elements = len(input)
  if (elements > 1):
    for i in range(elements):
      for j in range(0,elements-i-1):
        if (len(data[j]) > len(data[j+1])):
          data[j],data[j+1] = data[j+1],data[j]
    return input

def sort_array(input):
  sort_1st_elements(input)
  elements = len(input)
  for i in range(0,elements):
    childs = len(input[i])
    if (childs>1):
      for j in range(childs):
        for k in range(0,childs-j-1):
          if (input[i][k] > input[i][k+1]):
            input[i][k], input[i][k+1] = input[i][k+1], input[i][k]
  print(input)

sort_array(data)
