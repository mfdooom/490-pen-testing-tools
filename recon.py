import string
import subprocess 

def get_DNS_servers(website):
    subprocess.call("whois %s > temp.txt" % website, shell=True)

    with open("temp.txt", 'r') as f:	
        content = f.readlines()

    dns_servers = []
    for line in content:
        if "Name Server" in line:
            line = line.strip()
            dns_servers.append(line)

    # remove duplicates from dns_servers
    dns_servers = list(set(dns_servers))
    
    
    # create dns_servers txt file and populate with dns info	
    subprocess.Popen("touch dns_servers.txt", shell=True)
    i = 0
    for dns_server in dns_servers:
        if i == 0:
            subprocess.Popen("echo DNS recon info on %s > dns_servers.txt" % website, shell=True);
            subprocess.Popen("echo %s >> dns_servers.txt" % dns_server, shell=True)
        else:
            subprocess.Popen("echo %s >> dns_servers.txt" % dns_server, shell=True)
        i = i + 1

    # remove temp.txt file
    subprocess.Popen("rm temp.txt", shell=True)

def get_IP_addresses(website):

    # get the IP address for the website	
    subprocess.call("host %s > temp.txt" % website, shell=True)
    with open("temp.txt", 'r') as f:       
        first_line  = f.readline().strip()

    subprocess.call("echo %s IP address: > IPs.txt" % website, shell=True)
    subprocess.call("echo %s >> IPs.txt" % first_line, shell=True)

    # get the IP addresses for the websites DNS servers
    subprocess.call("whois %s > dns_temp.txt" % website, shell=True)
    with open("dns_temp.txt", 'r') as f:	
        content = f.readlines()

    dns_servers = []
    for line in content:
        if "Name Server" in line:
            line = line.strip()
            dns_servers.append(line)

    # remove duplicates from dns_servers
    dns_servers = list(set(dns_servers))
    
    subprocess.call("echo %s DNS server IP addresses: >> IPs.txt" % website, shell=True)
    for dns_server in dns_servers:
	dns_server_name = string.replace(dns_server, "Name Server: ", "")
        subprocess.call("host %s >> IPs.txt" % dns_server_name, shell=True) 
    
    subprocess.call("rm temp.txt dns_temp.txt", shell=True)

def get_recon_method():
    recon_method = raw_input("Select one of the folloing reconnaisance options: \n1)IP Addresses\n2)DNS Servers\n3)Public Files\n")
    return recon_method

def main():
    website = raw_input("Enter the name of the site you wish to perform reconnaisance on:")
    
    recon_method = get_recon_method()

    if recon_method == "1":
        get_IP_addresses(website)
    elif recon_method == "2":
        get_DNS_servers(website)
        subprocess.Popen("echo DNS reconsaissance successful!\necho \"dns_servers.txt\" created", shell=True)
    elif recon_method == "3":
        get_public_files(website)
    else: 
        get_recon_method()
    


main()
