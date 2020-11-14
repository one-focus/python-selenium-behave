## Simple project using Page Object model and selenium to automate https://wikipedia.org

### Installation
+ Install python
```
brew install python
```
+ Install chromedriver
```
brew install chromedriver
```
+ Install dependencies
```
pip install -r requirements.txt
```
+ Set username and password for wikipedia.org
```
├──tests/login.py
username = 'your_username'
password = 'your_password'
```

### Create page objects:
+ Base page 
+ Login page
+ Main page
+ Search Results page

### Test cases:
+ Regression.feature
+ Validation.feature
