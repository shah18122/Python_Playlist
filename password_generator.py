import random

list = (0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','^','&','*','(',')')

password = ''

for i in range(12):
    password += str(random.choice(list))

site: str = input("Enter the site name: ")
print(password)

with open('passwords.txt', 'a') as file:
    file.write(site + ' : ' + password + '\n')  