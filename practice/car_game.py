command = ""
started = False

# while command != "quit":
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print('Already started')
        else:
            started = True
            print('🚗 started...')
    elif command == "stop":
        if not started:
            print('Already stopped')
        else:
            started = False
            print("🚗 stopped.")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit
              ''')
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")
