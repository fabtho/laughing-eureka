# laughing-eureka

# economics

## target markets

## network
### personen

ich hatte kurz kontakt mit dem typ von http://catch.info/. der war sehr nett. 
     
     
## technical
 

# tld

## .com
 
this is the most important market in the domain business.

https://www.namecheap.com/support/knowledgebase/article.aspx/258/84/what-should-i-do-to-transfer-a-domain-from-namecheap

Policy on Transfer of Registrations between Registrars https://www.icann.org/resources/pages/policy-2012-03-07-en
 
## .ch 
 
possible test market, but almost no domain market in switzerland. But process off owner-change is much simpler then with .com domains. 

1. registrar change does not need agreement via mail. 
2. no grace periode 
3. No repayment for the domain is needed, is it free? (hexonet, no new fee has to be payed)
4. does a transfer look exist for .ch?

But:

  .ch domains have no Email-Field in whois!

## .de
 
 its a market, but regulation entries are much higer then gtld. 
 
 ### whois for .de
 
 "Aus Datenschutzgründen können Informationen über Eigentümer von .de Domains nicht mehr wie früher über das whois-Protokoll abgefragt werden. Dies geht nur noch über eine mit einem Captcha gesicherte Webwhois-Seite, erreichbar über die Homepage[1] des DENIC." Source: https://de.wikipedia.org/wiki/Whois
 
 But: whois entry about Tech-C is public via CLI


# workflow

 - decision to buy domain
 - pay ether to smartcontract
 - seller unlocks domain
 - seller send auth code to buyer
 - buyer pulls domain with auth code to his registrar - ownership in registry changed
 - to sign ownership buyer set generated, secret hash to whois contact
 - smarcontract dedect this hash and pays seller

## different proof of ownership for domain

### whois

 1. set password to whois entery, use organisation field
 2. set password via email, like lutnlilzhtzuz8oiuopmppue@plattform.com (.ch domains have no email field in whois!)

 the whois entry is mangend by the registry: 
 Source: https://whois.icann.org/en/primer, https://de.wikipedia.org/wiki/Whois

### via dns

set new dns delegation, then make DNS entry to proof ownership

# lock/unlock

# transfercode / auth code

## Exchange auth code

### over smart contract?

idea: to store auth code directly encrypted as value in the smart contract, payment is decrypting it, reincrypt it with the buyer privat key. Pitfall: We need the have it on the evm in clear text, everyhone can read it. Question: How long is a auth-code valid? Some system allow to set an arbitrary auth-code (hexonet does)

https://ethereum.stackexchange.com/questions/3442/using-ethereum-for-data-encryption

### via Mail offchain

# possible whois api

# possible attack vectors
##  seller secret hash 
  
### desc

everyone who obtain buyer secret hash can finalise contract, so the money should only go to sellers public key (eth address) or buyer public key (eth address).

### measurement  

best would be to set this two eth address at initalisation of deal.

### side effects

lost private key resulting in stuck ether in contract

    
## glossar

### registry
 a single company is responsible for the registry (Domain Owner Database) of a domain. this registries do not intaract with end users. different registrars (Domain-Name-Registrar) can change this entrys and sell domains to end users.


### address / public key
 this is a cryptocurrency address: its a public key. only people having the private key have access to funds. lost private key = lost funds

### gTLDs

 generic Top Level Domains
 https://en.wikipedia.org/wiki/Generic_top-level_domain

 
### CLI

Comand Line Interface. A text bassed Human/Computer interface. Als called shell
 
