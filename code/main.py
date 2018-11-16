import argparse
import rlp
import sha3
import sys
from web3 import Web3


parser = argparse.ArgumentParser(description='A Python snipet that looks for the BlockHash and the TxHash, that belongs to a contract address.')
requiredNamed = parser.add_argument_group('Required named arguments')
requiredNamed.add_argument('contractAddress', metavar='ContractAddress', type= str, nargs=1, help='Here, you must provide the contract address')
requiredNamed.add_argument('-p', '--host', help='HTTP provider like: https://mainnet.infura.io/<API_SECRET>', required=True)
args = parser.parse_args()


def lookForBlockAndHashBlock(end_point, address):
    web3 = Web3(Web3.HTTPProvider(end_point))
    assert web3.isAddress(address), 'You have provide an invalid address'
    if web3.isConnected() == True:
        address = address.lower()
        find = 0
        for i in range(web3.eth.blockNumber):
            if find > 0:
                break
            for u in web3.eth.getBlock(i, True)['transactions']:
                if u['to'] == None:
                    sender1 = bytes.fromhex(str(u['from']).replace('0x',''))
                    currentContract = '0x' + str(sha3.keccak_256(rlp.encode([sender1, u['nonce']])).hexdigest()[-40:])
                    if currentContract == address:
                        sys.stdout.write('Block: ' + str(web3.toHex(u['blockHash'])) + '\n')
                        sys.stdout.write('Transaction: ' + str(web3.toHex(u['hash'])) + '\n')
                        find +=1
                        break
        else:
            sys.stdout.write('There is a problem with the conection' + '\n')

lookForBlockAndHashBlock(args.host,sys.argv[1])
