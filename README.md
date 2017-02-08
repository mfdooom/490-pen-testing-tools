# 490-pen-testing-tools

####NAME  
recon.py - Reconnaissance tool for Penetration Testing  
  
####SYNOPSIS  
recon [-dei] [url]  
  
####DESCRIPTION
This is a script which streamlines a number of steps in
the reconnaissance phase of a penetration test. It allows
for the input of a flag and an URL which will be used to
gather information about a website, where the flag determines
what information is gathered.
  
####REQUIREMENTS  
This script is intended to be run with Python 2.7. It is not compatible  
with Python 3 and above.   
  
####OPTIONS  
If only a URL is entered, the command will return an aggregated list  
of all available information concerning that URL.  

If no operands are given, a help message will be displayed and the  
command will do nothing else.  

    -d          Return information about DNS servers associated with
                the given URL.

    -e          Return information about email addresses associated with
                the given URL.

    -i          Return information about IP addresses associated with
                the given URL.
    
####EXAMPLES  
recon.py -i google.com  
recon.py -d apple.com  
recon.py -p amazon.com  
  
####AUTHORS  
Patrick Knight  
Logan Smith  
