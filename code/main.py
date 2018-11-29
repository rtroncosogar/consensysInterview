import sys
import argparse
import helpers as hp
from web3 import Web3


def lookForBlockAndHashBlock(end_point, address):
    web3 = Web3(Web3.HTTPProvider(end_point))
    assert web3.isAddress(address), 'You have provide an invalid address'
    address = address.lower()
    if web3.isConnected() == True:
        address = web3.toChecksumAddress(address)
        find = 0
        i = hp.binarySeeker(web3.eth.blockNumber, web3, address) 
        if hp.blockSeeker(web3, address, i) > 0:
            state, index = hp.addressCalculator(web3, i, 'transactions', address)
            if state == True:
                find +=1
                hp.outputData(web3, index)
    else:
        sys.stdout.write('There is a problem with the conection' + '\n')

'''
        Below, is the argument parser
                                        '''

parser = argparse.ArgumentParser(description='A Python snipet that looks for the BlockHash and the TxHash, that belongs to a contract address.')
requiredNamed = parser.add_argument_group('Required named arguments')
requiredNamed.add_argument('contractAddress', metavar='ContractAddress', type= str, nargs=1, help='Here, you must provide the contract address')
requiredNamed.add_argument('-p', '--host', help='HTTP provider like: https://mainnet.infura.io/<API_SECRET>', required=True)
args = parser.parse_args()

lookForBlockAndHashBlock(args.host,sys.argv[1])
