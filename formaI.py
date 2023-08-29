for lin in range (9):
    for col in range(9):
        print((lin==col) * " *" , (lin!=col) * "  " , end="") 
    print()           
