p1 = input("Player 1! Rock Paper Scissors? ").upper()
p2 = input("Player 2! Rock Paper Scissors? ").upper()

if p1 == p2:
    print("\nDraw")

elif (p1 == 'ROCK' and p2 == 'PAPER') or (p1 == 'SCISSORS' and p2 == 'ROCK') \
     or (p1 == 'PAPER' and p2 == 'SCISSORS'):
    print("\nPlayer 2 wins")

else:
    print("\nPlayer 1 wins")
    
