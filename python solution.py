sol1:
def equilibrium(arr):
    sum1 = 0
    sum2 = 0
    n = len(arr)
    for i in range(n):
        sum1 = 0
        sum2 = 0
        for j in range(i):
            sum1 += arr[j]
        for j in range(i + 1, n):
            sum2 += arr[j]
        if sum1 == sum2:
            return i
    return -1
arr = [1,2,3]
print(equilibrium(arr))
sol 4:
word=input()
upper,lower,special=0,0,0
for ch in word:
    if ch.isalpha():
        if ch.isupper():
            upper+=1
        else:
            lower+=1
    else:
        special+=1
print("no of upper case letters",upper)
print("no of lower case letters",lower)
print("no of special cases",special)
sol6:
word=input()
reverse=word[::-1]
if word==reverse:
    print("palindrome")
else:
    print("not a palindrome")
sol5:
print("a".encode()[0])
or
w=input()
print(ord(w))
sol15:
word = input()
s = word.split()[::-1]
print(" ".join(s))
sol7:
word=input()
n=len(word)
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""
for i in range(n):
    if word[i] not in vowels:
        result = result + word[i]
print(result)
sol8:
w=input()
sum1=0
for i in w:
    if i.isdigit():
        sum1=sum1+int(i)
print(sum1)
sol11:
s1=input()
s2=input()
if(sorted(s1)== sorted(s2)):
    print(" anagrams.") 
else:
    print(" aren't anagrams.")
sol12:
w=input() 
n=len(w)
new=""
for i in range(0,n):   
    if w[i].islower():   
        new+= w[i].upper()  
    elif w[i].isupper():  
        new += w[i].lower()  
    else:  
        new+= w[i]          
print(new)
sol16:
num=int(input())
if num > 0:
    print("pos")
elif num == 0:
    print("Zero")
else:
    print("Neg")
if num % 2== 0:
    print("Even",num)
else:
    print("odd",num)
sol19:n = "1234"
sum = 0
for i in n:
    sum = sum + int(i)
print(sum)
