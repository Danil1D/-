from random import randint

len_array = 5  
count_array = 5 

array = list()

for i in range(count_array):
    array.append([])
    for _ in range(len_array):
        array[i].append(randint(0, 10)) 

print(array)

def maxaverline(mtx):
    return max(sum(line) / len(line) for line in mtx) 
  
print(maxaverline(array))

