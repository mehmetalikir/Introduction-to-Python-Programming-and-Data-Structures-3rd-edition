def encodeString(input_string):
    encodedString = ""
    for char in inputString:
        encodedString += str(ord(char)) + " "
    return encodedString.strip()

# Example usage:
inputString = "Hello, World!"
encodedString = encodeString(inputString)
print(encodedString)
