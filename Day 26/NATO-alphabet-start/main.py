import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass
    # print(value)

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
with open('nato_phonetic_alphabet.csv') as file:
    csv_file = pandas.read_csv(file)

    dictionary_letters = {value.letter: value.code for (key, value) in csv_file.iterrows()}
# csv_file=csv_file.to_dict()
# print(csv_file)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    try:
        word = input("Enter a Word:").upper()
        nato_alphabates = [dictionary_letters[letter] for letter in word]
    except KeyError:
        print("Sorry letters in alphabet only!")
        generate_phonetic()
    else:
        print(nato_alphabates)
    

generate_phonetic()
# print(letters)
# nato_alphabates = []
# for letter in letters:
#     for (key, value) in csv_file.items():
#         if (key == letter):
#             nato_alphabates.append(value)


