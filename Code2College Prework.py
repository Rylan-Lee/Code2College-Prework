def user():
    name = input("Please enter your name: ")
    if name.lower() == "exit":
        print("Exiting now")
        return
    print("Hello", name, "!")

    username_age = input("Please enter your username and age: ")
    if username_age.lower() == "exit":
        print("Exiting now")
        return
    print("Thank you!")

    print("How may I assist you?")
    problem = input(
        "Please enter the number of the problem you have:\n"
        "Problem 1\n"
        "Problem 2\n"
        "Problem 3\n"
        "(Type 'Exit' to quit)\n> "
    )
    if problem == "exit":
        print("Exiting now")
        return

    print("Thank you for your response, we will try to fix your problem as soon as possible!")

user()