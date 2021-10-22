# PyEzMail
An abstraction over smtplib and email modules<br>
Uses ssl connection on port 465

## Install libraries
###### All tested on python 3.8
Install libraries
```shell
pip install smtplib
pip install email
```

## Import this module
```python
from PyEzMail import Message, User, MIMEParts
```

## Setup
```python
user = User("myemail@gmail.com", "MySuperSecurePassword123")
```

## Create message
```python
my_msg = Message("Subject")
```
### attach plain text
```python
my_msg.text(MIMEParts.text, "Important text")
```
### attach html
```python
my_msg.attach_html(MIMEParts.html, "<h1>Hello</h1>")
```

## Send message
```python
user.send(my_msg, "receiver@gmail.com")
```

## Debug
```python
print(user)
```
```
Email works user
User: myemail@gmail.com
```
```python
print(my_msg)
```
```
Email works message
Data:
data will be here
```
