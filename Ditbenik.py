
#Intro + Eeste vraag.
print("Hallo en welkom bij Dit-ben-ik!")
print("\nHeb je zin om een paar vragen te beantwoorden?")
antwoord1 = input("ja of nee?:")
if antwoord1 == ("ja"):
    print("Mooi dan gaan we beginnen!")
elif antwoord1 == ("nee"):
    print("Pech, we beginnen al!")
else:
    print("dit is geen geldig antwoord (of je hebt hooftletters gebruikt), maar we gaan alsnog door!")

#Tweede vraag.
input("\nKlaar om te beginnen?")
print("\nOke tijd voor de 1ste vraag!")
print("Welke kleur shirt heb ik aan?")
print("A: Rood \nB: Grijs \nC: Blauw \nD: Hoe moet ik dit weten?")
print("\n(let op GEBRUIK hooftletters)")
antwoord2 = input(":")

#Tweede antwoord.
if antwoord2 == "A":
    print("Zou best kunnen, Vind ze wel mijn mooiste shirts.")
elif antwoord2 == "B":
    print("Zou best kunnen, heb er niet veel van dus warschijnlijk niet.")
elif antwoord2 == "C":
    print("Zou best kunnen, wel een mooie kleur.")
elif antwoord2 == "D":
    print("ik heb daar eigelijk niet aan gedacht... VOLGENDE VRAAG!")
else:
    print("Dit was een simpel antwoord wat begrijp je niet aan A, B, C of D?")

#Derde vraag.
input("\nDenk je klaar te zijn voor de 3de vraag?")
print("MOOI, denk ik heb niet echt naar je geluisterd.")
print("\nOke de 3de vraag is: \nWat heb ik in mijn telefoon hoesje zitten?")
print("A: Bankpas & ID \nB: ID & Speelkaart \nC: Pokémonkaart & bankpas")
antwoord3 = input(":")

#Derde antwoord.
if antwoord3 == "A":
    print("Alleen de ID klopt, de bankpas kan soms wel erg handig zijn helaas.")
elif antwoord3 == "B":
    print("Ja inderdaad ik heb zelf niet echt een antwoord voor de speelkaart ('t is een ruiten 10)")
elif antwoord3 == "C":
    print("Nee en waarom zou ik een pokémonkaart bij me hebben, wat is het 2013?")
else:
    print("Dit was een simpel antwoord wat begrijp je niet aan A, B of C?")

#Slot
print("\nOke dit was de laatste vraag tijd om te gaan")
antwoord4 = input("type ENTER voor het slot")

if antwoord4 == "ENTER":
    print("\nWow je tickte het nog uit ook... nice")
elif antwoord4 == " ":
    print("\nJa je kunt ook gewoon enter in clicken waarom niet...")
elif antwoord4 == "enter":
    print("\nWow je tickte het nog uit ook, helaas zonder hooftleters")
else:
    print("\nKom op je had letterlijk 1 ding in moeten type type het dan gewoon!")
print("END")







