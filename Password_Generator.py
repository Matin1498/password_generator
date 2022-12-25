import random
print("PASSWORD GENERATOR")
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = [0,1,2,3,4,5,6,7,8,9]

symbols = ['!','@','#','$','%','^','&','*','(',')',',','.','<','>','?','/',';',':','=','+','~']

q_letter = int(input("How many letters would you like in your password: "))
q_num = int(input("How many numbers would you like in your password: "))
q_sym = int(input("How many symbols would you like in your password: "))

password = ''
pass_list = []

for i in range(1, q_letter+1):
    pass_list.append(random.choice(letters))

for i in range(1, q_num+1):
    pass_list.append(random.choice(numbers))

for i in range(1, q_sym+1):
    pass_list.append(random.choice(symbols))

len = len(pass_list)

for i in range(len):
    ran = random.choice(pass_list)
    password += str(ran)
    pass_list.remove(ran)

print("\nYour new password is ready:")
print(password)
