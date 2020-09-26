
import os

bezig1 = True

#Intro + Eeste vraag.
print("HALLO, en welkom! Ik ben Ryan en dit is mijn 'dit ben ik' opdracht.")
print("\nik heb 3 vragen inclusief deze")
print("Welke vraag wil je beantwoorden?")
while (bezig1 == True):
    antwoord1 = input("2 of 3?: ")
    if antwoord1 == ("2"):
        print("Mooi dan gaan we beginnenaan vraag 2!")
        break
    elif antwoord1 == ("3"):
        os.system("cls")
        print("Mooi dan gaan we beginnen aan vraag 3!")
        break
    else:
        os.system("cls")
        print("dit is geen geldig antwoord, probeer '2' of '3'")
        continue
    
#Tweede vraag.
while antwoord1 == "2":
    input("\nKlaar om te beginnen?\n: ")
    os.system("cls")
    break

while antwoord1 == "2":
    print("-----------------------------------------------------------")
    print("\nWelke kleur shirt heb ik aan?")
    print("A: Rood \nB: Grijs \nC: Blauw \nD: Hoe moet ik dit weten?")
    print("\n(let op GEBRUIK hooftletters)")
    antwoord2 = input(":")
    
#Tweede antwoord. (ROOD = antwoord)
    if antwoord2 == "A":
        os.system("cls")
        break
    elif antwoord2 == "B":
        os.system("cls")
        print("Nee, heb er niet veel van dus kleinste kans.")
        continue
    elif antwoord2 == "C":
        os.system("cls")
        print("Nee, wel een mooie kleur.")
        continue
    elif antwoord2 == "D":
        os.system("cls")
        print("Geen idee... het antwoord is rood.")
        continue
    else:
        os.system("cls")
        print("Dit was een simpel antwoord wat begrijp je niet aan A, B, C of D?")
        continue


#Derde vraag.
while antwoord1 == "B":
    input("\nOke denk je klaar te zijn voor de 3de vraag?\n: ")
    print("MOOI, denk ik... heb niet echt naar je geluisterd.")
    break

while antwoord1 == "3":
    print("-----------------------------------------------------------")
    print("\nOke de 3de vraag is: \nWat heb ik in mijn telefoon hoesje zitten?")
    print("A: Bankpas & ID \nB: ID & Speelkaart \nC: Pokémonkaart & bankpas")
    antwoord3 = input(":")
    
#Derde antwoord.
    if antwoord3 == "A":
        os.system("cls")
        print("Nee alleen de ID klopt, de bankpas kan soms wel erg handig zijn helaas.")
        continue
    elif antwoord3 == "B":
        os.system("cls")
        print("Ja inderdaad ik heb zelf niet echt een antwoord voor de speelkaart ('t is een ruiten 10)")
        break
    elif antwoord3 == "C":
        os.system("cls")
        print("Nee en waarom zou ik een pokémonkaart bij me hebben, wat is het 2013?")
        continue
    else:
        os.system("cls")
        print("Dit was een simpel antwoord wat begrijp je niet aan A, B of C?")
        continue
        
#Slot
while antwoord1 == "2" or "3":
    print("---------------------------------------------------------------------")
    print("\nOke dit was alles voor vandaag, tijd om te gaan!")
    antwoord4 = input("type ENTER voor het slot\n: ")
    
    if antwoord4 == "ENTER":
        print("\nWow je tickte het nog uit ook... nice")
        break
    elif antwoord4 == " ":
        print("\nJa je kunt ook gewoon enter in clicken waarom niet...")
        break
    elif antwoord4 == "enter":
        print("\nOke mooi, eigelijk met hooftleters, maar oké")
        break
    else:
        print("\nKom op je had letterlijk 1 ding in moeten type type het dan gewoon!")
        continue

print("\nEND")







