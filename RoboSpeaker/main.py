import os

if __name__ == '__main__' :
    print("Welcome to the RoboSpeaker")
    while True :
        x = input("What you went to say")
        if(x == "quit"):
            break
        command = f"say {x}"
        os.system(command)
    
   