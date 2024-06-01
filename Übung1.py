hourly_wage = input("Bitte gebe deinen Stundenlohn ein: ")
day = 8 * int(hourly_wage)
month = day * 20
year = month * 12
print("Dein Stundenlohn beträgt " + str(hourly_wage) + "€")
print("Du verdienst " + str(day) + "€ pro Tag")
print("Du verdienst " + str(month) + "€ pro Monat")
print("Du hast ein Jahresgehalt von " + str(year) + "€")
print("")
input("Bitte Beliebige Taste drücken...")
