# Write a python code that converts temperatures to and from celsius, fahrenheit

def degree():
    print("Celcius")
    print("Fahrenheit")
    temp_unit = input("Enter the temperature unit: ")
    return temp_unit
# Check for the unit to be converted


def Fah_to_Cel(F):
    C = (F - 32) * 5/9
    return C

def Cel_to_Fah(C):
    F = (C * 9/5) + 32
    return F

def value():
    unit = degree()
    if unit == "Celcius":
        c = int(input("Enter degrees in celcius: "))
        print(str(c) + "C = " + str(Cel_to_Fah(c)) + "F")
    elif unit == "Fahrenheit":
        f = int(input("Enter degrees in Fahrenheit: "))
        print(str(f) + "F = " + str(Fah_to_Cel(f)) + "C")




value()
    
    

