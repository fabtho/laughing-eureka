# laughing-eureka

# economics

## target markets



## network
  ## personen
     ich hatte kurz kontakt mit dem typ von http://catch.info/. der war sehr nett. 
     
     
## technical
 
 

# tld

## .com
 
 this is the most important market in the domain business.
 
## .ch 
 
 possilbe test market, but almost no domain pro in switzerland

## .de
 
 its a market, but regulation entries are much higer then gtld. 
 
 ### whois for .de
 
 "Aus Datenschutzgründen können Informationen über Eigentümer von .de Domains nicht mehr wie früher über das whois-Protokoll abgefragt werden. Dies geht nur noch über eine mit einem Captcha gesicherte Webwhois-Seite, erreichbar über die Homepage[1] des DENIC." Source: https://de.wikipedia.org/wiki/Whois


# workflow

 - decision to buy domain
 - pay ether to smartcontract
 - seller unlocks domain
 - seller send auth code to buyer
 - buyer pulls domain with auth code to his registrar - ownership in registry changed
 - to sign ownership buyer set generated, secret hash to whois contact
 - smarcontract dedect this hash and pays seller


## different proof of ownership for domains

### whois

 the whois entry is mangend by the registry: 
 Source: https://whois.icann.org/en/primer, https://de.wikipedia.org/wiki/Whois

# lock/unlock

# transfer code

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
