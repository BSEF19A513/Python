car_start = False
while True:
    user_input = input(">")
    if user_input == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif user_input == "start":
        if car_start == False:
            print("Car started...Ready to go")
            car_start = True
        elif car_start == True:
            print("Car is already started")
    elif user_input == "stop":
        if car_start == True:
            print("Car stopped")
            car_start = False
        elif car_start == False:
            print("Car is already stopped")
    elif user_input == "quit":
        break
    else:
        print("I don't understand that...")