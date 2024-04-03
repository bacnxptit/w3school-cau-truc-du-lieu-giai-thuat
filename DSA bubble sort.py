my_array = [28,25,9,6,30,100,4,1,0,2,3,1,0]
l = len(my_array)
for i in range(l-1):
    for j in range(l-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j],my_array[j+1] = my_array[j+1],my_array[j]
print("mang dc sap xep la",my_array)