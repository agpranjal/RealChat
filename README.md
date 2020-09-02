# RealChat
Real time chat application

### Features:
+ Private chat (peer to peer) (with proper authentication and message storage)
+ Group chat

### Create a virtual environment and activate it (e.g. python3 venv):
+ `python3 -m venv testenv`
+ `source testenv/bin/activate`

> Note: To deactivate the virtual environment after you are done, type `deactivate` in the terminal.

### Install requirements:
`pip3 install -r requirements.txt`

### How to run ?
`python3 manage.py runserver`

Open browser and go to [127.0.0.1:8000](http://127.0.0.1:8000)

---

### NOTE (for private chat):
Following are some of the default users available in the database (only for testing purposes, you need to create your own account)

|username   |  password |
|---|---|
|  admin | admin123  | 
|  ag_pranjal |  ag_pranjal123 |
|  gaurav |  gaurav123 |
