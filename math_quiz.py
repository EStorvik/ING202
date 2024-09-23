import time

from svar import sjekk_svar

# Velkommen til quiz om matematikk
print("Velkommen til quiz om matematikk")


riktige_svar = 0


# Vent 1 sekund
time.sleep(1)

t0 = time.time()
# Oppgave 1
svar1 = input("Hva er 2 + 2? ")
fasit1 = "4"

print("Sjekker svar 1 ...")
time.sleep(1)

riktige_svar = sjekk_svar(svar1, fasit1, riktige_svar)

# Oppgave 2
svar2 = input("Hva er 3 * 3? ")
fasit2 = "9"

print("Sjekker svar 2 ...")
time.sleep(1)
riktige_svar = sjekk_svar(svar2, fasit2, riktige_svar)

# Oppgave 3
svar3 = input("Hvilken matematiker har fått navnet sitt på konstanten e? Oppgi etternavn, første bokstav stor. ")
fasit3 = "Euler"

print("Sjekker svar 3 ...")
time.sleep(1)
riktige_svar = sjekk_svar(svar3, fasit3, riktige_svar)

# Total tid. Formatterer til 2 desimaler
t = time.time() - t0
t = round(t, 2)

print("Du brukte " + str(t) + " sekunder på quizen.")

# Oppsummering og poenggivning
print("Totalt fikk du " + str(riktige_svar) + " riktige svar og brukte " + str(t) +
      " sekunder på quizen. Det gir en score på " + str(round(riktige_svar * 100 / t, 2)) + " poeng.")