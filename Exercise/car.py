while True:
    user_input = input(">")
    if user_input == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif user_input == "start":
        print("Car started...Ready to go")
    elif user_input == "stop":
        print("Car stopped")
    elif user_input == "quit":
        break
    else:
        print("I don't understand that...")