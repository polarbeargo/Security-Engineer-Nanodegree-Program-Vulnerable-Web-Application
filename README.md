# Security-Engineer-Nanodegree-Program-Vulnerable-Web-Application
[image1]: ./images/bruteforce.png
[image2]: ./images/cookie.png
[image3]: ./images/decode.png
[image4]: ./images/encode.png
[image5]: ./images/before.png
[image6]: ./images/admin.png
[image7]: ./images/BrokenAccess1.png
[image8]: ./images/brokenAccess.png
[image9]: ./images/b3.png
[image10]: ./images/Users.png
[image11]: ./images/SQLi.png
[image12]: ./images/SQLi2.png
[image13]: ./images/Sensitive.png
[image14]: ./images/hash.png
[image15]: ./images/onlinehashcracker.png
[image16]: ./images/SQLiResult.png
[image17]: ./images/XSS.png
[image18]: ./images/XSS1.png  
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
[VWA Project Report](/VWA-Project-Template.pdf)  

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

* Log in as user and copy the cookie
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

* Gain admin rights  

Before      |  Edit cookie & refresh browser
:-------------------------:|:-------------------------:
![][image5]                | ![][image6]
### We can retrieve the user information by modifying customers/id/1   

- After we manipulated the Cookie gain admin rights.
- Heading to Customers page hit view button.  
- Hit xhr type file go to Resonse tab then open new window.
![][image7] 
- You can see by modifying customers/id/2 we can direct retrieve the user information.

![][image8]  
![][image9]
Same as the Users page:  
![][image10]
![][image11]
![][image12]

### Expose Sensitive Data
- After we manipulated the Cookie gain admin rights.
- Heading to Customers page hit view button.
- Hit xhr type file go to Resonse tab then the passwords will be exposed. This is considered a security breach  

![][image13]  
- Copy paste the hash use hashid.py to find out the hash type is MD5 
 
![][image14]
- Use online hashcracker: https://hashes.com/en/decrypt/hash to crack the password.
![][image15]
### We can SQLi the customer page with' or 1='1  

- After we manipulated the Cookie gain admin rights.
- Heading to Customers page hit view button.
- Hit xhr type file go to Resonse tab then open new window.  

![][image13]
- We can SQLi customers page by insert' or 1 = '1 at the end of  /customers/id/1 to retrieve full customers information.
```
' or 1 = '1
```
![][image16]

### There is a XSS vulnerability in the profile section  

- Go to the XSS Section
- Next I check to see if Direct Chat was exploitable to XSS  
- Using the following XSS I was able to inject a javascript alert in Direct Chat  
 `“<script>alert(1)</script>”.`

![][image17]  
![][image18] 