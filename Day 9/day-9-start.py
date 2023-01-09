programming_dictionary = {
    "Bug":
    "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and overagain.",
    "Loop": "The action of doing something over and over again"
}
# print(programming_dictionary["Bug"])

programming_dictionary["Name"] = "Pratik"

empty_dictionary = {}
# programming_dictionary={}
print(programming_dictionary)
programming_dictionary["Bug"] = "Progamme khoto lakhyo che"
print(programming_dictionary)
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

###################################
# Nesting
capitals = {"France": "Paris", "Germary": "Berlin"}

travel_log = [
    # "Gujarat":{"cities_visited":"Ahmedabad","cities_visited":"Surat","cities_visited":"Gandhinagar"}
    {
        "Country": "Gujarat",
        "cities_visited": ["Ahmedabad", "Surat", "Gandhinagar"],
        "total_visit": 12
    },
    {
        "Country": "Mubai",
        "cities_visited": ["Ahmedabad", "Surat", "Gandhinagar"],
        "total_visit": 25
    }
]
starting_dictionary = {z`
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}
# starting_dictionary["c"]=9
final_dictionary=starting_dictionary
print(final_dictionary)