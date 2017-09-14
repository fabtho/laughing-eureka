

for ubuntu:
```
sudo apt-get install software-properties-common
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install solc
```
http://solidity.readthedocs.io/en/develop/installing-solidity.html

```
solc --bin --optimize --overwrite -o first.evm first.sol 
```
