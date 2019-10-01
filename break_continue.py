apple = 10
while apple > 0:
    print("We have ", apple, " amount of apple")
    apple -= 1
    if apple == 5:
        continue
    else:
        print("Breaking")

print("We have ", apple, " amount of apple, now")
