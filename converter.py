# ------------------------------------------
# Unit Converter
# Author: Michael Murchie
#
# Features:
# - Convert centimeters to inches
# - Convert inches to centimeters
# - Convert kilograms to pounds
# - Convert pounds to kilograms
# - Convert kilometers per hour to miles per hour
# - Convert miles per hour to kilometers per hour
#
# Version: 1.0
# ------------------------------------------
def cm_to_inches(cm):
    return round(cm / 2.54, 2)

def inches_to_cm(inches):
    return round(inches * 2.54, 2)

def kg_to_lbs(kg):
    return round(kg * 2.20462, 2)

def lbs_to_kg(lbs):
    return round(lbs * 0.45359237, 2)

def km_to_mph(km):
    return round(km * 0.621371, 2)

def mph_to_km(mph):
    return round(mph * 1.60934, 2)

while True:
    print("\n" + "="*50)
    print("                CONVERSION MENU")
    print("1. Centimeters to inches")
    print("2. Inches to centimeters")
    print("3. Kilograms to pounds")
    print("4. Pounds to kilograms")
    print("5. Kilometers per hour to miles per hour")
    print("6. Miles per hour to Kilometers per hour")
    print("7. Exit")
    print("="*50)
    
    choice = input("Which unit of measurement would you like to use?(use number)" ).strip()
    try:
        if choice == "1":
            cm = float(input("Enter amount in centimeters: "))
            result = cm_to_inches(cm)
            print(f"{cm} cm = {result} inches")
            print()
        
        elif choice == "2":
            inches = float(input("Enter length in inches: "))
            result = inches_to_cm(inches)
            print(f"{inches} in = {result} cm")
            print()
        
        elif choice == "3":
            kg = float(input("Enter the weight in kilograms: "))
            result = kg_to_lbs(kg)
            print(f"{kg} kgs = {result} lbs")
            print()
    
        elif choice == "4":
            lbs = float(input("Enter the weight in pounds: "))
            result = lbs_to_kg(lbs)
            print(f"{lbs} lbs = {result} kgs")
            print()
        
        elif choice == "5":
            km = float(input("Enter the speed in kilometers per hour: "))
            result = km_to_mph(km)
            print(f"{km} km/h = {result} mph")
            print()
    
        elif choice == "6":
            mph = float(input("Enter the speed in miles per hour: "))
            result = mph_to_km(mph)
            print(f"{mph} mph = {result} km/h")
            print()
        
        elif choice == "7":
            print("Thanks for using the program! Goodbye!")
            break
        
        else:
            print("Invalid option! Try again!")
            
    except ValueError:
        print("Please enter a valid number!")    
 