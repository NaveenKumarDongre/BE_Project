f = open("branch.txt", "r")
txt = f.read()
res = txt.split("\\n")
print(res)
file_object = open('branch_output.txt', 'a')

for i in range(0, len(res)):
#     arr[i] = " ".join( arr[i].split(" ")[1:] )
    file_object.write(res[i]+"\n")
# Close the file
file_object.close()
   
# for i in arr:
#     print(i)

f.close()