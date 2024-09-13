import decisions

def main():
    #create values from user input
    option = float(input("Enter Option: "))
    total = float(input("Enter Total: "))

    #assign variables from functions
    result = decisions.get_options_ratio(option, total)
    rating = decisions.get_faculty_rating(result)

    #display rating and rounded ratio value
    print(rating)
    print("Your ratio is", round(result, 2))

main()