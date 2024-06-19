# Encode_The_Number
# You work in the message encoding department of a national security agency.
# Every message that is sent from or received in your office is encoded. 
# You have an integer N, and each digit of N is squared and the squares are concatenated together to encode the original number. 
# Your task is to find and return an integer value representing the encoded value of the number.
# input1: An integer value N representing the number to be encoded.
# Output:Return an integer value representing the encoded value of the number.
# Sample Input:


N = input()
string=''
for i in N:
    string+=str(int(i)*int(i))
print(string)