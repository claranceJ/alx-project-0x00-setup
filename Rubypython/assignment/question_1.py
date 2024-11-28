#Write a function reverse_string(s) that takes a string s and returns the reversed string.
#A slice bracket has three 'slots': Start, end, and step.
#[::-1] means: Start at the end (the minus does that for you), end when nothing's left and walk backwards by 1.
def reverse_string(s):
     return s [::-1]  #this is the slice bracket


my_reverse = reverse_string("MUM")
print(my_reverse)

