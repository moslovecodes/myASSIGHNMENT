first_name = input('Enter your first name: ')
last_name = input('Enter your second name: ')
age = int(input('Enter your Age: '))
current_year = int(input('Enter your current year: '))

earth_appearance = current_year - age

print(first_name+' '+last_name+' , you are '+ str(age) +' , you came to earth in year ' +str(earth_appearance)+' .')