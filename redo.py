#this is a quick remake of the original code with slightly better logic to work as a refesher for me

#shifts a single letter forward by a set amount
def shifter(x, no):
    #don't shift spaces
    if x == " ":
        return x
    #move the letter's ordinate forward by the shift amount
    x = ord(x) + no

    #if the new ordinate has passed z...
    if x > 122:
        #then check how much it has passed it (%) and then add that to the
        #ordiante of a (97)
        x = (x % 123) + 97

    return chr(x)

#applys the letter shifter to a sentence
def shifter_sentence(sentence, shift):
    sentence = "".join([shifter(i, shift) for i in list(sentence)])
    return sentence

#easy dictionary access to each letter goodness
goods = {'a': '.0817', 'b': '.0149', 'c': '.0278', 'd': '.0425', 'e': '.1270', 'f': '.0223', 'g': '.0202', 'h': '.0609', 'i': '.0697', 'j': '.0015', 'k': '.0077', 'l': '.0402', 'm': '.0241', 'n': '.0675', 'o': '.0751', 'p': '.0193', 'q': '.0009', 'r': '.0599', 's': '.0633', 't': '.0906', 'u': '.0276', 'v': '.0098', 'w': '.0236', 'x': '.0015', 'y': '.0197', 'z': '.0007'}

#sums the "goods" value for each letter in a sentence
def get_goodness(x):
    global goods
    x = sum([float(goods[i]) for i in list(x.replace(' ', ''))])
    return x


message = 'lqkp og cv gkijv da vjg bqq'

#applys the goodness checker to each shift of a sentence finding the highest value
#and saving the corresponding message
goodness = 0
output_message = ""
for i in range(26):
    message = shifter_sentence(message, 1)
    temp_goodness = get_goodness(message)
    print(round(temp_goodness, 2), message, sep = "\t")
    if temp_goodness > goodness:
        goodness = temp_goodness
        output_message = message
        
print(output_message)
