def welcome():
 print('Welcome to our simple Calculator')
welcome()


def calculate():
    operation = raw_input('''
        Please type in the math operation you would like to complete:
        + addition
        - subtraction
        * multiplication
        / division
        
        ''')
    x = int(input('Enter your first number: '))
    y = int(input('Enter your second number: '))



    if operation == '+':
      print('{} + {} ='.format(x,y))
      print(x+y)

    elif operation == '-':
      print('{} -{} ='.format(x,y))
      print(x-y)

    elif operation == '*':
      print('{} * {} ='.format(x,y))
      print(x*y)

    elif operation == '/':
      print('{} / {} ='.format(x,y))
      print(x/y)
    else:
      print('You have not typed a valid operator,please run the program again!')
calculate()
#Add again () function to calculate () function
def again():
    calc_again = raw_input('''
        Do you want to calculate again?
        Please type Y for Yes or N for NO.
        ''')
    if calc_again.upper() == 'Y':
        calculate()
        again()
    elif calc_again.upper() == 'N':
        print('Thank you for using our simple calculator.')
    else:
        again()
again()











