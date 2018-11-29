# ConsensysInterview
Here is my personal python snipet that was required from Viant Team

## What does this code do?

This code it's a python script that returns the transaction Hash and the Blockhash where the contract was created, you just need to provide the contract address and a valid infura API Secret.

## How to install:

There is some requirements that must be accomplished, some of thems are:

 * Python 3.7.0
 * web3py
 * pysha3
 
To install every single requirement, please before run:
 
 `pip install -r requirements.txt` 
 
 Structure:
 ```bash
 - code
   - main.py
   - helpers.py
 - LICENSE
 - README.md
 - requirements.txt
 ```
 
 
 Also, I highly recommend to create a virtualenv to test it.
 
 ## How to use:
 
 Once you have created the virtual env and installed the requirements, execute in terminal the following:
 
 `python PATH_TO_FOLDER/main.py 0xcontract_address_here --host https://mainnet.infura.io/<API_SECRET>`
 
 And you will recieve (after a while, dependent of the block number) the output:
 
```bash 
Block: 0xblock_from_which_contract_was_deployed
Transaction: 0xtransaction_with_which_contract_was deployed
```
  
 ## Sources:
 Some useful knowledge, that I've used to make this possible:
 
 * https://medium.com/@codetractio/inside-an-ethereum-transaction-fa94ffca912f
 * https://infura.io/docs
 * https://ethereum.stackexchange.com/questions/2531/common-useful-javascript-snippets-for-geth/3478#3478
 
 ## How do this work?
 
 Currently, I have made an implementation based in the well known "Binary Search" algorithm (you can see the code [here](https://github.com/rtroncosogar/consensysInterview/blob/master/code/helpers.py)), the aforamentioned implementaion was made in the function "binarySeeker" which provides a O(log n) computation time, making possible to find quickly the exact block where the contract was deployed. 

Once we have the block where the contract was deployed, the program seeks across that block for the transaction where the contract was created. To do that, as filter uses any transaction where the "to" parameter is null, which is an indicator of a contract creation, then computes the anddress that the contract will take and compares with the Address provided by the user, if the is coincidence, will return the Transaction Hash and the block Hash related to the contract.

  ## How can we improve the speed?
 
 In the current version, seems like we have found the optimal solution, but if you can provide any other approach, it will be very appreciated. So forks and pull request are very welcomed.

 If you have any doubt, please feel free to contact to me at rtroncosogar@gmail.com
 