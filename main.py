import hashlib
import random
import string
import matplotlib.pyplot as plt
text = 'KravchenkoAntonAndriyovuch'
n = len(text)
symbols = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
def sha1_16(message):
    hash = hashlib.sha512(message.encode('utf-8')).hexdigest()
    #print('Hash:', hash[:-4] , ' | ' , hash [-4:])
    return hash[-4:]
def sha1_32(message):
    hash = hashlib.sha512(message.encode('utf-8')).hexdigest()
    print('Hash:', hash)
    return hash[-8:]
def random_message(message):
    i = random.randint(0, len(message) - 1)
    return message[:i] + random.choice(symbols) + message[i+1:]
def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))
    hash_var = sha1_16(text)
    hash_var1 = sha1_32(text)
def preimage_attack_1(mes):
    targetHash = sha1_16(mes)
    message = 0
    while True: 
        message += 1
        hash = hashlib.sha512((mes+str(message)).encode('utf-8')).hexdigest()
        #if int(message) < 31:
        #    print ((mes+str(message)), ' | ' , hash[:-4] , ' | ' , hash [-4:])
        #print(hash)
        if hash[-4:] == targetHash:
        #    print ((mes+str(message)), ' | ' , hash[:-4] , ' | ' , hash [-4:])
            return message
def preimage_attack_2(mes):
    message = mes
    targetHash = sha1_16(message)
    i = 0
    while True:
        candidat = random_message(message)
        state = sha1_16(candidat)
        if int(message) < 31:
            print ((mes+str(message)), ' | ' , hash[:-4] , ' | ' , hash [-4:])
        #temp = hashlib.sha512(candidat.encode('utf-8')).hexdigest()
        if state == targetHash:
            print ((mes+str(message)), ' | ' , hash[:-4] , ' | ' , hash [-4:])
            return candidat, i
        message = candidat
        i += 1
def birthday_attack_1():
    size = 10
    name = 'KravchenkoAntonAndriyovuch2002' + random_string(size)
    i = 0
    hashTable = {}
    message = random_message(name)
    hashh = sha1_32(message)
    for i in range(hashh):
        message = str(i)
        hash = hashlib.sha512(message.encode('utf-8')).hexdigest()
        if hash in hashTable:
            print('Message 1:', message)
            print('Message 2:', hashTable[hash])
            break
        else:
            hashTable[hash] = message
    print('Number of hashes computed:', len(hashTable), hashTable)

def birthday_attack_2():
    size = 10
    name = 'KravchenkoAntonAndriyovuch' + random_string(size)
    i = 0
    hashTable = {}
    while True:
        message = name + str(i)
        state = sha1_32(message)
        t = hashlib.sha512(message.encode('utf-8')).hexdigest()
        if state in hashTable:
            temp = hashTable[state]
            if temp == message:
                continue
            return state, hashTable[state], message, i
        hashTable[state] = message
        i += 1

def main():
    n = 1
    count = [i for i in range(n)]
    #iters = [preimage_attack_1(text+str(i)) for i in range(n)]           # first attack
    #M = sum(iters)/len(iters)
    #D = (1/len(iters))*sum([(i - M)**2 for i in iters])
    
    iters = [preimage_attack_2(text+str(i)) for i in range(n)]            # second attack
    M = sum([iters[i][1] for i in range (len(iters))])/len(iters)
    print(f'Meaning:{M}')
    D = (1/len(iters))*sum([(i[1] - M)**2 for i in iters])
    print(f'Dispersion:{D}')
    fig = plt.figure(figsize = (10, 5))
    plt.bar(count, [i[1] for i in iters], color = 'purple', edgecolor = 'darkblue', width = 0.8)
    plt.show()
main()
