import random
world_list=["finally","first","hello"]
chosen_world=random.choice(world_list)
guess=input("guess a letter\n").lower()
lives=6
display=[]

for letter in chosen_world:
    display+="_"
print(display)
end=False
while not end:
    guess=input("guess a letter\n").lower()
    for position in range(len(chosen_world)):
        letter=chosen_world[position]
        if letter==guess:
            display[position]=letter
            print(display)
        if guess not in chosen_world:
            lives-=1
        if lives==0:
            end=True
            print("you lose")
        if "_" not in display:
            end=True
            print("you win")
            #essalution44
