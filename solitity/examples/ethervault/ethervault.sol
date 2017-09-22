contract Vault {

    address public owner;

   /**
     * @dev after this time in s the ether can be withdraw
     * 
     */
    uint public minStoreDurationInSeconds;

	function Vault() {
		owner = msg.sender;
		fundsStored = 0;
		numDeposits = 0;
	}

	function sendAssets(uint blockWithDrawlNumber) {
		Member newMember;
		newMember.addr = msg.sender;
		newMember.amount = msg.value;
		newMember.blockNumberDeposited = block.number;
		newMember.blockWithdrawlNumber = blockWithDrawlNumber;
		members[numDeposits] = newMember;
		numDeposits++;
		fundsStored = fundsStored + msg.value;
	}

	function retrieveAssets() { 
		for (uint i =0; i < numDeposits; ++i) {
			if (members[i].blockWithdrawlNumber >= block.number) {
				members[i].addr.send(members[i].amount);
				numDeposits--;
				fundsStored = fundsStored - msg.value;
			}
		}
	}
}
