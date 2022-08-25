import socket
import time

if __name__ == "__main__":

    # Define Connection
    ip = "169.254.106.66"
    port = 1234

    # Making Socket 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,port))

    # Select Smart Speaker's Voice Assistant Name
    """speaker_type = input("Insert Smart Speaker Type (Google,Alexa) :")
    if speaker_type.lower() == "google":
        text = "ok   google "
    elif speaker_type.lower() == "alexa":
        text = "hi   alexa "
    else:
        print("Please Insert Smart Speaker Type!!!")
        exit()"""

    # Sending Message    
    string = input("Enter message: ")
    #message = text + ", " + string
    message = "Hi . Alexa....., " + string + "....." 
    time.sleep(5)
    s.send(bytes(message,"utf-8"))
 
