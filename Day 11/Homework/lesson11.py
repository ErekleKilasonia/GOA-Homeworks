ints = [1,3,6,14,16,34,4,7,43,23,12]         #1
print(ints[0]/ ints[1])
print(ints[3]/ints[5])
print(ints[2]/ints[6])
print(ints[4]/ints[7])
print(ints[8]/ints[9])

meanings = ["value", "list", "parentheses", "commas", "include", "refer", "acces", "permission"]       #2
meanings[1] = "mutable"
meanings[5] = "lime"
meanings[6] = "display"
meanings[2] = "output"
meanings[4] = "define"

print(meanings)   



drinks = ["Coca-Cola", "Fanta", "Sprite", "Pepsi"]                                                                                 #3

drink = int(input("""What Drink do you like from this list 
    Coca-Cola(0),
    Fanta(1), 
    Sprite(2), 
    Pepsi(3)
    : """))

print(drinks[drink])



