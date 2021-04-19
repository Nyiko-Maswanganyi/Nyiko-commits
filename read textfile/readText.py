 

def file_reader():
 #The global keyword allows you to access any variable anywhere
 global s
 global arr
 arr = []
 fileR = open( "test.txt", "r")
 
#read word by word instead of line by line     
 for line in fileR:
      for word in line.split():
        arr.append(word.strip())             
#add every word or symbol in the text file to a list
 fileR.close()
 #close the read() resources
 

def welcomeUser():
    print("Welcome,input value: ")
    global element
    element=input()
    
    
def number_of_times(element,arr):
    print(arr)
    print(arr.count(element))
file_reader()
welcomeUser()
number_of_times(element,arr)


