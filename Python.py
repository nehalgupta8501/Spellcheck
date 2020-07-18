speller={}     #empty

def load():    #to load all words in speller
    my_dictionary=open("dictionary.txt", 'r')
    for word in my_dictionary:
        word=word.lower()
        if word[0].lower() not in speller:
            speller[word[0]]=[]
        speller[word[0]].append(word.rstrip('\n'))
    for element in speller:
        print(element, speller[element])
    my_dictionary.close()

def input_para():
    para=input("enter paragraph: ")
    temp=Punctuation(para.lower())

    input_list=temp.split()
    return input_list

def check(input_list):
    count=0
    for word in input_list:
        if word in speller[word[0]]:
            print("correct")
        else:
            print("misspelled")
            count+=1
    print("count of misspelled words is : ", count)

def Punctuation(string):
    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in string:
        if x in punctuations:
            string=string.replace(x,"")
    return string

def main():
    load()
    input_list=input_para()
    check(input_list)
if __name__=="__main__":
    main()