secret=7
guess=int(input("Guess a number :"))
if guess>secret:
        print("Too high")
elif guess<secret:
        print("Too Low")
else:
    print("Correct Guess!")

print("\nProgram Finished Successfully")
print("-----------------------------")
input("Press Enter to Exit...")
