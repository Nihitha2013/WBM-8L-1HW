file_read=open('Codingal.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

"""file_write=open('Codingal.txt','w')
file_write.write("File in write mode ....")
file_write.write("Hi! I am Penguin. I am 1 yr. old ")
file_write.close()"""

file_append=open('Codingal.txt','a')
file_append.write("\n File in append mode ....")
file_append.write("Hi! I am Penguin. I am 1 yr. old")
file_append.close()

file_read=open('Codingal.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_write=open('Sample.txt','w')
file_write.write("Hey Everyone....")
file_write.write("Welcome to the text file.")
file_write.close()

file_read=open('Sample.txt','r')
print("File in Read Mode-")
print(file_read.read())
file_read.close()

file_append=open('Sample.txt','a')
file_append.write("\n I am penguin ....")
file_append.write("I am 1 yr. old")
file_append.close()

file_read=open('Sample.txt','r')
print("File in Read Mode-")
print(file_read.read())
file_read.close()