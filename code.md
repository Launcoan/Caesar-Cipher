def clear():
    print(chr(27) + "[2J")
    
def caesarCipherDecode(sentence, leap):
    for thing in range(0, len(sentence)):
        if ord(' ') == ord(sentence[thing]):
            sentence = sentence.replace(' ', ' ')
        elif ord(sentence[thing]) - leap >= ord('a'):
            sentence = sentence[0: thing] + chr(ord(sentence[thing]) - leap) + sentence[thing + 1:]
        else:
            sentence = sentence[0:thing] + chr(ord('z') - (ord('a') - (ord(sentence[thing]) - leap)) + 1) + sentence[thing + 1:]
    return sentence
    
def caesarCipherEncode(sentence, leap):
    for thing in range(0, len(sentence)):
        if ord(' ') == ord(sentence[thing]):
            sentence = sentence.replace(' ', ' ')
        elif ord(sentence[thing]) + leap <= ord('z'):
            sentence = sentence[0:thing] + chr(ord(sentence[thing]) + leap) + sentence[thing + 1:]
        else: 
            sentence = sentence[0:thing] + chr(ord('a') + (ord(sentence[thing]) + leap) - ord('z') - 1) + sentence[thing + 1:]
    return sentence

def goodness(sentence):
    sum = 0
    for thing in sentence:
        if thing == 'a':
            sum += 0.0817
        if thing == 'b':
            sum += 0.0149
        if thing == 'c':
            sum += 0.0278
        if thing == 'd':
            sum += 0.0425
        if thing == 'e':
            sum += 0.1270
        if thing == 'f':
            sum += 0.0223
        if thing == 'g':
            sum += 0.0202
        if thing == 'h':
            sum += 0.0609
        if thing == 'i':
            sum += 0.0697
        if thing == 'j':
            sum += 0.0015
        if thing == 'k':
            sum += 0.0077
        if thing == 'l':
            sum += 0.0402
        if thing == 'm':
            sum += 0.0241
        if thing == 'n':
            sum += 0.0675
        if thing == 'o':
            sum += 0.0751
        if thing == 'p':
            sum += 0.0193
        if thing == 'q':
            sum += 0.0009
        if thing == 'r':
            sum += 0.0599
        if thing == 's':
            sum += 0.0633
        if thing == 't':
            sum += 0.0906
        if thing == 'u':
            sum += 0.0276
        if thing == 'v':
            sum += 0.0098
        if thing == 'w':
            sum += 0.0236
        if thing == 'x':
            sum += 0.0015
        if thing == 'y':
            sum += 0.0197
        if thing == 'z':
            sum += 0.0007
    return sum
    
def sentenceTester(encoded):
    words = []
    for thing in range(1, 27):
        why = caesarCipherDecode(encoded, thing)
        words.append(why)
    testing = 0
    word = ''
    for thing in words:
        if goodness(thing) > testing:
            testing = goodness(thing)
            word = thing
    return word
    
while True:
    print("Do you want to encode a message or decode a message?")
    if input() == 'encode':
        print("Enter message")
        message = input()
        print("Enter amount to increment by")
        step = int(input())
        print(caesarCipherEncode(message, step))
    else:
        print("Enter code")
        message = input().lower()
        clear()
        print(sentenceTester(message).upper())
        value = ord(sentenceTester(message)[0]) - ord(message[0])
        if value < 0:
            print('Leap: back ' + str(value * -1))
        elif value == 0:
            print('Leap: Did not change')
        else:
            print('Leap: forward ' + str(value))
