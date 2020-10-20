#-------------------------------------------------------------------------------------------
#Imports hier!:
import os


#-------------------------------------------------------------------------------------------
#Alle vragen
vraag1 = True
vraag2 = False
vraag3 = False
vraag4 = False
vraag5 = False
vraag6 = False
vraag7 = False
vraag8 = False


#-------------------------------------------------------------------------------------------
#Introductie:
print("\n--------------------------------------------------------------------------------")
print("Dit is dan de introductie de plek waar je het verhaal opzet en informatie geeft aan de speler")
input("\n Dank je dat je kunt beginnen?\n:")


#-------------------------------------------------------------------------------------------
#Defenitie voor de eerste vraag / template voor aankomende vragen (TEXT VERANDERD NOG):
def def1(antwoord):
        if antwoord.lower() == "a":
                print("A werkt")
                return "A"
        elif antwoord.lower() == "b":
                return "B"
                print("B1 werkt")
        else:
                print("Fout1 werkt")
                return "C"


#-------------------------------------------------------------------------------------------
#Vraag 1 / input:
while vraag1 == True:
        
        os.system("cls")
        print("Tijd voor de eerste vraag!")
        antwoord1 = input("Wat ga je doen?\nA: ik bijf thuis\nB: ik ga weg\n\n:")
        
        if def1(antwoord1) == "A":
                vraag2 = True
                break
        elif def1(antwoord1) == "B":
                vraag3 = True
                break
        else:
                continue


#-------------------------------------------------------------------------------------------
#defenitie vraag2
def def2(antwoord):
        if antwoord.lower() == "A":
                print("A2 werkt")
                return "A"
        elif antwoord.lower() == "B":
                print("B2 werkt")
                return "A"
        else:
                print("fout2 werkt")
                return "C"

        
#-------------------------------------------------------------------------------------------
#Vraag 2 / input:
while vraag2 == True:
        print("vraag2 werkt")
        break

#-------------------------------------------------------------------------------------------
#defenitie vraag3
def def3(antwoord):
        if antwoord.lower() == "nederland":
                print("A3 werkt")
                return "A"
        elif antwoord.lower() == "engeland":
                print("B3 werkt")
                return "A"
        else:
                print("fout3 werkt")
                return "C"

       
#-------------------------------------------------------------------------------------------
#Vraag 3 /input:
while vraag3 == True:

        os.system("cls")
        print("vraag3 werkt")
        antwoord3 = input("Naar welk land ga je?\nNederland\nEngeland\n:")

        if def3(antwoord3) == "A":
                vraag4 = True
                break
        else:
                continue


#-------------------------------------------------------------------------------------------
#defenitie vraag4
def def4(antwoord):
        if antwoord.lower() == "a":
                print("A4 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B4 werkt")
                return "B"
        else:
                print("fout4 werkt")
                return "C"


#-------------------------------------------------------------------------------------------
#Vraag 4 /input:
while vraag4 == True:

        os.system("cls")
        print("vraag4 werkt")
        antwoord4 = input ("Waneer ga je vertrekken\nA: onmiddelijk\nB: eerst voorbereiden\n: ")

        if def4(antwoord4) == "A":
                vraag5 = True
                break
        elif def4(antwoord4) == "B":
                vraag6 = True
                break
        else:
                continue


#-------------------------------------------------------------------------------------------
#defenitie vraag4
def def4(antwoord):
        if antwoord.lower() == "a":
                print("A4 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B4 werkt")
                return "B"
        else:
                print("fout4 werkt")
                return "C"


#-------------------------------------------------------------------------------------------
#Vraag 4 /input:
while vraag4 == True:

        os.system("cls")
        print("vraag4 werkt")
        antwoord4 = input ("Waneer ga je vertrekken\nA: onmiddelijk\nB: eerst voorbereiden\n: ")

        if def4(antwoord4) == "A":
                vraag5 = True
                break
        elif def4(antwoord4) == "B":
                vraag6 = True
                break
        else:
                continue


#-------------------------------------------------------------------------------------------
#defenitie vraag4
def def4(antwoord):
        if antwoord.lower() == "a":
                print("A4 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B4 werkt")
                return "B"
        else:
                print("fout4 werkt")
                return "C"


#-------------------------------------------------------------------------------------------
#Vraag 4 /input:
while vraag4 == True:

        os.system("cls")
        print("vraag4 werkt")
        antwoord4 = input ("Waneer ga je vertrekken\nA: onmiddelijk\nB: eerst voorbereiden\n: ")

        if def4(antwoord4) == "A":
                vraag5 = True
                break
        elif def4(antwoord4) == "B":
                vraag6 = True
                break
        else:
                continue


#-------------------------------------------------------------------------------------------
#defenitie vraag4
def def4(antwoord):
        if antwoord.lower() == "a":
                print("A4 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B4 werkt")
                return "B"
        else:
                print("fout4 werkt")
                return "C"


#-------------------------------------------------------------------------------------------
#Vraag 4 /input:
while vraag4 == True:

        os.system("cls")
        print("vraag4 werkt")
        antwoord4 = input ("Waneer ga je vertrekken\nA: onmiddelijk\nB: eerst voorbereiden\n: ")

        if def4(antwoord4) == "A":
                vraag5 = True
                break
        elif def4(antwoord4) == "B":
                vraag6 = True
                break
        else:
                continue


#-------------------------------------------------------------------------------------------
#defenitie vraag5
def def5(antwoord):
        if antwoord.lower() == "a":
                print("A5 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B5 werkt")
                return "B"
        else:
                print("fout5 werkt")
                return "C"


#-------------------------------------------------------------------------------------------
#Vraag 5 /input:
while vraag5 == True:

        os.system("cls")
        print("vraag5 werkt")
        antwoord5 = input ("Hoe ga je weg\nA: Bus\nB: Rennen\n: ")

        if def5(antwoord5) == "A":
                vraag7 = True
                break
        elif def5(antwoord5) == "B":
                vraag8 = True
                break
        else:
                continue

print("........................")
        







