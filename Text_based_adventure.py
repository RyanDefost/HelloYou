#-------------------------------------------------------------------------------------------
#Imports hier!:
import os
import time

#-------------------------------------------------------------------------------------------
#Introductie:
os.system("cls")
print("\n--------------------------------------------------------------------------------")
print("WELKOM!\n\nDit is mijn 'Text Based Adventure' en is gemaakt als een eind project voor leerjaar 1, piriode 1.")
print("\n Voor dat je begint:\n-Alle vragen beantwoord je met A/a of B/b\n-Er zijn 6 eindes met 2 varianten\n-Als je nog een keer speeld zie je dit niet meer")
input("\nAls je denkt dat je wil beginnen type iets\n:")


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
        if antwoord.lower() == "a":
                print("A2 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B2 werkt")
                return "A"
        else:
                print("fout2 werkt")
                return "C"


#defenitie vraag3
def def3(antwoord):
        if antwoord.lower() == "a":
                print("A3 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B3 werkt")
                return "B"
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


#defenitie vraag12b
def def12b(antwoord):
        if antwoord.lower() == "a":
                print("A12b werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B12b werkt")
                return "B"
        else:
                print("fout12b werkt")
                return "D"


#defenitie vraag13
def def13(antwoord):
        if antwoord.lower() == "a":
                print("A13 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B13 werkt")
                return "B"
        else:
                print("fout13 werkt")
                return "D"


#defenitie vraag14
def def14(antwoord):
        if antwoord.lower() == "a":
                print("A14 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B14 werkt")
                return "B"
        else:
                print("fout14 werkt")
                return "D"


#defenitie vraag15
def def15(antwoord):
        if antwoord.lower() == "a":
                print("A15 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B15 werkt")
                return "B"
        else:
                print("fout15 werkt")
                return "D"


#defenitie vraag16
def def16(antwoord):
        if antwoord.lower() == "a":
                print("A16 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B16 werkt")
                return "B"
        else:
                print("fout16 werkt")
                return "D"


#defenitie vraag17
def def17(antwoord):
        if antwoord.lower() == "a":
                print("A17 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B17 werkt")
                return "B"
        else:
                print("fout17 werkt")
                return "D"


#defenitie vraag18
def def18(antwoord):
        if antwoord.lower() == "a":
                print("A18 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B18 werkt")
                return "B"
        else:
                print("fout18 werkt")
                return "D"


#defenitie vraag19
def def19(antwoord):
        if antwoord.lower() == "a":
                print("A19 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B19 werkt")
                return "B"
        else:
                print("fout19 werkt")
                return "D"


#defenitie vraag20
def def20(antwoord):
        if antwoord.lower() == "a":
                print("A20 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B20 werkt")
                return "B"
        else:
                print("fout20 werkt")
                return "D"


#defenitie vraag21
def def21(antwoord):
        if antwoord.lower() == "a":
                print("A21 werkt")
                return "A"
        elif antwoord.lower() == "b":
                print("B21 werkt")
                return "B"
        else:
                print("fout21 werkt")
                return "D"
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
gamerunning = True
while gamerunning == True:
        
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
        vraag12b = False
        vraag13 = False
        vraag14 = False
        vraag15 = False
        vraag16 = False
        vraag17 = False
        vraag18 = False
        vraag19 = False
        vraag20 = False
        vraag21 = False
        Einde1A = False
        Einde1B = False
        Einde2A = False
        Einde2B = False
        Einde3A = False
        Einde3B = False
        Einde4A = False
        Einde4B = False
        Einde5A = False
        Einde5B = False
        Einde6A = False
        Einde6B = False     

        
