def opt1():
  print('you chose opt 1')

def opt2():
  print('you chose opt 2')

def opt3():
  print('you chose opt 3')

print('Welcome to the Presidential College Vote Simulator!')


option = 0

while (option != 3):
  print('Please choose an option:')
  print('\t 1. Run simulator')
  print('\t 2. Enter custom state')
  print('\t 3. Quit') 

  option = int(input('Enter the option: '))

  if option == 1:
    opt1()
  elif option == 2:
    opt2()
  elif option == 3:
    opt3()
    print('Goodbye!')
    exit()
  else: 
    print('error! enter the correct input')


