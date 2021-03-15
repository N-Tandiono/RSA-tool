import math

def encrypt(e, N, x):
    return pow(x, e) % N

def decrypt(d, N, y):
    return pow(y, d) % N

def stringToNumbers(string):
    numbers = ''
    for i in range(len(string)):
        num = ord(string[i]) - ord('A') + 1
        if (num < 10):
            numbers += f'0{str(num)}'
        else:
            numbers += str(num)
    return int(numbers)

def numbersToString(num):
    string = ''
    for i in range(0, len(str(num)), 2):
        curr = num[i] + num[i + 1]
        curr_letter = int(curr) + ord('A') - 1
        string += chr(curr_letter)
    return string

if __name__ =='__main__':
    while True:
        print("""\033[96m \033[1m
    RSA Tool
    1) RSA Encode
    2) RSA Decode
    3) String to Numbers
    4) Numbers to String
    \033[0m""")
        
        selection = int(input("Please select a number: "))
        if selection == 1:
            e = int(input("e (\033[91mco-prime of m\033[0m (m is: (p - 1) * (q - 1))): "))
            N = int(input("N (N is: p * q): "))
            string = input("String: ")
            x = int(stringToNumbers(string))
            print(f"\033[92mEncoded message: {encrypt(e, N, x)}\033[0m")

        elif selection == 2:
            d = int(input("d (inverse of e mod m): "))
            N = int(input("N (N is: p * q): "))
            encrypted_message = int(input("Encrypted Message: "))
            print(f"\033[92mDecoded message: {decrypt(d, N, encrypted_message)}\033[0m")

        elif selection == 3:
            string = input("String: ")
            print(f"\033[92mConverted to numbers: {stringToNumbers(string)}\033[0m")
            
        elif selection == 4:
            numbers = input("Numbers: ")
            if len(numbers) % 2 != 0:
                print(f"\033[91mInvalid Number. Please Try Again.\033[0m")
                continue
            print(f"\033[92mConverted to string: {numbersToString(numbers)}\033[0m")

        else:
            print("\033[93mSelection not recognised.\033[0m")
