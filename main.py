import hashlib
import random
import string
import matplotlib.pyplot as plt
#text = 'KravchenkoAntonAndriyovuch'                    # first and second attack
text = 'KravchenkoAntonAndriyovuchFI04' 
n = len(text)
symbols = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
def sha1_16(message):
    hash = hashlib.sha512(message.encode('utf-8')).hexdigest()
    print('Hash:', hash[:-4] , ' | ' , hash [-4:])
    return hash[-4:]
def sha1_32(message):
    hash = hashlib.sha512(message.encode('utf-8')).hexdigest()
    print('Hash:', hash)
    return hash[-8:]
def random_message(message):
    res = message
    while res == message:
        i = random.randint(0, len(message) - 1)
        res = message[:i] + random.choice(symbols) + message[i+1:]
    return res
def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))
    hash_var = sha1_16(text)
    hash_var1 = sha1_32(text)
def preimage_attack_1(mes):
    targetHash = sha1_16(mes)
    message = 0
    while True: 
        message += 1
        hash = hashlib.sha512(((mes+str(message)).encode('utf-8'))).hexdigest()
        #if int(message) < 31:
        #    print ((mes+str(message)), ' | ' , hash , ' | ' , hash [-4:])
        if hash[-4:] == targetHash:
        #    print ((mes+str(message)), ' | ' , hash[:-4] , ' | ' , hash [-4:])
            return message
def preimage_attack_2(mes):
    message = mes
    targetHash = hashlib.sha512(message.encode('utf-8')).hexdigest()
    print(mes, ' | ' , targetHash[:-4] , ' | ' , targetHash[-4:])
    targetHash = targetHash[-4:]
    i = 0
    while True:
        candidat = random_message(message)
        state = hashlib.sha512(candidat.encode('utf-8')).hexdigest();
        #if int(i) < 31:
        #    print (i, ": ",candidat, ' | ' , state[:-4] , ' | ' , state[-4:])
        #temp = hashlib.sha512(candidat.encode('utf-8')).hexdigest()

        if state[-4:] == targetHash:
        #    print(candidat, ' | ' , state[:-4] , ' | ' , state[-4:])
            return candidat, i
        message = candidat
        i += 1
def birthday_attack_1(mes):
    name = mes
    i = 0
    hashTable = {}
    #message = random_message(name)
    message = name
    hashh = hashlib.sha512(message.encode('utf-8')).hexdigest()
    print(message, ' | ' , hashh[:-8] , ' | ' , hashh[-8:])
    hashh = hashh[-8:]
    i = 1
    while True:
        #message = str(i)
        hash = hashlib.sha512((mes+str(i)).encode('utf-8')).hexdigest()
        message = hash
        hash = hash[-8:]
        #if i < 31:
        #    print ((mes+str(i)), ' | ' , message , ' | ' , hash)
        if hash in hashTable:
            print('Message 1:', mes+str(i),hashlib.sha512(( mes+str(i)).encode('utf-8')).hexdigest() )
            print('Message 2:', hashTable[hash], hashlib.sha512((hashTable[hash]).encode('utf-8')).hexdigest() )
            break
        else:
            hashTable[hash] = mes+str(i)
            i += 1
        message = random_message(name)
    return i

def birthday_attack_2(mes):
    i = 0
    hashTable = {}
    message = mes
    while True:
        message = random_message(message) 
        state = hashlib.sha512(message.encode('utf-8')).hexdigest()
        #if i < 31:
        #    print (message, ' | ' , state[:-8] , ' | ' , state[-8:])
        if state[-8:] in hashTable:
            temp = hashTable[state[-8:]]
            if temp[1] != message:
                f = hashlib.sha512((temp[1]).encode('utf-8')).hexdigest()
            #    print("iter",temp[0], f[:-8] , ' | ' , f[-8:])
            #    print("iter", i , state[:-8] , ' | ' , state[-8:])
                break
        hashTable[state[-8:]] = i, message
        i += 1
    return i

def main():
    n = 100
    count = [i for i in range(n)]
    #iters = [preimage_attack_1(text+str(i)) for i in range(n)]           # first attack
    #M = sum(iters)/len(iters)
    #D = (1/len(iters))*sum([(i - M)**2 for i in iters])
    
    #iters = [preimage_attack_2(text+str(i)) for i in range(n)]            # second attack
    #M = sum([iters[i][1] for i in range (len(iters))])/len(iters)
    #D = (1/len(iters))*sum([(i[1] - M)**2 for i in iters])
    
    #iters = [birthday_attack_1(text+str(i)) for i in range(n)]          # third attack
    #M = sum([i for i in iters])/len(iters)  
    #D = (1/len(iters))*sum([(i - M)**2 for i in iters])
    
    iters = [birthday_attack_2(text+str(i)) for i in range(n)]             # fourth attack
    M = sum([i for i in iters])/len(iters)
    D = (1/len(iters))*sum([(i - M)**2 for i in iters])
    
    
    print(f'Meaning:{M}')
    print(f'Dispersion:{D}')
    fig = plt.figure(figsize = (10, 5))
    #plt.bar(count, [i for i in iters], color = 'purple', edgecolor = 'darkblue', width = 0.8)           # first attack
    #plt.bar(count, [i[1] for i in iters], color = 'purple', edgecolor = 'darkblue', width = 0.8)        # second attack
    #plt.bar(count, [i for i in iters], color = 'purple', edgecolor = 'darkblue', width = 0.8)           # third attack
    plt.bar(count, [i for i in iters], color = 'purple', edgecolor = 'darkblue', width = 0.8)            # fourth attack
    plt.show()
main()
