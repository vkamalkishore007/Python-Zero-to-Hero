#PROJECT :TO GENERATE A OTP
import random
import string
length= 7
otp= ''
characters = string.ascii_letters+ string.digits
for i in range(length):
  otp = otp + random.choice(characters)
print('OTP',otp)