import sys
import argparse
import helpers as hp
from web3 import Web3


def lookForBlockAndHashBlock(end_point, address):
    web3 = Web3(Web3.HTTPProvider(end_point))
    if not web3.isAddress(address):
        sys.stdout.write('The address: ' + address + ' is not an ethereum address.')
    elif not web3.isConnected():
        sys.stdout.write('Can not reach Infura with the host: ' + end_point)
    elif len(web3.eth.getCode(address)) == 0:
        sys.stdout.write('Please, verify the current deployment state of the contract.')
    else:
        address = web3.toChecksumAddress(address.lower())
        i = hp.binarySeeker(web3.eth.blockNumber, web3, address) 
        index = hp.blockSeeker(web3, i, 'transactions', address)
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
