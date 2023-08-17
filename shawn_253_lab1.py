"""
#Lab Exercise 
#1: Demonstrate the use of Python data structures.
paragraph='''\nGood day to you !\nmy name is Shawn Biju Thomas from MCA and my register no is : 2347253\nThe domain i have chosen is ' 
Esports Team Management ' .\nMy domain basically deals with how an esports team is managed , for example ; Who are the players in each team , 
how many tournaments they have won etc , True or False , 3.14 '''
print(paragraph)
paragraphList = paragraph.split()


#COUNTING HOW MANY SPECIFIC WORDS ARE PRESENT
countOfSpecificWord=0
userInput=input("Enter a word : ")
for x in paragraphList:
    if userInput==x:
        countOfSpecificWord+=1
    else:
        pass
print(countOfSpecificWord)


#COUNTING HOW MANY LETTERS,DECIMALS,SPACES,SPEC CHARACTERS ARE PRESENT
countOfLetter=0
countOfInt=0
countOfSpecial=0
countOfSpace=0
for j in paragraph:
    if j.isdigit():
        countOfInt+=1
    elif j.isalpha():
        countOfLetter+=1
    elif j.isspace():
        countOfSpace+=1
    else:
        countOfSpecial+=1
print("Special characters : ", countOfSpecial)
print("Special decimals : ",countOfInt)
print("Special letters : ",countOfLetter)
print("Special Spaces : ",countOfSpace)


#TO PRINT DATATYPES ACCORDANCE TO STRING
n=input("\nEnter a word : ")

for word in paragraphList:
    if n in paragraphList:
        if n.isdigit():
            data_type = "int"
        elif n.replace('.', '').isdigit():
             data_type = "float"
        elif n.lower() == "true" or n.lower() == "false":
             if n[1:4].islower() and n[0].isupper():
                data_type = "bool"
             else:
                data_type="str"
        elif n.isalpha():
            data_type = "str"
        else:
            data_type = "Special Character"
    else:
        data_type="not found"

print("Word- ",n,"\t","|| Data Type-", data_type)



#ii)Sets and Tuples
domainSet={1,'TenZ','Sentinels',22,10000.0,True}
duplicatedomainSet = domainSet

print(domainSet.pop())     #the pop() method removes and returns a random element from the set.
print(domainSet)

domainSet.discard(1)       #the discard(x) method removes x from the set, but doesn't raise any error if x is not present in the set.
print(domainSet)

domainSet.clear()          #the clear() method removes all elements from a set
print(domainSet)

domainSet.update(('Shahzam','Shroud','Sinatraa','Dapr','HunterMims'))
print(domainSet)



newSetWithNumbers={12,24,123,42,1,42}
print(sorted(newSetWithNumbers))    #FOR ASCENDING ORDER
print(sorted(newSetWithNumbers,reverse=True))    #FOR DECENDING ORDER



# PROGRAM FOR PACKING AND UNPACKING IN TUPLE
domainTuple = (1,'TenZ','Sentinels',22,10000.0,True)        #this lines PACKS values

(id, name, team, age, cashPrize, active) = domainTuple  #this lines UNPACKS values

print(id)     #print Character name

print(*age)      #print age of player

#print(cashPrize)    #print the money he has won




inputChar=input("enter a character : ")
lettercount=0
TeamName=('s','e','n','t','i','n','e','l','s')
for char in TeamName:
    if char == inputChar:
        lettercount+=1
    else:
        pass
print("count of ",inputChar," is : ",lettercount)




newDomainName="Esports Team Management"
print(newDomainName[0:10])          #this is to print first 10 characters in the string
print(newDomainName[0:15:2])        #this is to print until the first 15 characters in the string but skipping every other character
print(newDomainName[::-1])          #this is to print the string in reverse order(good for checking palindrome)
print(newDomainName[-15:-5])        #this is to print the string in from negative index -15 unto  neg index -5


"""

# Sample dictionary
data = {'apple': 10, 'banana': 5, 'cherry': 15, 'date': 3}

# Sorting the dictionary in descending order of values using lambda function
sorted_data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

# Displaying the sorted dictionary
for key, value in sorted_data.items():
    print(f'{key}: {value}')

