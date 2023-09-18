import string
import random 
#we will use "random" module to shuffle our characters randomize
s1 = string.ascii_letters    #(s1 contains all ascii letters)
s2 = string.digits   #(s2 contains numeric numbers)
s3 = string.punctuation  #[s3 contains all punctuations(!"#$%)]

length = int(input("Enter your length:\n")) #asks password length from the user.
s = [] #create an empty list to add all above elements.
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))

random.shuffle(s) #shuffle the characters in our list randomly
print("Your password is:")
print("".join(s[0:length])) #choose the characters to print according to the length specified by user
                                       #and also concatenate the elements of list.
