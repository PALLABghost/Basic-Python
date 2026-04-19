print("""
start -to start the car
stop - to stop the car
quit - to quit
        """)
started =False
while True:
    user_input = input("> ").lower()
    if user_input == "start":
        if not started:
            print("Car started..Lets go")
            started = True
        else:
            print("Car already started")
    elif user_input == "stop":
        if not started:
            print("Car already stopped")
        else:
            print("Car stopped")
            started = False
    elif user_input == 'help':
        print("""
    start -to start the car
    stop - to stop the car
    quit - to quit
            """)
    elif user_input =="quit":
        print("Game End!!!")
        break
    else:
        print("I didn't understand that")
