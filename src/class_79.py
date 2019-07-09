# def centered_average(arr):
#     arr.sort()

#     arr = arr[1:-1]

#     return sum(arr) // len(arr)


# def centered_average2(arr):
#     lowest = arr[0]
#     highest = arr[0]

# def centered_average3(arr):
#     arr.remove(min(arr))
#     arr.remove(max(arr))
#     return sum(arr) // len(arr)

# Rock Paper Scissors
import random

wins = 0
losses = 0
ties = 0
# build a REPL command loop
while True:
# Prompt player to input r/p/s 
    cmd = input("Type r/p/s -> ")
    # calc cpu move
    cpu_move = ["r", "p", "s"]
    # check for input validity
    if cmd == "r":
        if cpu_move == "r":
            # TIE
            ties += 1
            print(f"Computer picks {cpu_move}.  You tie")
        elif cpu_move == "p":
            # LOSE
            losses +=1
            print(f"Computer picks {cpu_move}.  You tie")
        elif cpu_move == "s":
            # WIN
            wins += 1
            print(f"Computer picks {cpu_move}.  You tie")
    elif cmd == "p":
        if cpu_move == "p":
            # TIE
            ties += 1
            print(f"Computer picks {cpu_move}.  You tie")
        elif cpu_move == "s":
            # LOSE
            losses +=1
            print(f"Computer picks {cpu_move}.  You tie")
        elif cpu_move == "r":
            # WIN
            wins += 1
            print(f"Computer picks {cpu_move}.  You tie")
    elif cmd == "s":
        if cpu_move == "s":
            # TIE
            ties += 1
            print(f"Computer picks {cpu_move}.  You tie")
        elif cpu_move == "r":
            # LOSE
            losses +=1
            print(f"Computer picks {cpu_move}.  You tie")
        elif cpu_move == "p":
            # WIN
            wins += 1
            print(f"Computer picks {cpu_move}.  You tie")
    elif cmd == "q":
        print("Goodbye!")
        break
    else:
        print("I did not understand that command.")
    # if player types q quit game
    # if input is not valid, print an error message and loop
# eval results based on comp command
print(f"{wins} - {losses} - {ties}")
# display result and score
# loop