#-------------------------------------------------------------------------------------------
        #Vraag 1 / input:
        while vraag1 == True:
                
                os.system("cls")
                print("BEEP! BEEP! BEEP!\nJe schrikt wakker, Je had weer een nachtmerrie. Dit was helaas niks nieuws en het ging altijd over het zelfde, vluchten, rennen, weg hier uit dit land.")
                print("\nVandaag is de dag, de dag dat je mee genomen zou worden voor het leger, dit was dan ook de reden waardoor je zovaak aan het vluchten dacht.")
                print("Maar wat zou je dan doen? ze zouden ieder moment aan je deur kunnen staan!")
                print("----------------------------------------------------------------")
                antwoord1 = input("\nWat zou je nu moeten doen?\nA: Ik besluit thuis te blijven\nB:Ik ga weg\n:")
                
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

                os.system("cls")
                print("Ja... waarom zou je rennen, niet dat je ver zou kunnnen kommen dat is gewoon absuurd om te denken.")
                print("----------------------------------------------------------------")
                antwoord2 = input("Je hebt nog oven de tijd voor ze hier zunnen zijn dus wat nu?\nA:Ik blijf nog even in bed liggen\nB:Ik wacht...\n:")

                if def1(antwoord1) == "A":
                        Einde6A = True
                        break
                elif def1(antwoord1) == "B":
                        Einde6B = True
                        break
                else:
                        continue

       
#-------------------------------------------------------------------------------------------
        #Vraag 3 /input:
        while vraag3 == True:

                os.system("cls")
                print("Je wilt weg, maar hoe? Hoe wil je dit land uit WAAR wil je heen???\nOke 1 ding tegelijk, waar ga je heen?")
                print("----------------------------------------------------------------")
                antwoord3 = input("Naar welk land ga je?\nA:een buurland\nB:Europa\n:")

                if def3(antwoord3) == "A":
                        vraag4 = True
                        landKeuze = ("als je naar een van de buurlanden wil dan zou je...\nJA dan zou je over de grens moeten")
                        break
                elif def3(antwoord3) == "B":
                        vraag4 = True
                        landKeuze = ("als je naar Europa wil dan zou je...\n met een boot moeten dus.. de haven!")
                        break
                else:
                        continue


#-------------------------------------------------------------------------------------------
        #Vraag 4 /input:
        while vraag4 == True:

                os.system("cls")
                print("Oke, Oke ", landKeuze, "\nJe hebt nu een locatie, maar er is nog zo veel wat je moet doornemen hier is alleen niet veel tijd voor.")
                print("----------------------------------------------------------------")
                antwoord4 = input ("Dus wat nu ga je nu gelijk weg of neem je het risico?\nA:Ik vertrekt omidelijk\nB:Ik risceer het en ga nog voorbereiden\n: ")

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
                vraag5 = True
                break


#-------------------------------------------------------------------------------------------
        #Vraag 10 /input:
        while vraag10 == True:

                os.system("cls")
                print("vraag10 werkt")
                print("Je gaat naar je vriend +Tip voor haven")
                vraag5 = True
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
        #Vraag 13 /input:
        while vraag13 == True:

                os.system("cls")
                print("vraag13 werkt")
                antwoord13 = input ("Je waarscuwd de man mee naar verzet helpen met verzet\nA:Ja\nB:Nee\n:")

                if def13(antwoord13) == "A":
                        Einde3A = True
                        break
                elif def13(antwoord13) == "B":
                        Einde3B = True
                        break
                else:
                        continue


#-------------------------------------------------------------------------------------------
        #Vraag 14 /input:
        while vraag14 == True:

                os.system("cls")
                print("vraag14 werkt")
                antwoord14 = input ("Je loopt snel door en besluit toch de bus te nemen\nA:haven\nB:grens\n:")

                if def14(antwoord14) == "A":
                        vraag11 = True
                        break
                elif def14(antwoord14) == "B":
                        vraag12 = True
                        break
                else:
                        continue

        
#-------------------------------------------------------------------------------------------
        #Vraag 11 /input:
        while vraag11 == True:

                os.system("cls")
                print("vraag11 werkt")
                print("je komt aan op de haven wat nu?")    
                if vraag10 == True:
                        print("A:Naar man van de Tip vraag10")      
                else:
                        print("B:Stiekem mee boot")
                print("C:Verder naar grens")
                
                antwoord11 = input(":")
                if def11(antwoord11) == "B":
                        vraag15 = True
                        break
                elif def11(antwoord11) == "C":
                        vraag12 = True
                        break
                elif def11(antwoord11) == "A":
                        vraag16 = True
                        break
                else:
                        continue


