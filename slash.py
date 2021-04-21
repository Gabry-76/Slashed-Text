#<----------SLASH STAMP---------->
import pyfiglet
i = 1
while i < 500:
    stamp_20 = input("INSERISCI UNA STRINGA QUI > ")
    text = pyfiglet.figlet_format(stamp_20)
    if (stamp_20 == ''):
        print('INSERISCI UNA STRINGA VALIDA')
        continue
    if len(stamp_20) > 28:
        print('INSERISCI UNA STRINGA PIU\' CORTA')
        continue
    if (stamp_20 == 'stop'):
        print('IL CODE È STATO INTERROTTO!')
        break
    print(text)