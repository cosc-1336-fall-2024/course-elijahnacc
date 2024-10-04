#
def get_hamming_distance(dna1, dna2):

    distance = 0

    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
    
    return distance

def get_dna_complement(dna):

    conversion = {"A":"T", "C":"G", "G":"C", "T":"A"}
    complement = ""

    for i in range(len(dna)):
        j = int(len(dna) - i - 1)
        base = dna[j]
        complement += conversion[base]
    
    result = complement
    
    return result

def display_menu():
    print("1) Hamming Distance")
    print("2) DNA Complement")
    print("3) Exit")

def valid_strand(strand):
    
    options = ("A", "C", "G", "T")
    invalid_options = 0

    for i in range(len(strand)):
        if strand[i] not in options:
            invalid_options += 1

    if invalid_options == 0:
        return True
    else:
        return False

def prompt1():

    while True:
        
        dna1 = str(input("Enter DNA strand 1 : ")).upper()
        dna2 = str(input("Enter DNA strand 2 : ")).upper()

        if len(dna1) == len(dna2):

           valid1 = valid_strand(dna1)
           valid2 = valid_strand(dna1)

           if valid1 == True and valid2 == True:
                break
           
           else:
               print("Invalid values in strand(s)")
        
        else:
            print("Strands must be same length")

    return dna1, dna2

def prompt2():

    while True:

        dna = str(input("Enter DNA strand : ")).upper()
        valid = valid_strand(dna)

        if valid == True:
            break
        else:
            print("Invalid value in strand")

    return dna