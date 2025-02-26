# File management system

s = "This a sample string"

# Writing 

# with open("test.txt", 'w') as f:      # This is a context manager
#     f.write(s)

# same thing as above
fp = open("test.txt", 'a')
fp.write(s)
fp.close()

# Reading

with open("test.txt" , 'r') as f:
    str = f.read()
    print(str)