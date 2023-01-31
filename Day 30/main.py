try:
    file = open('a_file.txt')
    a_dictionary = {"key": "value"}
    print(a_dictionary['key'])
except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write('something')
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    # print("File was closed")
    # raise TypeError("This is an error that I made up.")

height=int(input("Height:"))
weight=int(input("weight:"))
if height>3:
    raise ValueError("If you are human then your height can't be over 3 meters but it can if you are not human and i think you are not!")
bmi=weight/height**2
print(bmi)