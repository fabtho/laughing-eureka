
pragma solidity ^0.4.11;

/// @title

contract Salary{



    //do not send fees direclty, just withdraw:
    //use https://solidity.readthedocs.io/en/latest/common-patterns.html#withdrawal-from-contracts
    address feeaccount = 0x092Acb624b08C05510189BBbe21e6524D644CcAd;
    var fees = 1/1000

    // not allow dust as Salary
    if (msg.value < 100){
        throw;
    }
    
    function Salary {
        receiver = msg.data
   
    }
    
    function feeCalc(uint id){
        absfee = msg.value * fees;
        absamount = msg.value - absfee;
    }
    
    function public payable {
        Sent(msg.sender, feeaccount, absfee);
        Sent(msg.sender, receiver, absamount);
        or?
        msg.sender.send(feeaccount, absfee);

    }
    
    function () {
        throw; // throw reverts state to before call
    }
}
