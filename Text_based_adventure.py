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
vraag9 = False
vraag10 = False
vraag11 = False
vraag12 = False
vraag13 = False
vraag14 = False
vraag15 = False
vraag16 = False
vraag17 = False
vraag18 = False
vraag19 = False
vraag20 = False
vraag21 = False
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


#defenitie vraag5i5
def def5i5(antwoord):
        if antwoord.lower() == "a":
                print("A5i5 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B5i5 werkt")
                return "B"
        else:
                print("fout5i5 werkt")
                return "C"


#defenitie vraag6
def def6(antwoord):
        if antwoord.lower() == "a":
                print("A6 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B6 werkt")
                return "B"
        else:
                print("fout6 werkt")
                return "C"


#defenitie vraag7
def def7(antwoord):
        if antwoord.lower() == "a":
                print("A7 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B7 werkt")
                return "B"
        else:
                print("fout7 werkt")
                return "C"


#defenitie vraag8
def def8(antwoord):
        if antwoord.lower() == "a":
                print("A8 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B8 werkt")
                return "B"
        else:
                print("fout8 werkt")
                return "C"


#defenitie vraag9
#def def9(antwoord):
        #Er is geen Def


#defenitie vraag10
#def def10(antwoord):
        #Er is geen Def



#defenitie vraag11
def def11(antwoord):
        if antwoord.lower() == "a":
                print("A11 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B11 werkt")
                return "B"
        elif antwoord.lower() == "c":
                print("C11 werkt")
                return "C"
        else:
                print("fout11 werkt")
                return "D"


#defenitie vraag12
def def12(antwoord):
        if antwoord.lower() == "a":
                print("A12 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B12 werkt")
                return "B"
        elif antwoord.lower() == "c":
                print("C12 werkt")
                return "C"
        else:
                print("fout12 werkt")
                return "D"



#-------------------------------------------------------------------------------------------
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
#Vraag 2 / input:
while vraag2 == True:
        print("vraag2 werkt")
        break

       
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
#Vraag 6 /input:
while vraag6 == True:

        os.system("cls")
        print("vraag6 werkt")
        antwoord6 = input ("Je gaat voorbereiden wat pak je eerst?\nA:paspoort pakken\nB:afscheid vriend\n:")

        if def6(antwoord6) == "A":
                vraag9 = True
                break
        elif def6(antwoord6) == "B":
                vraag10 = True
                break
        else:
                continue


#-------------------------------------------------------------------------------------------
#Vraag 9 /input:
while vraag9 == True:

        os.system("cls")
        print("vraag9 werkt")
        print("Je pakt je paspoort en gaat snel weg\n")
        vraag5i5 = True
        break


#-------------------------------------------------------------------------------------------
#Vraag 10 /input:
while vraag10 == True:

        os.system("cls")
        print("vraag10 werkt")
        print("Je gaat naar je vriend +Tip voor haven")
        vraag5i5 = True
        break


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


#-------------------------------------------------------------------------------------------
#Vraag 7 /input:
while vraag7 == True:

        os.system("cls")
        print("vraag7 werkt")
        antwoord7 = input ("Je besluit de bus te nemen waar ga je heen?\nA:De haven\nB:De grens\n:")

        if def7(antwoord7) == "A":
                vraag11 = True
                break
        elif def7(antwoord7) == "B":
                vraag12 = True
                break
        else:
                continue


#-------------------------------------------------------------------------------------------
#Vraag 8 /input:
while vraag8 == True:

        os.system("cls")
        print("vraag8 werkt")
        antwoord8 = input ("Je ziet iemand grafitie maken, maar er komt politie wat doe je?\nA:Waarschuw|nB:Niks\n:")

        if def8(antwoord8) == "A":
                vraag13 = True
                break
        elif def8(antwoord8) == "B":
                vraag14 = True
                break
        else:
                continue


#-------------------------------------------------------------------------------------------
#Vraag 11 /input:
while vraag11 == True:

        os.system("cls")
        print("vraag11 werkt")
        print("je komt aan op de haven\nA:Stiekem mee boot\nB: verder naar grens")
        if vraag10 == True:
                print("C:Naaar man van de Tip 'vraag10'")
        antwoord11 = input 

        if def11(antwoord11) == "A":
                vraag15 = True
                break
        elif def11(antwoord11) == "B":
                vraag12 = True
                break
        elif def11(antwoord11) == "C":
                vraag16 = True
                break
        else:
                continue


#Vraag 12 /input:
while vraag12 == True:

        os.system("cls")
        print("vraag12 werkt")
        print("Wat ga je doen bij de grens")
        if vraag9 == True:
                print("A:probeer over de grens te gaan.")
        else:
                print("B:Je hebt geen paspoort stiekem langs")
        print("C:Verder naar de haven")
        antwoord12 = input(":")

        if def12(antwoord12) == "A":
                vraag18 = True
                break
        elif def12(antwoord12) == "B":
                vraag19 = True
                break
        elif def12(antwoord12) == "C":
                vraag12b = True
                break
        else:
                continue


#Vraag 12b /input:
while vraag12b == True:

        os.system("cls")
        print("vraag12b werkt")
        print("je komt aan op de haven\nA:Stiekem mee met vracht schip")
        if vraag10 == True:
                print("B:Naar man van de Tip 'vraag10'")
        antwoord11 = input

        if def12b(antwoord12b) == "A":
                vraag15 = True
                break
        elif def12b(antwoord12b) == "B":
                vraag16 = True
                break
        else:
                continue



print("........................")
        







