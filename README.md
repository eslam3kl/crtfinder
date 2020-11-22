# crtfinder v2 
Here's the new version of CrtFinder tool which collect subdomains from crt.sh. 

The new update come with more scripts which collect more and more subdomains form the same site but in more intelligence techniques <3 


![intro](https://github.com/eslam3kl/crtfinder/blob/v2/intro.png)

-----------------------------------------

### How to install 
` pip install -r requirments.txt`

-----------------------------------------


### How to use it 
#### 1. Starndard search 
` python crtfinder.py -u domain.com `

This will come back with the subdomains from search keywords:
```
%.domain.com
domain.% 
```
and the output file will be `domain.txt` which contain the output. 

#### 2. Advanced search 
` python dig.py domain.txt ` 

this step will take more time but it will get more and more subdomains 

-----------------------------------------

### Case study

Website `dell.com`
 
**Standard serach ~ 4000 subdomain**

**Advanced search ~ 13000 subdomain**
 
 
