# 1
def read():
    print("1.Reading the file content")
    file=open("anudip.txt", 'r')
    content=file.read()
    print(content)
    file.close()

# 2    
def counting():
    print("2. Counting the number of letters in the text file")
    file=open("anudip.txt" , 'r')
    content=file.read()
    words=content.split()
    print("The total words are =" ,len(words))

# 3    
def uppercase():
    print("3. counting the uppercase letter in the textfile")
    file=open("anudip.txt",'r')
    content=file.read()
    alpha=[b for b in content if b.isupper()]
    print("The total uppercase letters are =", len(alpha))

# 4    
def read_lines():
    print('''4.to read lines from a text file 'story.txt',
and display those words, which are less than 4 characters''')
    file=open("anudip.txt" ,'r')
    content=file.readlines()
    for c in content:
        print(c)
    print("----Displaing the words less then four character------")
    words=c.split()
    for d in words:
        if len(d)<4:
            print(d)



read()
counting()
uppercase()
read_lines()
