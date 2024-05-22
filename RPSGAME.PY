import random
choose=("ROCK","PAPER","SCISSOR")
run=True

while run:
    player=None
    computer=random.choice(choose)
    while player not in choose:
        player=input("ENTER (ROCK PAPER SCISSOR)").upper()
    print(f"player:{player}")
    print(f"computer:{computer}")
        
    if player==computer:
        print("IT'S A TIE")
            
    elif player=="ROCK" and computer=="SCISSOR":
        print("YOU WIN!!!")
            
    elif player=="PAPER" and computer=="SCISSOR":
        print("YOU WIN!!!")
            
    elif player=="PAPER" and computer=="ROCK":
        print("YOU WIN!!!")
            
    else:
        print("YOU LOSE!!!")
            
    if not input("PLAY AGAIN? (Y/N): ").lower()=="y":
        run=False
            
print("THANKS FOR PLAYING")