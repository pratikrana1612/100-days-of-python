# with open("my_file.txt") as file:
#     contents=file.read()
#     print(contents)
#     file.close()

with open("new_file.txt",'a') as file:
    file.write("\nNew text.")