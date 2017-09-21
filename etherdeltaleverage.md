
Etherdelta ist eine dezentralisierte Exchange die momentan für 10 prozent der Fee von Etherum aufkommt. Umsatzt pro tag ca 2'000'000 Fiat. https://coinmarketcap.com/exchanges/etherdelta/

Die Preise sind recht verzogen aeternity/ETH 

0.001600000 ETH liqui
0.001800000 ETH Etherdelta

Abweichungen ca 12%

Man könnte es automatisieren

- bei liqui kaufen
- zu withdraw zu Etherdelta 
- bei etherdelta verkaufen

Fees sind aber recht gross, die voreingestellten 4 gwei (Gas price) reichen nicht aus. Eine Interaktion mit Etherdelta kann schon $1 kosten. 40 gwei

https://www.reddit.com/r/EtherDelta/comments/6hrvwl/how_fees_work/

hier eine transaktionen

https://etherscan.io/tx/0x17c9b053ef570204285e9e25d899e3e83877382e0333802ce32f85402dbd605d
https://etherscan.io/tx/0x99aa2521b3fdc964adaa2c488cc19ef11ea15e367752004877a4578e6e660e6f

Etherdelta Kontrakt:

https://etherscan.io/address/0x8d12a197cb00d4747a1fe03395095ce2a5cc6819

Weiter Interaktionen durch mich: https://etherscan.io/address/0x092acb624b08c05510189bbbe21e6524d644ccad


deposit 0.75 ether from 0x092acb624b08c05510189bbbe21e6524d644ccad to etherdelta contract:
der code liegt in diesem repro: see: solitity/examples/etherdelta.sol

```
Function: deposit()

MethodID: 0xd0e30db0
```
https://etherscan.io/tx/0xd8a5241d9b073c8b513217965b66d7c8a8ec4eea1d993067014249152fdc6c50

dann habe ich 0.1 MKR gekauft und MKR withdraw gemacht. (über etherdelta contract)

Function: withdrawToken(address token, uint256 amount)

```
Function: withdrawToken(address token, uint256 amount)

MethodID: 0x9e281a98
[0]:000000000000000000000000c66ea802717bfb9833400264dd12c2bceaa34a6d (MKR crc20 token contract adress)
[1]:000000000000000000000000000000000000000000000000016345785d8a0000
```

MKR crc20 token contract adress: https://etherscan.io/address/0xc66ea802717bfb9833400264dd12c2bceaa34a6d

https://etherscan.io/tx/0x2875c5fc07d9b821f5527bef64ad4608843bdfd46e669c0ac9e8c78bf0e0c7c6


### Verkauf von Blackmoon BMC

1. Coin Übertragung (Token)  ($0.16) 8 Gwei

https://etherscan.io/tx/0x2666eee11179ccd8539f41b6b7b5b1e9bbcce03694ab99d1356ecaaabd89bfb2

```Function: approve(address _spender, uint256 _value)

MethodID: 0x095ea7b3
[0]:0000000000000000000000008d12a197cb00d4747a1fe03395095ce2a5cc6819
[1]:00000000000000000000000000000000000000000000000000000036173b5b80
```

2. Interaktion Smartcontract  ($0.18) 8 Gwei


https://etherscan.io/tx/0x0e390b2d9aff98e5b33df9156bb420404b99510cc491d2d0f4c1828539e863b0

```
Function: depositToken(address token, uint256 amount)

MethodID: 0x338b5dea
[0]:000000000000000000000000df6ef343350780bf8c3410bf062e0c015b1dd671
[1]:00000000000000000000000000000000000000000000000000000036173b5b80
```

3. signatur für bid




