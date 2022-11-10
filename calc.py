# Simple Allrounder Calculator
# Author: Sandro Zappulla
# Github: @SandroZappulla
# version: v1.0

# IMPORT
import os

# main
print("--- Simple Allrounder Calculator ---")
print("Bitte wählen Sie eine Rechenart aus:")
print("1. Grundrechenart (2 Zahlen)")
print("2. Zahlensystem umrechner")
main_selection = int(input())
os.system('cls')

# Grundrechenart
if main_selection == 1:
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")
    print("5. Modulo")
    print("6. Exponential")
    print("7. Quadratwurzel")
    grund_selection = int(input())
    
    # Addition
    if grund_selection == 1:
        print("Bitte gebe deine erste Zahl ein: ")
        number1 = float(input())
        print("Nun gebe deine zweite Zahl ein: ")
        number2 = float(input())
        addition = number1+number2
        print("Ergebnis: " + str(number1) + "+" + str(number2) + "=" + str(addition))
    
    # Subtraktion
    if grund_selection == 2:
        print("Bitte gebe deine erste Zahl ein: ")
        number1 = float(input())
        print("Nun gebe deine zweite Zahl ein: ")
        number2 = float(input())
        subtraktion = number1-number2
        print("Ergebnis: " + str(number1) + "-" + str(number2) + "=" + str(subtraktion))

    # Multiplikation
    if grund_selection == 3:
        print("Bitte gebe deine erste Zahl ein: ")
        number1 = float(input())
        print("Nun gebe deine zweite Zahl ein: ")
        number2 = float(input())
        multiplikation = number1*number2
        print("Ergebnis: " + str(number1) + "*" + str(number2) + "=" + str(multiplikation))

    # Division
    if grund_selection == 4:
        print("Bitte gebe deine erste Zahl ein: ")
        number1 = float(input())
        print("Nun gebe deine zweite Zahl ein: ")
        number2 = float(input())
        division = number1/number2
        print("Ergebnis: " + str(number1) + "/" + str(number2) + "=" + str(division))

    # Modulo
    if grund_selection == 5:
        print("Bitte gebe deine erste Zahl ein: ")
        number1 = float(input())
        print("Nun gebe deine zweite Zahl ein: ")
        number2 = float(input())
        modulo = number1%number2
        print("Ergebnis: " + str(number1) + "%" + str(number2) + "=" + str(modulo))

    # Exponential
    if grund_selection == 6:
        print("Bitte gebe deine erste Zahl ein: ")
        number1 = float(input())
        print("Nun gebe deine zweite Zahl ein: ")
        number2 = float(input())
        exponential = number1**number2
        print("Ergebnis: " + str(number1) + "^" + str(number2) + "=" + str(exponential))

    # Quadratwurzel
    if grund_selection == 7:
        print("Bitte gebe deine Zahl ein: ")
        number1 = float(input())
        wurzel = number1**0.5
        print("Wurzel aus: " + str(number1) + "=" + str(wurzel))

# Zahlensystem umrechner
if main_selection == 2:
    print("1. Von Dezimal nach Binär umrechnen")
    print("2. Von Binär nach Dezimal umrechnen")
    print("3. Von Hex nach Dezimal umrechnen")
    bin_selection = int(input())

    def getInput(base_value):
        input_raw = input()
        return int(input_raw, base=base_value)


    if bin_selection == 1:
        print("Wie lautet die Dezimal Zahl?")
        binarynumber = getInput(0)
        print("Die Binär Zahl lautet:", str(binarynumber))

    if bin_selection == 2:
        print("Wie lautet die Binär Zahl?")
        binarynumber = int(input(), base=2)
        decimalnumber = int(binarynumber, base=2)
        print("Die Dezimal Zahl lautet: ", decimalnumber)

    if bin_selection == 3:
        print("Wie lautet die Hex Zahl?")
        hexnumber = input()
        decimalnumber = int(hexnumber, base=16)
        print("Die Dezimal Zahl lautet: ", decimalnumber)
    



