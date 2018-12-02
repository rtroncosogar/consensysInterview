import rlp
import sys
import sha3

''' This is the function collecion used to accomplish the challenge,
    this code was separated just to improve the readbility of the main function 
'''


def outputData(provider, index):
    ''' This function is used to get the BlockHash and TransactionHash, it's separated
        just to make a cleaner code 
    '''    
    sys.stdout.write('Block: ' + str(provider.toHex(index['blockHash'])) + '\n')
    sys.stdout.write('Transaction: ' + str(provider.toHex(index['hash'])))
    

def blockSeeker(provider, currentBlockNumber, attribute, address):
    ''' Looks for the transaction Hash and block Hash inside the
        provided block 
    '''
    for u in provider.eth.getBlock(currentBlockNumber, True)[attribute]:        
        if u['to'] == None and addressCalculator(u, provider) == address:
            break
    return u


def addressCalculator(currentDict, provider):
    ''' This function returns a candidate address, generated according the Ethereum specification,
        for  reference, I highly reccomend to see: 
        https://medium.com/@codetractio/inside-an-ethereum-transaction-fa94ffca912f
    '''
    sender = bytes.fromhex(str(currentDict['from']).replace('0x',''))
    currentContract = provider.toChecksumAddress('0x' + str(sha3.keccak_256(rlp.encode([sender, 
                                                    currentDict['nonce']])).hexdigest()[-40:]))
    return currentContract
            

def binarySeeker(value, provider, address):
    ''' This function implements BinarySearch Algorithm to 
        seek the first main block, where the contract was deployed 
    '''
    first = 0
    last = value
    while first != last:
        midpoint = (first + last) // 2      
        if len(provider.eth.getCode(address, midpoint)) > 0:        
            last = midpoint
        else:
            first = midpoint + 1
    return first