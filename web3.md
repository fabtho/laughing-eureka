
## install

for ubuntu:
```
sudo apt-get install software-properties-common
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install ethereum
sudo apt-get install solc

```
## geth

start geth

```
geth
```


login from another terminal

```
geth attach
```

```
--syncmode "fast"   --cache 1024   
```


attach


```
personal.unlockAccount(web3.eth.accounts[0])
```

```
function checkAllBalances() {
  web3.eth.getAccounts(function(err, accounts) {
   accounts.forEach(function(id) {
    web3.eth.getBalance(id, function(err, balance) {
     console.log("" + id + ":\tbalance: " + web3.fromWei(balance, "ether") + " ether");
   });
  });
 });
};
checkAllBalances()
```
quelle: https://ethereum.org/cli#other-options


## private chain mit geth

unter /dev/m/myether/

```
mkdir data
```

custom-genesis.json:
```
{
    "config": {
        "chainId": 15,
        "homesteadBlock": 0,
        "eip155Block": 0,
        "eip158Block": 0
    },
    "difficulty": "0x1",
    "gasLimit": "2100000",
    "alloc": {}
}
```

```
geth init --datadir ./data custom-genesis.json
```

```
geth  --identity "myether" --rpc --rpcport "8000" --rpccorsdomain "*" --datadir "./data" --port "30304" --nodiscover --rpcapi "db,eth,net,web3" --networkid 1900 --nat "any" console```

Anleitung von hier:

https://medium.com/@balwant.matharu/starting-with-ethereum-dapps-development-environment-config-and-ide-92da7c214caf


einfach ohne get starten ohne --dev (see here https://github.com/ethereum/go-ethereum/issues/14352)

```
web3.personal.newAccount()
```

passwort für den account auf der private chain: Yeek4gee

address: 0x9c2adad72dcab6df4eab6f26f77dd372e3cdfa97

```
miner.setEtherbase('0x9c2adad72dcab6df4eab6f26f77dd372e3cdfa97');
miner.start(1)
```

```
miner.stop()
```

```
web3.eth.getBalance(web3.eth.accounts[0])
web3.eth.getBalance('0x9c2adad72dcab6df4eab6f26f77dd372e3cdfa97')
```

```
exit
```




