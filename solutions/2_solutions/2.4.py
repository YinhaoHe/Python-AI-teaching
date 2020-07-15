import numpy as np

# To open file, mode set to 'r' means read only
with open ('data.txt', mode = 'r') as f:
  
  read_in = []
  write_data= []
  data = f.readlines()
  data = list([i.strip() for i in data]) #strip can be used to remove the head and tail space char

  data.pop(0) # first line is useless

  for words in data:
    b = words.split(",")
    read_in.append(b)
  array1 = np.array([read_in]).reshape(10000, 4)

  for i in range(-1,10000, 3):
    array1[i, 1 ] = 1992

  with open('newData.csv', mode = 'w') as w:
    for i in range(10000):
      writein = np.array_str(array1[i])
      writein = writein.replace('[', '')
      writein = writein.replace(']', '')
      writein = writein.replace("'", '')
      writein = writein.replace(' ', ',')
      write_data.append(writein)
      w.write(writein + "\n")

  #shape
  print(array1.shape)
  #dimension
  print(array1.ndim)
  #size
  print(array1.size)
  