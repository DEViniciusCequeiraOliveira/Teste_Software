posX = int(input("digite a posição X: "))
posY = int(input("digite a posição Y: "))

if posX > 0 and posY > 0:
    print("primeiro")
elif posX > 0 and posY < 0:
    print("quarto")
elif posX < 0 and posY < 0:
    print("terceiro")
elif posX < 0 and posY > 0:
    print("segundo")
else:
    print("")
