# Security-Engineer-Nanodegree-Program-Vulnerable-Web-Application
[image1]: ./images/bruteforce.png
[image2]: ./images/cookie.png
[image3]: ./images/decode.png
[image4]: ./images/encode.png
### Install bandit:
```
 # Using virtualenv
virtualenv venv

source venv/bin/activate

# The wheel is optional, but its always a good idea to install this
pip install wheel
pip install bandit
```

### Run bandit:
```
 bandit -r VulnWebApp -o RESULT-FILE-NAME.txt -f txt
 ```
 
[bandit Scan Results](/RESULT-FILE-NAME.txt)

### Security Report: 
[VWA Project Report](/VWA-Project-Template.docx)  

### Use the bruteforce.py tool for brute force attacks:

```
python bruteforce.py -U test-username.txt -P test-password.txt -d username=^USR^:password=^PWD^ -m POST -f "Login Failed" http://localhost:3000/login
```
![image1]

### Open Browser Developer Tools 
#### FireFox
```
Cmd + Opt + I 
```
#### macOS
```
Option + ⌘ + J 
```

### The Cookie can be manipulated to gain admin rights  
![image2]  

* Decode the cookie with base64
``` 
python performbase64.py -d Mjp1c2Vy
```
![image3]

* Eecode the cookie with base64
```
python performbase64.py 2:user
python performbase64.py 1:admin
```

![image4]
### We can count the customers up if you add customers/id/1 and so an at the end of the URL  

### We can SQLi the customer page with or 1='1  

### There is a XSS vulnerability in the profile section  

### If we put a breakpoint in the getCustomer function, we can see the hashes of the customers