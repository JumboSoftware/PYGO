# welcome to pygo's source code

startup_message = """

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pygo V1

Made by Jumbo
Owned by Jumbo

Welcome to Pygo, a Text Editor.

If you are new, please execute 'help' to get started.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

help = """

~~ IN TERMINAL

help - Returns List of Available Commands

pygo.start - Enter the Editor

pygo.end - Exit Pygo

~~ IN EDITOR:

pygo.exit - Exit the Edtor

pygo.save - Save the File


"""
# for terminal
terminal_name = 'v1.pygo@terminal:~$ '

modeList = """

r - Read File
	
	A new file will be generated if the file does not already exist.



a - Append Data to File
	
	A new file will be generated if the file does not already exist.
	
	
	
x - Create New File
	
	If the file already exists, the creation process will fail.


"""

# terminal
def PygoTerminal():
	print(startup_message)
	while True:
		cmd = input(f"{terminal_name}")
		if cmd == 'help':
			print(help_)
			continue
		# open editor
		elif cmd == 'pygo.start':
		  PygoEditor()
		  break
		# end session
		elif cmd == 'pygo.end':
			break
		# just something random dont worry about it
		elif cmd == '' or ' ':
			continue
		elif cmd == '  ' or '   ':
			continue
		else:
                        print('\nInvalid Command. Please use \'help\' if you are lost.\n')
			continue

# editor
def PygoEditor(*pygo_extensions):
	# for extensions
	extensions = [pygo_extensions]
	# select file
	global path
	path = input('\nENTER FILE PATH OR USE A FILE NAME FOR A LOCAL FILE: ')
	# choose mode
	print(modeList)
	global mode
	while True:
		mode = input('\nMODE: ')
		if mode == 'cancel':
			PygoTerminal()
		else:
			break
		# for invalid files
		if '.' not in path:
			print('\nFile must have an extension.')
			# return to terminal, this will be used some more
			PygoTerminal()
		else:
			file = open(f"{path}", f"{mode}")
			# this will hold the text
			global per_line
			per_line = '~  '
			global data
			data = ""
			# mode checking
			if mode == 'r':
				print(f.read())
				PygoTerminal()
			elif mode == 'a':
				while True:
					global text
					text = input(f'{per_line}' + '  ')
					# text and data are seperate variables so that every time the user enters a line of code, the text is added to the data variable along with a newline escape, otherwise, all of the text entered would be gathered into one line
					data += (text + '\n')
					# save file and return to terminal
					if text == 'pygo.save':
						data -= 'pygo.save'
						f.write(data)
						PygoTerminal()
						break
					elif text == 'pygo.exit':
						PygoTerminal()
						break
			# create new file
			elif mode == 'x':
				new_file_name = input('\nCREATE NEW FILE: ')
				new_file = open(f"{new_file_name}", 'x')
				print()
				PygoTerminal()
			else:
				print('\nInvalid Mode Choice.\n')
				PygoTerminal()

PygoTerminal()


# nothing else here 





