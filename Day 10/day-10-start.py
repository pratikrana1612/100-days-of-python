# Functions with outputs


def format_name(f_name, l_name):
    """This the function which will return you string with every first character capital"""
    if(f_name=="" or l_name==""):
      return  "You have entered invalid input"
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} and {l_name}"

print(format_name(input("What is your first name?"),input("What is your last name?")))
# format_name()
