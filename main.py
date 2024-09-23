#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt", "r") as data_file:
    names = data_file.readlines()

new_names = []
for name in names:
    stripped_name = name.strip()
    new_names.append(stripped_name)

with open("Input/Letters/starting_letter.txt") as data_file:
    email = data_file.read()

    baba = email.replace("Dear", "kala")
    print(baba)

for name in new_names:
    edited_email = email.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}.txt", "w") as data_file:
        data_file.write(edited_email)
