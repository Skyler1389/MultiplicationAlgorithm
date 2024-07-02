import random # random Modul implementiert die zufällige Generation von
              # Integers, um meine Funktion zu beweisen.
import time # time Modul um gebrauchte Zeit der Funktionsaufrufe zu erfassen.

# Projektvorgabe:

# Versuche eine Multiplikationsaufgabe mit 3 Faktoren (a * b * c) zu lösen,
# ohne die Multiplikation deiner Programmiersprache zu verwenden
# (also nicht in der Form: $erg = a * b * c;).
# Man sollte für a, b und c beliebige positive ganze Zahlen einsetzen können.

# Für dieses Projekt habe ich den offensichtlichen Weg der repetitiven
# Addition gewählt, basiert auf der Definition der Multiplikation. 
# Effizientere Multiplikations Algorithmen durch Bit-Shifting
# (bspw. Booth-Algorithmus) existieren zwar, diese liegen, nach mehreren 
# versuchten Implementationen, jedoch leider noch Außerhalb meiner Fähigkeiten.

def forLoopAddition(multiplicand:int, multiplier:int) -> int: # Nutzt eine 
                                        # Schleife zur kontinuierlichen Addition
    output = 0 # Initialisierung des Integers
    for _ in range(0, multiplier):
        output += multiplicand # Addiere n = Multiplikator mal den Multiplikant
                            # auf sich selbst
    return output

def multiply(a:int, b:int, c:int) -> int: # Nimmt a, b und c den Projekt-
                                    # Spezifikationen entsprechend entgegen
    return forLoopAddition(forLoopAddition(a, b), c) # Verwende die
            # forLoopAddition() Methode anstelle des Multiplikations-Operators

nIterations = 100 # Anzahl der zufälligen Multiplikationsaufgaben
lowestRandInt = 1 # Geringstmöglicher Faktor
highestRandInt = 1000 # Höchstmöglicher Faktor

t0 = time.time()

for iteration in range(0, nIterations): # Führe n = nIterations 
                                    # Multiplikationsaufgaben durch
    a = random.randint(lowestRandInt, highestRandInt)
    b = random.randint(lowestRandInt, highestRandInt)
    c = random.randint(lowestRandInt, highestRandInt)
    print(f"Result of multiplying {a}, {b} and {c} is = {multiply(a, b, c)}")
    assert(multiply(a, b, c) == a * b * c), f"Result of {a}, {b} and {c} is inaccurate!"
    # Löse eine Fehlermeldung aus und stoppe Ausführung, 
    # falls das Ergebnis der Funktion nicht dem erwarteten Wert (== false) entspricht

t1 = time.time() - t0 # Berechne Zeitaufwand

print(f"Time taken: {t1} seconds")