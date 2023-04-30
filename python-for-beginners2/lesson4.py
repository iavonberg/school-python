writeMe = 'Example text'
saveFile = open('exampleWrite.txt', 'w')
saveFile.write(writeMe)
saveFile.close()

appendMe = 'Even more text'
saveFile = open('exampleFile.txt', 'a')
saveFile.write('\n')
saveFile.write(appendMe)
saveFile.close()

readMe = open('exampleFile.txt', 'r').read()
print(readMe)

readMe2 = open('exampleFile.txt','r').readlines()

print(readMe2)

class calc:

    def add(num1, num2):
        answer = num1+num2
        print(answer)

    def sub(num1, num2):
        answer = num1-num2
        print(answer)

    def mult(num1, num2):
        answer = num1*num2
        print(answer)

    def div(num1, num2):
        answer = num1/num2
        print(answer)

