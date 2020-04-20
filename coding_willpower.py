# Willingness to learn using a scale range of 1 - 10
print("Rate your will power and programming on a scale of 1 - 10: ")
userWillpower = input("whats your willpower scale? ")
userSkill = input("whats your programming skill scale? ")

# Cast the user input to integers
willpower = int(userWillpower)
skill = int(userSkill)

# Sieve the grain and husks
if willpower and skill in range(6,11):
    # check for resilience
    answer = input("Are you sure you want to learn ways of the Jedi? ")
    response = answer.lower() # Cater for Upper / camel case input
    if response == 'yes':
        print('Are you willing to work harder? ')
        answer = input().lower() # Cater for Upper / camel case input
        if answer == 'yes':
            print("Welcome newbie Jeddi!")
        elif answer == 'no':
            print('Find your level')
    else:
        print("Come back when ready!")
       
