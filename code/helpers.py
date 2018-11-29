import rlp
import sys
import sha3


def getRightBlock(provider, address, currentBlockNumber):
    ''' This function returns the length of a parameters that returns the eth_Code,
        for reference: https://infura.io/docs/ethereum/json-rpc/eth_getCode '''
    return len(provider.eth.getCode(address, currentBlockNumber))



def outputData(provider, index):
    ''' This function is used to get the BlockHash and TransactionHash, it's separated
        just to make a cleaner code '''
    sys.stdout.write('Block: ' + str(provider.toHex(index['blockHash'])) + '\n')
    sys.stdout.write('Transaction: ' + str(provider.toHex(index['hash'])) + '\n')
    

def addressCalculator(provider, currentBlockNumber, attribute, address):
    ''' This function returns a candidate address, generated according the Ethereum specification,
        for  reference see: https://medium.com/@codetractio/inside-an-ethereum-transaction-fa94ffca912f'''
    count = 0
    for u in provider.eth.getBlock(currentBlockNumber, True)[attribute]:
        if count > 0:
            return True, currentDict            
        elif u['to'] == None:
            sender = bytes.fromhex(str(u['from']).replace('0x',''))
            currentContract = '0x' + str(sha3.keccak_256(rlp.encode([sender, u['nonce']])).hexdigest()[-40:])
            currentContract = provider.toChecksumAddress(currentContract)
            if currentContract == address:
                currentDict = u
                count += 1
