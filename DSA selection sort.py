my_array = [ 2,32,5,10,100,50,28,9,5]
l = len (my_array)
for i in range(l):
    min_index = i
    for j in range (i+1,l):
        if my_array[j] < my_array[min_index]:
            min_index = j
    my_array[i],my_array[min_index] = my_array[min_index],my_array[i]
print("mang sau sap xep la:",my_array)

