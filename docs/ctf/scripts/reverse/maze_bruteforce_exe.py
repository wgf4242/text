import subprocess
import string
import time

charset = string.ascii_letters + string.digits + string.punctuation

def brute_force_exe():
    current_value = ''
    ii = 49  
    while True:
        for char in charset:
            attempt = current_value + char
            process = subprocess.Popen(['a.exe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, error = process.communicate(input=attempt)
            process.wait()  
            print(f"Trying: {attempt} - Response: {output.strip()}")
            last_char = output.strip()[-1]
            if chr(ii) == last_char:
                print(chr(ii))
                print(f"Found correct character: {char}")
                ii += 1 
                current_value += char 
                break  

            # time.sleep(0.1)

        #if  'win' in output:
        if len(current_value) > 0 and char == charset[-1] and last_char != chr(ii):
            print(f"Finished: The correct string is '{current_value}'")
            break

# 开始穷举
brute_force_exe()
