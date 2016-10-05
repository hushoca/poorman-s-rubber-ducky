#NAME : DIGISPARK KEYBOARD CODE CREATOR (digispark_converter.py)
#VERSION : 1.0
#AUTHOR : HUSEYIN HOCA
#DATE : 1 OCTOBER 2016
#DESCRIPTION: Feel free to modify and distrubute however you like
#this code is completely free to use and open sourced.
########################################################################
import sys
 
indicator = False;
arg = sys.argv;             #get arguments
arg_ = len(arg);            #get number of arguments
 
def convert_to_key(key):
	key = key.upper();      #turn into uppercase
	nkey = "KEY_"+key;      #turn into "KEY_A"
	return nkey
 
def process_line(str):  #function for processing lines of txt file
	str = str.replace("\n","");     #get rid of line breaks
	space_ = str.find(" ");         #find index of the first space
	length = len(str);              #get length of line
	command = str[0:space_].upper();#get command = from index 0 to index space_
	argument = str[space_+1:length] #get arg = from index space_ + 1 to index length of the line
	#PYTHON DOESNT HAVE SWITCH/CASE SO MANUALLY CHECK WITH IF:
	if command == "DELAY":
		newf.write("    DigiKeyboard.delay("+argument+");\n");
	elif command == "PRINT":
		ag = argument.replace("\"","\\\"");     #replace " with \"
		newf.write("    DigiKeyboard.println(\""+ag+"\");\n");
	elif command == "WIN":
		key = convert_to_key(argument)  
		newf.write("    DigiKeyboard.sendKeyStroke("+key+",MOD_GUI_LEFT);\n");
	elif command == "PRESS":
		key = convert_to_key(argument)
		newf.write("    DigiKeyboard.sendKeyStroke("+key+");\n");
	elif command == "CTRL":
		key = convert_to_key(argument)
		newf.write("    DigiKeyboard.sendKeyStroke("+key+",MOD_CONTROL_LEFT);\n");
	elif command == "ALT":
		key = convert_to_key(argument)
		newf.write("    DigiKeyboard.sendKeyStroke("+key+",MOD_ALT_LEFT);\n");
	elif command == "SHIFT":
		key = convert_to_key(argument)
		newf.write("    DigiKeyboard.sendKeyStroke("+key+",MOD_SHIFT_LEFT);\n");
	elif command == "COMBINE":
		keys = argument.split(" ")
		newf.write("    DigiKeyboard.sendKeyStroke(");
		rkeys = reversed(keys)
		for item in rkeys:
			newf.write("KEY_"+item.upper());
			if (item <> keys[len(keys)-1]) and (item <> keys[0]):
				newf.write("|")
			if item == keys[len(keys)-1]:
				newf.write(",")
		newf.write(");\n");
	elif str.upper() == "INDICATOR=TRUE":
		global indicator            #set indicator to global
		indicator = True;           #set global indicator variable to true
 
     
if arg_ <> 3:             #check if the argument count is not equal to 2
	print("USAGE: convert.py \"original_file_path\" \"new_file_path\"") #print instructions
else:                               #if argument count matches to 2 do the following:
	old_file_path = str(arg[1]);        #get file path of the txt file
	new_file_path = str(arg[2]);        #get path for the ino file to be created
                             
	oldf = open(old_file_path,"r"); #open the txt file
	newf = open(new_file_path,"w"); #open/create the ino file
 
	newf.write("#include \"DigiKeyboard.h\"\n\n");      #write
	newf.write("#define KEY_ALT (1<<2)\n");      #write
	newf.write("#define KEY_CTRL (1<<0)\n");      #write
	newf.write("#define KEY_SHIFT (1<<1)\n");      #write
	newf.write("#define KEY_WIN (1<<3)\n");      #write
	newf.write("#define KEY_TAB 43\n");      #write
	newf.write("#define KEY_DEL 76\n\n");      #write
	newf.write("void setup() {\n");                     #write
	newf.write("    pinMode(1, OUTPUT);\n");            #write
	newf.write("    pinMode(0, OUTPUT);\n");            #write
	newf.write("    DigiKeyboard.delay(1000);\n");      #write
	newf.write("    DigiKeyboard.sendKeyStroke(0);\n"); #write
	newf.write("    DigiKeyboard.update();\n");         #write
	newf.write("    DigiKeyboard.delay(100);\n");       #write
     
	for line in oldf:       #for each line in txt file do the following:
		process_line(line);
     
	newf.write("}\n\n");            #write
	newf.write("void loop() {\n");  #write
	if indicator == True:   #if indicator is true do the following:
		newf.write("    digitalWrite(1, HIGH);\n");     #write
		newf.write("    digitalWrite(0, HIGH);\n");     #write
		newf.write("    DigiKeyboard.delay(100);\n");   #write
		newf.write("    digitalWrite(1, LOW);\n");      #write
		newf.write("    digitalWrite(0, LOW);\n");      #write
		newf.write("    DigiKeyboard.delay(100);\n");   #write
	newf.write("}\n");                                  #write
     
	newf.close();   #close the arduino file
	oldf.close();   #close the txt file
     
	print "Converted successfully!" #let the user know that conversion is succesful
