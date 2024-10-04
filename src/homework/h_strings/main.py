from strings import get_dna_complement, get_hamming_distance, display_menu, prompt1, prompt2

def main():

    options = ("1", "2", "3")
    selection = "0"

    while selection not in options:
        display_menu()
        selection = str(input("Please enter menu selection : "))

    if selection == "3":
        exit()
    
    elif selection == "1":
        dna1, dna2 = prompt1()
        ham_distance = get_hamming_distance(dna1, dna2)
        print(f"The hamming distance of strand {dna1} and {dna2} is {ham_distance}.")

    elif selection == "2":
        input2 = prompt2()
        comp = get_dna_complement(input2)
        print(f"The complement of strand {input2} is {comp}.")

if __name__ == "__main__":
    main()