#-------------------------------------------------------------------------------------------
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
                        vraag17 = True
                        break
                elif def12(antwoord12) == "B":
                        vraag18 = True
                        break
                elif def12(antwoord12) == "C":
                        vraag12b = True
                        break
                else:
                        continue


#-------------------------------------------------------------------------------------------
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


#-------------------------------------------------------------------------------------------
        #Vraag 15 /input:
        while vraag15 == True:

                os.system("cls")
                print("vraag15 werkt")
                antwoord15 = input ("Welk ship ga je aanboord?\nA:Naar NL\nB:naar ?\n:")

                if def15(antwoord15) == "A":
                        Einde1A = True
                        break
                elif def15(antwoord15) == "B":
                        Einde1B = True
                        break
                else:
                        continue


#-------------------------------------------------------------------------------------------
        #Vraag 16 /input:
        while vraag16 == True:

                os.system("cls")
                print("vraag16 werkt")
                antwoord16 = input ("Je ziet 2 groepen bij een boot wie kies je?\nA:Rode boot \nB:Grote boot\n:")

                if def16(antwoord16) == "A":
                        Einde2A = True
                        break
                elif def16(antwoord16) == "B":
                        vraag19 = True
                        break
                else:
                        continue


#----------------------------------------------------------------------------------------
        #Vraag 17 /input:
        while vraag17 == True:

                os.system("cls")
                print("vraag17 werkt")
                antwoord17 = input ("Ze zien wie je bent en vragen wat waarom je niet naar het trainings kamp gaat.\nA:vertel een leugen\nB:Vertel de waarheid\n:")

                if def17(antwoord17) == "A":
                        vraag20 = True
                        break
                elif def17(antwoord17) == "B":
                        vraag21 = True
                        break
                else:
                        continue


#----------------------------------------------------------------------------------------
        #Vraag 18 /input:
        while vraag18 == True:

                os.system("cls")
                print("vraag18 werkt")
                antwoord18 = input ("Hoe er dan langs\nA:Met een vrachtwagen mee\nB:Verderop over het hek\n:")

                if def18(antwoord18) == "A":
                        Einde4A = True
                        break
                elif def18(antwoord18) == "B":
                        Einde4B = True
                        break
                else:
                        continue


#----------------------------------------------------------------------------------------
        #Vraag 19 /input:
        while vraag19 == True:

                os.system("cls")
                print("vraag19 werkt")
                antwoord19 = input ("Het blijkt politie te zijn ze komen, wat nu\nA:Rennen\nB:doe alsof je verdwaald bent\n:")

                if def19(antwoord19) == "A":
                        Einde2B = True
                        break
                elif def19(antwoord19) == "B":
                        Einde2A = True
                        break
                else:
                        continue


#----------------------------------------------------------------------------------------
        #Vraag 20 /input:
        while vraag20 == True:

                os.system("cls")
                print("vraag20 werkt")
                antwoord20 = input ("Welk leugen vertel je\nA:'Ik ben uitgezonden naar het buitenland\nB:'Ik weet van niks'\n:")

                if def20(antwoord20) == "A":
                        Einde5A = True
                        break
                elif def20(antwoord20) == "B":
                        Einde5B = True
                        break
                else:
                        continue


#----------------------------------------------------------------------------------------
        #Vraag 21 /input:
        while vraag21 == True:

                os.system("cls")
                print("vraag21 werkt")
                antwoord21 = input ("Je besluit de waatheid te vertellen ze proberen je aan te houden wat nu?\nA:Rennen\nB:Geef op\n:")

                if def21(antwoord21) == "A":
                        Einde6A = True
                        break
                elif def21(antwoord21) == "B":
                        Einde6B = True
                        break
                else:
                        continue


#----------------------------------------------------------------------------------------
        print("........................")
        os.system("cls")
        print("Wil je nog een keer proberen? [J/N]")
        eindvraag = input(":")

        if eindvraag.lower == "N":
                gamerunning = False
        else:
                continue
        
        







