import random



message=input("Enter any message and Santa will help you to hide it from others HO HO HO:")

list_input = []

for chars in message:
	if(chars == "a"):
		list_input.append(1)
	elif(chars == "/"):
		list_input.append(11)
	elif(chars == "b"):
		list_input.append(2)
	elif(chars == "c"):
		list_input.append(3)
	elif(chars == "h"):
		list_input.append(4)
	elif(chars == "p"):
		list_input.append(5)
	elif(chars == "t"):
		list_input.append(6)
	elif(chars == "2"):
		list_input.append(7)
	elif(chars == "4"):
		list_input.append(8)
	elif(chars == "5"):
		list_input.append(23)
	elif(chars == "0"):
		list_input.append(0)
	elif(chars == "P"):
		list_input.append(49)
	elif(chars == "F"):
		list_input.append(21)
	elif(chars == "N"):
		list_input.append(43)
	elif(chars == "n"):
		list_input.append(92)
	elif(chars == "L"):
		list_input.append(44)
	elif(chars == "s"):
		list_input.append(87)
	elif(chars == "S"):
		list_input.append(82)
	elif(chars == "."):
		list_input.append(26)
	elif(chars == "!"):
		list_input.append(13)
	elif(chars == "A"):
		list_input.append(33)
	elif(chars == "x"):
		list_input.append(63)
	elif(chars == "X"):
		list_input.append(19)
	elif(chars == "d"):
		list_input.append(19)
	elif(chars == "y"):
		list_input.append(45)
	elif(chars == "Y"):
		list_input.append(35)



pi_list=[3.14, 3.141, 3.1415, 3.14159, 3.141592, 3.1415926, 3.14159265, 3.141592653]

key_1=random.choice(pi_list)

phi_list=[1.61, 1.618, 1.6180, 1.61803, 1.618033,1.6180339, 1.61803398, 1.618033988, 1.6180339887]

key_2=random.choice(phi_list)


first_layer = []
for nums in list_input:
	first_layer.append(nums * key_1)

second_layer=[]
for nums in first_layer:
	second_layer.append(nums * key_2)
	

encrypted_message=[]
for nums in second_layer:
	encrypted_message.append(nums * key_1)

print(f"Encrypted message:{encrypted_message}")
