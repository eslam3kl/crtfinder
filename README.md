# crtfinder
Simple script tool to extract all subdomains from **crt.sh** website. Output will be up to *sub.sub.sub.subdomain.com*

![Welcome](Start.png)

![End](End.png)

--------------------------

## Updades: 
### Version 1.1, what's new? 
1. Upgrade to python3 
2. Add `dig.py` script to make advanced enumeration. 
```
# Default mode: it will return the default output ~ 4K subdomain
python3 crtfinder.py -u dell.com | tee -a subdomains.txt 
# Advanced mode: it will return ~ 14k subdomain
python3 dig.py subdomains.txt  
```

--------------------------
### Installation  
` pip install -r requirments.txt`

--------------------------
### Usage
` python crtfinder.py -u domain.com `
 
 
--------------------------
## Stay in touch <3 
[LinkedIn](https://www.linkedin.com/in/eslam3kl/) | [Blog](https://eslam3kl.medium.com/)  |  [Twitter](https://twitter.com/eslam3kll)
