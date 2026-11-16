import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created By Mr Moi")
    while True:
        x = input("Enter what you want me to speak :")
        if x == "m":
            os.system("say Bye Bye Mr Moi")
            break
        command = f"say {x}"
        os.system(command)