def calcArea(shap,*dimntions):
    if(shap == 't'):
        triangleArea = .5*dimntions[0]*dimntions[1]
        print(f"triangleArea is: {triangleArea}")

    elif(shap == 'r'):
        RectangleArea = dimntions[0]*dimntions[1]
        print(f"RectangleArea is: {RectangleArea}")

    elif(shap == 's'):
        SquareArea = dimntions[0]*dimntions[0] #dimntions[0]*2
        print(f"SquareArea is: {SquareArea}")
    
    elif(shap == 'c'):
        pi=3.14
        CircleArea = pi*dimntions[0]**2
        print(f"CircleArea is: {CircleArea}")
    else:
        print("Please enter correct shap")

calcArea("t",4,5)
calcArea("c",4)
    
