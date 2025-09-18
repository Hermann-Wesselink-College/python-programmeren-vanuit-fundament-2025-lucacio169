# opdracht 1 en 2 van paragraaf 2.7

# opdracht 1
voornaam = input("wat is je voornaam?")
achternaam = input("wat is je achternaam?")
print("hallo" +" " +(voornaam +" " + achternaam))

#opdracht 2
naam = input("Voer de naam in: ")
straat = input("Voer de straatnaam in: ")
huisnummer = input("Voer het huisnummer in: ")
postcode = input("Voer de postcode in: ")
woonplaats = input("Voer de woonplaats in: ")

postcode = postcode.upper()
woonplaats = woonplaats.upper()

print("Adresgegevens")
print(naam)
print(straat + " " + huisnummer)
print(postcode + "  " + woonplaats)
