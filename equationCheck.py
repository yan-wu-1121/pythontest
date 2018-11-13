def equalChecker(string): #function to check whether or not the string has a valid equal sign amount/position 
    equalAmount = string.count("=") #finds amount of equal signs 
    equalPos = string.find("=") #finds position of equal signs 
    if equalPos == -1: #checking if the equal sign exists or not
        print("Your equation has no equal sign.") #error handling for when it does not
        quit() #ends the program 
    elif equalAmount != 1: #checks if there is exactly one equal sign 
        print("You have an incorrect number of equal signs.") #error handling when there is an incorrect number of equal signs 
        quit() #ends the program 
    else:
        return equalPos #if all conditions have been satisfied then returns the position and the program can continue 

def xFinder(string): #function to find whether or not the string has single x and return its position 
    xPos = string.find("X") #finds the position of the x
    if xPos == -1: #checking if x exists or not
        return -1
    elif string.count("X") == 1:
        return xPos
    else:
        print("There are an incorrect number of xs in your equation.")
        quit() #ends the program 
        
def yChecker(string): #function to detect any errors with the y
    if string.find("Y") != 0: #checking if y exists and is in the correct position or not
        if string.find ("Y") == -1:
            return -1
        else:
            print("Your equation does not have a y in the correct position.")
            quit() #ends the program 
    else:
        return 0

def plusMinusFirst(string):
    if string.startswith("+"): 
        return True
    if string.startswith("-"):
        return True;
    else:
        return False

def divCheck(string):
    divAmount = string.count("/")
    divPos = string.find("/")
    if divAmount >= 2:
        print("You may have wrong division sign.")
        quit() #ends the program 
    if divAmount == 1:
        numberChecker(string[0:divPos])
        numberChecker(string[divPos+1:])
    else:
        numberChecker(string)


def numberChecker(string):
    dotAmount = string.count(".")
    dotPos = string.find(".")
    if dotAmount >2:
        print("You may have multiple dot in the number")
        quit() #ends the program 
    if dotAmount ==1:
        left = string[0:dotPos].strip()
        right = string[dotPos+1:].strip()
        if left.isdecimal() == False :
            print("Your Equation has the invalid object: " + string)
            quit() #ends the program 
        if left.isdecimal() == False :
            print("Your Equation has the invalid object: " + string)
            quit() #ends the program 
    elif string.isdecimal() == False :
            print("Your Equation has the invalid object: " + string)
            quit() #ends the program

def slopeConstant():
    inputer1 = input("Input first equation please: ") #gets user input for the equation
    sameCase = inputer1.upper() #changes input to uppercase to remove variation
    equation = sameCase.strip() #using a function to remove all spaces from the equation
    equalPos = equalChecker(equation) #using a function to check if there is an equal sign in the correct position in the equation
    
    leftSide = equation[0:equalPos].strip()
    rightSide = equation[equalPos+1:len(equation)].strip()
    if rightSide =="":
        print("Your equation has nothing on the right side.")
        quit() #ends the program 
    if leftSide == "Y":
        # Y on the left side, now handle right side: ax + b
        
        hasPlusMinus = plusMinusFirst(rightSide) 
        if hasPlusMinus :
            # remove first PlusMinus
            rightSide = rightSide[1:].strip()        
        
        xPos = xFinder(rightSide) 
        hasX = False
        if xPos >0 :
            m = rightSide[0:xPos].strip()
            divCheck(m)            
            hasX = True
        
        b = rightSide[xPos+1:].strip() 
        if len(b)>0:
            hasPlusMinus = plusMinusFirst(b) 
            if hasPlusMinus == False :
                if hasX:
                    print("need Plus or minues to connect B")
                    quit() #ends the program 
            else:
                # has PlusMinus
                b = b[1:].strip()
            divCheck(b)
            if hasX:
                
                return m, b
            else: 
                return 0,b
    elif leftSide == "X":
        # X on the left side
        
        hasPlusMinus = plusMinusFirst(rightSide) 
        if hasPlusMinus :
            # remove first PlusMinus
            b = rightSide[1:].strip()         
        else:
            b = rightSide         
        divCheck(b)
        return 0, b
    else:
        # didn't find X or Y on the left side
        print("Unkown left side symbol:" + leftSide)
        quit()

m1, b1 = slopeConstant()
m2, b2 = slopeConstant()

print (m1, b1)
print (m2, b2)

mFloater1 = float(m1)
bFloater1 = float(b1)
mFloater2 = float(m2)
bFloater2 = float(b2)

finalB = bFloater1 - bFloater2
finalM = mFloater2 - mFloater1
finalX = (finalB/finalM)
finalY = ((finalX*mFloater1) + bFloater1)
print("(%0.2f, %0.2f)"%(finalX, finalY))

