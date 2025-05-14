import math
import sys

def bereken_snelheid(afstand_km, uren):
    """
    Bereken de baansnelheid van een planeet op basis van de afstand tot de zon en de omlooptijd.
    """
    omtrek = 2 * math.pi * afstand_km  # Omtrek van de baan (cirkel)
    snelheid = omtrek / uren  # Snelheid in km/u
    return snelheid

def schrijf_naar_bestand(afstand_km, uren, snelheid):
    """
    Schrijft het resultaat naar een logbestand.
    """
    with open("snelheid_log.txt", "a") as bestand:
        bestand.write(f"Afstand: {afstand_km} km, Tijd: {uren} uur, Snelheid: {snelheid:.2f} km/u\n")

def main():
    if len(sys.argv) == 3:
        try:
            afstand_km = float(sys.argv[1])
            uren = float(sys.argv[2])
        except ValueError:
            print("Fout: Zorg ervoor dat de ingevoerde waarden getallen zijn.")
            sys.exit(1)
    else:
        # Standaardwaarden voor de aarde
        afstand_km = 150_000_000  # 150 miljoen km
        uren = 8766  # 1 jaar
    
    snelheid = bereken_snelheid(afstand_km, uren)
    print(f"De planeet beweegt zich met ongeveer {snelheid:.2f} km/u door de ruimte.")
    schrijf_naar_bestand(afstand_km, uren, snelheid)

if __name__ == "__main__":
    main()
