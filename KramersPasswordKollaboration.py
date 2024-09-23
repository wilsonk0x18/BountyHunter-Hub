from itertools import combinations

splash_screen = """
      ,-.                               ____                    
  ,--/ /|                             ,'  , `.                  
,--. :/ |   __  ,-.                ,-+-,.' _ |          __  ,-. 
:  : ' /  ,' ,'/ /|             ,-+-. ;   , ||        ,' ,'/ /| 
|  '  /   '  | |' | ,--.--.    ,--.'|'   |  || ,---.  '  | |' | 
'  |  :   |  |   ,'/       \  |   |  ,', |  |,/     \ |  |   ,' 
|  |   \  '  :  / .--.  .-. | |   | /  | |--'/    /  |'  :  /   
'  : |. \ |  | '   \__\/: . . |   : |  | ,  .    ' / ||  | '    
|  | ' \ \;  : |   ," .--.; | |   : |  |/   '   ;   /|;  : |    
'  : |--' |  , ;  /  /  ,.  | |   | |`-'    '   |  / ||  , ;    
;  |,'     ---'  ;  :   .'   \|   ;/        |   :    | ---'     
'--'             |  ,     .-./'---'          \   \  /           
                  `--`---'                    `----'        

________________________________________________________________
________________________________________________________________


"""

print(splash_screen)


print("You will be asked a series of questions on the subject to create a wordlist consisting of good passwords relating to that person.\n This is not a general password list, so if you are trying to crack a password, please use a common wordlist first\n")
print("If you do not have an answer, just press enter and continue.\n")

total_inputs = []

# Subject
subject_firstname = input("What is the subject's first name: ")
if subject_firstname:
    total_inputs.append(subject_firstname)
subject_lastname = input("What is the subject's last name: ")
if subject_lastname:
    total_inputs.append(subject_lastname)
subject_Birth_year = input("What is the subject's birth year (enter a number): ")
if subject_Birth_year:
    total_inputs.append(subject_Birth_year)
subject_Birth_month = input("What is the subject's birth month (enter a number): ")
if subject_Birth_month:
    total_inputs.append(subject_Birth_month)
subject_Birth_day = input("What is the subject's birth day (enter a single number): ")
if subject_Birth_day:
    total_inputs.append(subject_Birth_day)

# Subject's Parents
subject_fathersname = input("What is the subject's father's name: ")
if subject_fathersname:
    total_inputs.append(subject_fathersname)
subject_fathers_Birth_year = input("What is the subject's father's birth year (enter a number): ")
if subject_fathers_Birth_year:
    total_inputs.append(subject_fathers_Birth_year)
subject_fathers_Birth_month = input("What is the subject's father's birth month (enter a number): ")
if subject_fathers_Birth_month:
    total_inputs.append(subject_fathers_Birth_month)
subject_fathers_Birth_day = input("What is the subject's father's birth day (enter just the day number): ")
if subject_fathers_Birth_day:
    total_inputs.append(subject_fathers_Birth_day)

subject_mothersname = input("What is the subject's mother's name: ")
if subject_mothersname:
    total_inputs.append(subject_mothersname)
subject_mothers_Birth_year = input("What is the subject's mother's birth year (enter a number): ")
if subject_mothers_Birth_year:
    total_inputs.append(subject_mothers_Birth_year)
subject_mothers_Birth_month = input("What is the subject's mother's birth month (enter a number): ")
if subject_mothers_Birth_month:
    total_inputs.append(subject_mothers_Birth_month)
subject_mothers_Birth_day = input("What is the subject's mother's birth day (enter just the day number): ")
if subject_mothers_Birth_day:
    total_inputs.append(subject_mothers_Birth_day)

# Subject's Siblings
siblings_list = []
Siblings = input("Does your subject have siblings? (enter nothing if not): ")

if Siblings == "":
    print("No siblings")
else:
    while True:
        siblings_name = input("What is the subject's sibling's first name (or type 'exit' to stop adding siblings): ")
        if siblings_name == "exit":
            break
        if siblings_name:
            siblings_list.append(siblings_name)
            total_inputs.append(siblings_name)

# Subject's Pets
pets_list = []
pets = input("Does your subject have pets? (enter nothing if not): ")

if pets == "":
    print("No pets")
else:
    while True:
        pets_name = input("What is the subject's pet's first name (or type 'exit' to stop adding pets): ")
        if pets_name == "exit":
            break
        if pets_name:
            pets_list.append(pets_name)
            total_inputs.append(pets_name)

# Special Words or Phrases
spwords_list = []
spwords = input("Do you have any special words that you would also like to implement into your word list (enter nothing if not): ")

if spwords == "":
    print("No special words")
else:
    while True:
        spwords_name = input("What special word would you like to add (or type 'exit' to stop adding special words): ")
        if spwords_name == "exit":
            break
        if spwords_name:
            spwords_list.append(spwords_name)
            total_inputs.append(spwords_name)

# Print the list of all inputs
print("Total Inputs: ", total_inputs)

output_file = input("Enter the name of the output text file (e.g., combinations.txt): ")

all_combinations = []
for r in range(1, 6):  # Generate combinations of size 1 to 5
    combs = combinations(total_inputs, r)
    all_combinations.extend(combs)

# Write combinations to the output file
with open(output_file, 'w') as file:
    for combo in all_combinations:
        file.write(''.join(combo) + '\n')