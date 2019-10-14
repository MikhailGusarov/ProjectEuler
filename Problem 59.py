def encrypt(message, key):
    encrypted_message = []
    for i in range(len(message)):
        encrypted_message.append(chr(message[i] ^ key[i % len(key)]))
    return encrypted_message


with open('Problem 59 cipher.txt') as data:
    arr = data.readline().split(',')
arr = [int(i) for i in arr]
for i in range(ord('a'), ord('z') + 1):
    for j in range(ord('a'), ord('z') + 1):
        z = 112
        res = ''.join(encrypt(arr, [i, j, z]))
        if '$' not in res and '}' not in res and '#' not in res and '|' not in res:
            if '%' not in res:
                res_ascii = sum([ord(k) for k in (encrypt(arr, [i, j, z]))])
                print(res_ascii, [chr(i), chr(j), chr(z)], res)
