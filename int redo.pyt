'''Module 3: Individual Programming Assignment 1
Thinking Like a Programmer
This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    encryption = ""
    for character in letter:
        if character == ' ': #if letter is a space, continue
            continue

        if character.isupper():
            character_index = ord(character) - ord ("A") #value of letter in terms of 0-25
            new_index = (character_index + shift) % 26 #shift, while the %26 loops it back, not sure how though
            new_unicode = new_index + ord("A") #get ASCII value for new letter
            new_character = chr(new_unicode) #get the letter from the ASCIII 
            encryption = encryption + new_character #gives the blank encryption a value
            return new_character

    else:
        return letter
            
my_answer = shift_letter ("M",2)
print (my_answer)

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    result = ""  
# transverse the plain txt  
    for i in range(len(message)):  
        char = message[i]  #kinda makes things like a list

        # encypt_func uppercase characters in plain txt  
        if (char.isupper()):  
            result += chr((ord(char) + shift - 64) % 26 + 65) 

        # encypt_func lowercase characters in plain txt  
        else:  
            result += chr((ord(char) + shift - 96) % 26 + 97)  
    return result  
# check the above function   

my_answer = caesar_cipher ("I LOVE ITMGT",2)
print (my_answer)

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    encryption = ""
    for character in letter:
        if character == ' ': #if letter is a space, continue
            continue

        if character.isupper():
            character_index = ord(character) - ord ("A") #value of letter in terms of 0-25
            letter_shiftval = ord(letter_shift) - ord("A") + 1#value of letter shift in terms of 0-25
            new_index = (character_index + letter_shiftval) % 26 #shift, while the %26 loops it back, not sure how though
            new_unicode = new_index + ord("A") #get ASCII value for new letter
            new_character = chr(new_unicode) #get the letter from the ASCIII 
            encryption = encryption + new_character #gives the blank encryption a value
            return new_character
    else:
        return letter
            
my_answer = shift_by_letter ("M","B")
print (my_answer)

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.
    Example:
    vigenere_cipher("A C", "KEY") -> "K A"
    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # Convert to ordinals.

    plain = [ord(k) for k in message]
    keywd = [ord(k) for k in key]

    # Expand the keyword to match the length of the plaintext.

    keywd = keywd * (len(plain)//len(keywd) + 1)

    # Do the shift and convert back to text.

    A = ord('A')
    cipher = ''.join( [chr(A + ((p+k)%26)) for p,k in zip(plain,keywd)] )
    return cipher

my_answer = vigenere_cipher ("MEOW","MO")
print (my_answer)