import random
import string




def generate_password(min_length,min_number_length, min_punc_length, needs_number=True, needs_punc=True):
    letters = string.ascii_letters
    numbers = string.digits
    punctuations = string.punctuation
    
    available_characters = letters
    if needs_number:
        available_characters = available_characters + numbers
    if needs_punc:
        available_characters = available_characters + punctuations

    password = ""
    meets_criteria = False
    has_number = False
    has_punc = False
    while not meets_criteria or len(password) < min_length:
        to_add = random.choice(available_characters)
        password+=to_add
        number_count=0
        punc_count=0

        for char in password:
            if char in numbers:
                number_count+=1
            if char in punctuations:
                punc_count+=1

        # for char in password:
        #     if to_add in numbers:
        #         has_number = True
        #     if to_add in punctuations:
        #         has_punc = True
        
        meets_criteria = True

        if needs_number:
            if number_count < min_number_length:
                meets_criteria = False
        if needs_punc:        
            if punc_count < min_punc_length:
                meets_criteria = False

        # if not has_number:
        #     meets_criteria = False
        # if not has_punc:
        #     meets_criteria = False

    return password



while True:
    try:
        min_length=input("What is the minimum length of your password?")
        min_length=int(min_length)
        break
    except ValueError:
        print("Please enter a valid integer")

while True:
    try:
        needs_number_input = input("Do you need numbers in your password? (y/n)").lower()
        if needs_number_input not in ["y", "n"]:
            raise Exception("Enter either y or n")
        if needs_number_input == "y":
            needs_number = True
            while True:
                try:
                    min_number_length = int(input("How many minimum numbers do you want?"))
                    break
                except ValueError:
                    print("Please enter an integer value")    
        break
    except Exception as e:
        print(e)

while True:
    try:
        needs_punc_input = input("Do you need special characters in your password? (y/n)").lower()
        if needs_punc_input not in ["y", "n"]:
            raise Exception("Enter either y or n")
        if needs_punc_input == "y":
            needs_punc = True
            while True:
                try:
                    min_punc_length = int(input("How many minimum spl. characters do you need?"))
                    break
                except ValueError:
                    print("Enter a valid integer")   
        break
    except Exception as e:
        print(e)

        
# if needs_number_input == "y":
#     needs_number = True
# else:
#     needs_number = False

# if needs_punc_input == "y":
#     needs_punc = True
# else:
#     needs_punc = False

if needs_number:
    if min_number_length == 0:
        needs_number = False

if needs_punc:
    if min_punc_length == 0:
        needs_punc = False

final_password = generate_password(min_length,min_number_length, min_punc_length, needs_number, needs_punc)
print(f"Final Password: {final_password}")
print(f"Password Length: {len(final_password)}")

final_number_count=0
final_punc_count=0

for char in final_password:
    if char in string.digits:
        final_number_count+=1
    if char in string.punctuation:
        final_punc_count+=1

print(f"Number Count: {final_number_count}")
print(f"Sp. Char. Count: {final_punc_count}")

