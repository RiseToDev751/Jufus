import os

def write(locale = None,device = None):
    if locale == None:
        print("[Writer] You must be select iso file")
    elif device == None:
        print("[Writer] You must be select target device")
    else:
        try:
            os.system(f"sudo dd if={locale} of={device} bs=4M status=progress") 
            print("[Writer] ISO succesfully writed")   
        except Exception as e:
            print(f"An error occured:\n{str(e)}")