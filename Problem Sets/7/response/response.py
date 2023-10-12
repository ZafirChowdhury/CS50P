import validator_collection

email = input("What's your email address? ")

try:

    flag = validator_collection.validators.email(email)

except(ValueError, validator_collection.errors.EmptyValueError):
    flag = False

if flag:
    print("Valid")

else:
    print("Invalid")