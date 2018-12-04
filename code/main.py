import sys
import argparse
import helpers as hp
from web3 import Web3


def lookForBlockAndHashBlock(end_point, addressToSeek):
    ''' 
        This is the "Main" function of the challenge proposed by VIANT, it uses every
        function defined in the "helpers.py" in order to complete the task
        The challenge consist in using the infura's API and web3.py to
        create a python script capable to return the BlockHash and TransactionHash
        of the contract provided.

        This code usually takes 15 seconds (or less) to complete the task.
    '''
    web3 = Web3(Web3.HTTPProvider(end_point))
    addressToSeek = web3.toChecksumAddress(addressToSeek.lower())
    if not web3.isAddress(addressToSeek):
        sys.stdout.write('The address: ' + addressToSeek + ' is not an ethereum address.')
    elif not web3.isConnected():
        sys.stdout.write('Can not reach Infura with the host: ' + end_point)
    elif len(web3.eth.getCode(addressToSeek)) == 0:
        sys.stdout.write('Please, verify the current deployment state of the contract.')
    else:
        blockNumberOfTheContract = hp.binarySeeker(web3.eth.blockNumber, web3, addressToSeek) 
        index = hp.blockSeeker(web3, blockNumberOfTheContract, 'transactions', addressToSeek)
        hp.outputData(web3, index)


if __name__ == "__main__":
    ''' Below, is the argument parser
    '''
    parser = argparse.ArgumentParser(description = 'A Python snipet that looks for the BlockHash and the TxHash, that belongs to a contract address.')
    requiredNamed = parser.add_argument_group('Required named arguments')
    requiredNamed.add_argument('ContractAddress', type = str, help = 'Here, you must provide the contract address')
    requiredNamed.add_argument('-p', '--host', help = 'HTTP provider like: https://mainnet.infura.io/<API_SECRET>', required = True)
    args = parser.parse_args()

    lookForBlockAndHashBlock(args.host, args.ContractAddress)
