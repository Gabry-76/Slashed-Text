#<----------SLASH STAMP---------->
import pyfiglet
import time
i = 1
while i < 500:
    stamp_20 = input("inserisci il testo: ")
    text = pyfiglet.figlet_format(stamp_20)
    if (stamp_20 == ''):
        print('Inserisci un testo valido.')
        continue
    if len(stamp_20) > 28:
        print("Il testo che hai inserito è troppo lungo,\ndigitane uno più corto.")
        continue
    if (stamp_20 == 'stop'):
        print("Vuoi uscire dall'esecuzione programma?")
        scelta=input("yes or no?\n:")
        if scelta == "yes" or scelta == "y":
            print("Chiusura in corso...")
            time.sleep(2)
            break
        else:
            pass
    print(text)
