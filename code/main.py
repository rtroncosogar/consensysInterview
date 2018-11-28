import argparse
import rlp
import sha3
import sys
from web3 import Web3




def getRightBlock(provider, address, currentBlockNumber):
    return len(provider.eth.getCode(address, currentBlockNumber))
    

def addressCalculator(provider, currentBlockNumber, attribute):
    for u in provider.eth.getBlock(currentBlockNumber, True)[attribute]:
        if u['to'] == None:
            sender = bytes.fromhex(str(u['from']).replace('0x',''))
            currentContract = '0x' + str(sha3.keccak_256(rlp.encode([sender, u['nonce']])).hexdigest()[-40:])
            currentContract = provider.toChecksumAddress(currentContract)
            return currentContract, u

def outputData(provider, index):
    sys.stdout.write('Block: ' + str(provider.toHex(index['blockHash'])) + '\n')
    sys.stdout.write('Transaction: ' + str(provider.toHex(index['hash'])) + '\n')


def lookForBlockAndHashBlock(end_point, address):
    web3 = Web3(Web3.HTTPProvider(end_point))
    assert web3.isAddress(address), 'You have provide an invalid address'
    if web3.isConnected() == True:
        address = web3.toChecksumAddress(address)
        find = 0
        for i in range(4203584, web3.eth.blockNumber):
            if find > 0:
                break
            elif getRightBlock(web3, address, i) > 0:
                currentContract, index = addressCalculator(web3, i, 'transactions')
                if currentContract == address:
                    outputData(web3, index)
                    find +=1
                    break
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
