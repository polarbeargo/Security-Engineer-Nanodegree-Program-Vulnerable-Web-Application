# Security-Engineer-Nanodegree-Program-Vulnerable-Web-Application
[image1]: ./images/bruteforce.png
### Use the bruteforce.py tool for brute force attacks.

```
python bruteforce.py -U test-username.txt -P test-password.txt -d username=^USR^:password=^PWD^ -m POST -f "Login Failed" http://localhost:3000/login
```
![image1]
