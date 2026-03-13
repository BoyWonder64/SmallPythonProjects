"""Caesar Cipher Hacker, by Me
This program hacks messages encrypted with Caesar Cipher by doing
a brute force attack against every possible key
Try using Google to learn more, the more you learn the more you learn
- Some idiot who bought a billizion YT ad space"""

print('Caesar Cipher Hacker by Me')

# Let the user specify the message to hack:
print('Enter the encrypted Caesar cipher to hack.')
message = input('> ')

# Every possible symbol that can be encrypted/decryted:
# (This must match the SYMBOLS used when encrypting the message.)
SYMBOLS = 'ABCDEFGHIJKLMNOPQUSTUVWXYZ'

for key in range(len(SYMBOLS)): # for each key in the length of the symbol list above
    translated = '' # This will be the translated message
    
    # Decrypt each symbol in the message:
    for symbol in message: # Message was gathered from the user, symbol would be i in other cases
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol) # Get the number of the symbol
            num = num - key # Decrypt the number
            
            # Handle the wrap around if the num is less than 0:
            if num < 0:
                num = num + len(SYMBOLS)
                
            # Add decrypted number's symbol to translated:
            translated = translated + SYMBOLS[num]
            
        else:
            # just add the symbol without decrypting:
            translated = translated + symbol
    
    # Display the key being tested, along with its decrypted text:
    print('Key #{}: {}'.format(key, translated))
    
    # Test your knowledge
    
    # What error message if you delete the line that has translated = ''
        # Unbound local variable, and therefore you wont get your message
        
    # What happens if you change translated = translated + SYMBOLS[num] on line 33
    # to translated = translated + symbols
        # The message isnt encryted or decrypted
        
    # What happens if you enter an unencrypted message into the caesear cipher hacker program?
        # Then it prints out the message 25 times and its not needing to encrypt anything