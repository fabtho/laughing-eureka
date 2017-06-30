# laughing-eureka

# economics

## network
 ich hatte kurz kontakt mit dem typ von catch.at. der war sehr net
## technical

# workflow

 - desicion to buy domain
 - pay ether to smartcontract
 - seller unlocks domain
 - seller send auth code to buyer
 - buyer pulls domain with auth code to his registrar - ownership in registry changed
 - to sign ownership buyer set generated, secret hash to whois contact
 - smarcontract dedect this hash and pays seller


# lock/unlock

# transfere code

# possible whois api



# possible attack vectors

  ##  seller secret hash 
  
  ### desc
    everyone who obtain buyer secret hash can finalise contract, so the money should only go to sellers public key (eth address) or buyer public key (eth address). 
  ### mesurement  
    best would be to set this two eth address at initalisation of deal.
  ### side effects
   lost private key resulting in stuck ether in contract   
    
