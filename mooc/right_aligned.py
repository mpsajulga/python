string = str(input("Please type in a string: "))
length_string = len(string)
base_char = "*"
base_char_amount = 20
sub_base_from_len_string = base_char_amount - length_string
printed_base_char = base_char * sub_base_from_len_string 
print(f"{printed_base_char}{string}")