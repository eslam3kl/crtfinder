# crtfinder v2 
Here's the new version of CrtFinder tool which collects more and more subdomains from crt.sh. 

The new update come with more scripts which collect more and more subdomains form the same site but in more intelligence techniques <3 

It works with python3 


![intro](https://github.com/eslam3kl/crtfinder/blob/v2/intro.png)

-----------------------------------------

### How to install 
```
pip3 install termcolor
pip3 install requests
```
-----------------------------------------


### How to use it 
#### 1. Starndard search 
 
` python3 crtfinder.py -u domain.com `

This will come back with the subdomains from search keywords:
```
%.domain.com
domain.% 
```
and the output file will be `domain.txt` which will contain the results. 


#### 2. Advanced search 
` python3 dig.py domain.txt | tee -a more_subdomains.txt` 

this step will take more time than the standard search, but it will get more subdomains 

/!\ Note: Don't change the text file name and use the one which get back from the first step --> `domain.txt`

-----------------------------------------


### Case study

Website `dell.com`
 
**Standard serach ~ 4000 subdomain**

**Advanced search ~ 13000 subdomain**
 
 
