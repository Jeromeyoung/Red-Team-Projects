import subprocess
# this python script is used to check for DNS Zone Transfers

def ns_identifier(domain):
	pipe1 = subprocess.Popen(('host', '-t', 'ns', domain), stdout=subprocess.PIPE)
	output = subprocess.check_output(('cut', '-d', " ", '-f', '4'), stdin=pipe1.stdout)
	output = output.decode('ascii')
	pipe1.wait()

	return output

def zone_transfer(nsserverlist, domain):
	for line in nsserverlist.splitlines():
		print(domain, line)
		try:
			output = subprocess.check_output(['host', '-l', domain, line], stderr=subprocess.STDOUT).decode('ascii')
		except subprocess.CalledProcessError as e:
			print(e.output.decode('ascii'))
	return output

domain = input("Enter the domain you wish to attempt zone transfers on: ") 
nameservers = ns_identifier(domain)
if domain:
	print("Here is a list of recognized name servers:\n"+ nameservers)
	print("Zone Transfer Results:\n" + zone_transfer(nameservers, domain))
else:
	print("You must specify a domain. Example: ./DNSTransferer.py megacorpone.com")

	

