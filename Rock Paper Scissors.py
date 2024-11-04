import random
Score = [0,0,0]

Outcomes = {'Legend':["Win", "Tied", "Lose"],
                'Rock':[-2, 0, -1],
                'Paper':[1, 0, -1],
                'Scissors': [1, 0 , 2]}

Round = 1

while Round <= 10: 

    print(f'\nTurn {Round}')
    UserInput = input("Input 1, 2, or 3: ")

    #If the user wants to quit, they can input that
    #The final score will still be calculated
    if UserInput == "quit":
        break

    #Check to see if the input was valid
    if UserInput in ["1","2","3"]:


        #If input was valid, CPU generates a random number
        #1-3
        CPUInput = random.randint(1,3)

        #list(Outcomes.keys())[int(UserInput)]
        #This converts the keys in the Outcomes Dictionary to
        #A list which we then slice to the index of UserInput
        #or CPUInput
        UserKey = list(Outcomes.keys())[int(UserInput)]
        print(f'You input {UserKey}')
        CPUKey = list(Outcomes.keys())[CPUInput]
        print(f'CPU input {CPUInput}')

        total = int(UserInput) - CPUInput

        #Use the list trick used above to determine the index for the Legend to
        #Display the correct results to the user
        print(f'You {Outcomes["Legend"][Outcomes[UserKey].index(total)]} this round\n')

        #Based on the index of UserInput in Outcome and UserInput - CPUInput, return the correct
        #Index position to iterate that Score Index
        Score[Outcomes[UserKey].index(total)] += 1

        #Add 1 to Round to enter the next iteration
        Round += 1
    else:
        #Don't iterate, and ask user for valid input
        print('Please enter a valid input\n')

#Calculate final scores using the indexes of Score.
print(f'Final Score: {Score[0]} Wins, {Score[1]} Ties, {Score[2]} Loses')