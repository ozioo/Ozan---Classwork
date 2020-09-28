from random import randint
outputs=["draw","win","Loss"]
print(outputs[((int(input(print("0 for rock, 1 for paper, 2 for scissors"))) + (-(randint(0,2)))) % 3 )])

