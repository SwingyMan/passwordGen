import string
import random
if __name__ == '__main__':
    print("How long password should be?")
    i =  input()
    randomised = string.ascii_letters+string.digits
    final = []
    for x in range(int(i)):
        final.append(random.choice(randomised))
    print("".join(final))