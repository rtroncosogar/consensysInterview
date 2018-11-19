# ConsensysInterview
Here is my personal python snipet that was required from Viant Team

## What does this code do?

This code it's a python script that returns the transaction Hash and the Blockhash where the contract was created, you just need to provide the contract address and a valid infura API Secret.

## How to install:

There is some requirements that must be accomplished, some of thems are:

 * Python 3.7
 * web3py
 * pysha3
 
To install every single requirement, please before run:
 
 `pip install -r requirements.txt` 
 
 Structure:
 ```bash
 - code
   - main.py
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
Block: 0xblock_from_which_contract_was_deployed`
Transaction: 0xtransaction_with_which_contract_was deployed
```
  
 ## Sources:
 Some useful knowledge, that I've used to make this possible:
 
 * https://medium.com/@codetractio/inside-an-ethereum-transaction-fa94ffca912f
 * https://infura.io/docs
 * https://ethereum.stackexchange.com/questions/2531/common-useful-javascript-snippets-for-geth/3478#3478
 
 ## How could we improve the speed?
 
 Well, by now, I think it's smart to look at the blockchain from the last mined block, towards the origin of time. Cause, the last blocks will contain more transactions than the very first ones and that will increase the chance to find the bloock that you are looking for. Regarless of that, this version will start from the very first block until the last.
 
 In the future, I'll add some useful comments and test some optimization, but after the review (cause I try to preserve the esence of the challenge). 
 
 If you want to know something about this script, please feel free to wrtite me an email to rtroncosogar@gmail.com
 
 Any fork or pull request will be apreciated.
 
