## Dezentralisierte Exchanages

# bestehend

# geplant

Airswap:

- Preisverhandlung:  Off-Chain, mit Orakel als Unterstütung
- Swap: On-Chain

Zu kompliziert, ICO im Oktober

https://swap.tech/whitepaper


## flatx, meine DX Exchange

* Rate A/B wird über Orakel bestimmt.
* Maker schickt alle A-Token mit Rate A/B und TTL in Block an Flatx Smartcontract
* Taker schickt seine Tocken innerhalb TTL
* Swap zu Rate A/B
* Token A gehen zu B und Token B zu A
* Überzählige Token werden zurückgesendet, an Maker oder Taker



## Vorteil:
* Keine Preisververhandlung nötig 
* Einfacher Smartcontract
* Kein Spread


## Nachteil:
* Ohne Liquitität funktioniert es schlecht
* Auch bei Nichterfüllung fallen Kosten für Smartcontract an
* Manipulierbar über Orakel
* Es können nur Token mit Ether oder Bitcoin Kursen gehandelt werden, dieser Muss in Rate A/B umgerechnet werden