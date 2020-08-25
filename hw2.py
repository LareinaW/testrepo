#Wang, Qinruo

#Problem 1
def fibonacci_list(num):
    'Create a list of fibonacci sequence as a dictionary'
    n, a, b = 0, 0, 1
    L = []
    while n < num:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

def isInBasicFibonacci(x):
    'Determine whether inputs are in the list or not'
    if x in fibonacci_list(1000):
        return True
    else:
        return False
a = int(input())
print(isInBasicFibonacci(a))



#Problem 2

num1 = int(input())
num2 = int(input())
def Lcm(num1,num2):
    'Get the lowest common muliple of the inputs'
    if num1 < num2:
        num1,num2 = num1,num2
    for x in range(num2, num1*num2+1,num2):
        'the loop will continue during the range'
        if x % num1 == 0:
            return x

def Hcf(num1,num2):
    'Get the highest common factor of the inputs'
    if num1>num2:
        num1,num2=num2,num1
    for y in range(num1 , 1 ,-1):
        'the loop will continue during the range'
        if num1%y==0 and num2%y==0:
            return y

def LcmHcf():
    print("Hcf is "+ str(Hcf(num1,num2)))
    print("Lcm is "+ str(Lcm(num1,num2)))

LcmHcf()

#Problem 3

def listMult():
    'Create random numbers and seprate them by space'
    a= input("Enter number to create list").split()
    b = [int(a[i]) for i in range(len(a))]
    c = 0
    d = len(b)
    for i in b:
        c = c + i
        e = c/d
    new_list = [x * e for x in b]'to compute the product of average and number in the original list '
    print(new_list)

listMult()

#Problem 4

def newAvg():
    'Create a grade Tuple '
    a = input("Enter number to create list").split()
    b = [int(a[i]) for i in range(len(a))]
    print(b)
    b.sort()'Reorder the sequence from the lowest to the highest'
    print(b)
    c = b.pop(0)'Delete the lowest grade'
    print(b)
    d = 0
    e = len(b)
    for i in b:
        d = d + i
        f = d/e
    new_grade = f
    print(new_grade)

newAvg()

#Problem 5

 a = input()
 b = input()
 def areReverseOfEachOther(string1,string2):
     'Take these two strings as arguements'
     if string1[::-1] == string2:
         return True
     else:
         return False
 print(areReverseOfEachOther(a,b))

#Problem 6

def formattedPrint(list_str):
    max_count = max([len(x) for x in list_str])+2
    'print 2 extra * than the length of inputs'
    print("*"*max_count)
    for s in list_str:
        print("*%s"%(s), end='')
        'Convert inputs into string format'
        print(' '* (max_count-len(s)-2),end='')\
        'Take up the rest empty space '
        print('*')
    print("*"*max_count)

formattedPrint(['hello', 'world', 'in','a','frame'])

#Problem 7

a = str(input())
def translator(mystr):
    l = str.lower(mystr).split(' ')
     'lower capital letters to small letters'
    l = [x[1:]+x[0]+'ay' for x in l]
    res = [l[i] if i is not 0 else (str.upper(l[i][0])+l[i][1:]) for i in range(len(l))]
    'capitalize the first letter of the string '
    return ' '.join(res)
     'connect result by space'
print(translator(a))

#Problem 8

a =input()
b =input()
c =input()
d =input()
e =input()
import random
def randomPicks(a,b,c,d,e):
    tuzhu = [a,b,c,d,e]
    rand_list = random.randint(0,4)
    'Randomly pick one number from the list'
    print(tuzhu[rand_list])
randomPicks(a,b,c,d,e)

#Problem 9

def hangman(string):
    print("Welcome to Hangman!")
    gameMessage ={}
    gameMessage['lettersInWordGuessed'] =[]
    gameMessage['strikeCount'] = 0
    'Set original strikecount as zero'
    win = False
    'At beginning, the default result is lose'
    for i in range(8):
        'The times of attamptions cannot exceed 8'
        letter = input("Guess a letter:")
        if letter  in string:
            print("\"%s\" is in the word." % letter)
            'Convert inputs into string'
            gameMessage['lettersInWordGuessed'].append(letter)
        else:
            print("\"%s\" is not in the word." % letter)
            gameMessage['strikeCount'] += 1
            'A wrong guess adds on 1 to strikecount'
        print("Strike Count=", gameMessage['strikeCount'])
        if len(gameMessage['lettersInWordGuessed']) == len(string):
            print("Congratulations, you have won the game! The word is", string)
            win = True
            'The result of game is win only when the player meets the condition'
            break
    if not win:
        print("Sorry, you loss the game! The word is", string)

hangman("tag")
