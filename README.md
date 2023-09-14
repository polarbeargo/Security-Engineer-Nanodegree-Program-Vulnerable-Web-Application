# Security-Engineer-Nanodegree-Program-Vulnerable-Web-Application
[image1]: ./images/bruteforce.png
### Use the bruteforce.py tool for brute force attacks:

```
python bruteforce.py -U test-username.txt -P test-password.txt -d username=^USR^:password=^PWD^ -m POST -f "Login Failed" http://localhost:3000/login
```
![image1]

#### Open Browser (FireFox)
```
Cmd + Opt + I 
```

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