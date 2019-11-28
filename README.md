# Python-Keylogger
A simple proof of concept Python keylogger for Linux and Windows that uses the pynput module
No attempts are made at stealth, and for convenience the keylogger will close if the escape button is pressed. 

## WARNING
This code is for educational purposes only and should not (and honestly probably could not) be used maliciously. I take no responsibility for any misuse of this code by other parties. 

# Files

## keylogger.py
This is the keylogger that would be on the machine it is targeting. It gather a specified amount of input then sends it too the listening server as a base64 encoded string.  No effort is made to ensure the integrity of the data and if it fails to connect to the server it will continue sending new data anyway. 

## server.py
This is the server that receives the logged information and appends it to a log file. No effort is made to differentiate between clients although that would be trivial to implement. 
Data format is http://serverurl.com:port/data/BASE64PAYLOAD
