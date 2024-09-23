def riktig_svar(n):
    print("Riktig! Så langt har du fått " + str(n) + " riktige svar.")

def feil_svar(n):
    print("Feil, svar. Du må nok ta grunnskolen om igjen. Så langt har du fått " + str(n) + " riktige svar.")


def sjekk_svar(svar, fasit, n):
    if svar == fasit:
        n += 1
        riktig_svar(n)
    else:
        feil_svar(n)
    return n