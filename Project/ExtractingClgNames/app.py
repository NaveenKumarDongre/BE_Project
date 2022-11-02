f = open("clg.txt", "r")
arr = f.readlines()
print(len(arr))

 
# unique_clg = set(arr)
file_object = open('output.txt', 'a')
# Append 'hello' at the end of file
for i in range(1, len(arr)):
    arr[i] = " ".join( arr[i].split(" ")[1:] )
    file_object.write(arr[i])
# Close the file
file_object.close()
   
# for i in arr:
#     print(i)

f.close()