#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
    
with open("./mail_merge/input/Names/invited_names.txt") as name:
    names_list = name.read().splitlines()
    print(names_list)
    for name in names_list:
        with open(f"./mail_merge/Output/ReadyToSend/letter_for_{ name }.txt", "w") as list:
            with open("./mail_merge/input/Letters/starting_letter.txt") as letter:
                content = letter.read().replace("[name]", name)
            list.write(content)
    
    