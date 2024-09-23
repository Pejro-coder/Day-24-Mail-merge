with open("invited_names.txt", "r") as data_file:
    names = data_file.readlines()

new_names = []
for name in names:
    stripped_name = name.strip()
    new_names.append(stripped_name)

with open("starting_letter.txt") as data_file:
    email = data_file.read()

for name in new_names:
    edited_email = email.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}.txt", "w") as data_file:
        data_file.write(edited_email)
