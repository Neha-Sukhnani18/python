correct_email = "user@neha.com"
correct_password = "neha1234"

user_email = input("Kindly enter your email:")

if user_email == correct_email:
    user_password = input('Kindly enter your password:')

    if user_password == correct_password:
        print("You have logged in successfully!")
    else:
        print("incorrect password (re-check your password")
else:
    print("Your email cannot be found.")