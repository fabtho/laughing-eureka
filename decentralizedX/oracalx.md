## Dezentralisierte Exchanages

# bestehend

http://ubitok.io/products/

# geplant

RadarRelay:auf 0x

https://medium.com/@RadarRelay/comparing-token-marketplaces-3606ca8d780b

Airswap:

- Preisverhandlung:  Off-Chain, mit Orakel als Unterstütung
- Swap: On-Chain

Zu kompliziert, ICO im Oktober

https://swap.tech/whitepaper


## flatx, meine DX Exchange

* Rate A/B wird über Orakel bestimmt.
* Maker schickt alle A-Token mit Rate A/B und TTL in Block an Flatx Smartcontract
* Taker schickt seine Token innerhalb TTL
* Swap zu Rate A/B
* Token A gehen zu B und Token B zu A
* Nach dem TTL vom Maker werden die B Token ausbezahlt und allfällige überzählige A Token an den Maker zurückgesendet
* Nach dem TTL vom Taker werden die A Token ausbezahlt und allfällige überzählige B Token an den Maker zurückgesendet

## Vorteil:
* Keine Preisververhandlung nötig 
* Einfacher Smartcontract
* Kein Spread


## Nachteil:
* Ohne Liquitität funktioniert es schlecht
* Auch bei Nichterfüllung fallen Kosten für Smartcontract an
* Manipulierbar über Orakel
* Es können nur Token mit Ether oder Bitcoin Kursen gehandelt werden, dieser Muss in Rate A/B umgerechnet werden
