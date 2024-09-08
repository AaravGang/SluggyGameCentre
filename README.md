# Server Code for online tic tac toe and connect4

---

## Install dependencies

```
pip3 install pygame
```

**Use `pip` on windows**

## Run the server

```
cd path/to/where/u/downloaded/this/folder
python3 server.py
```

☝🏻Above commands will switch yo working directory to where u download this folder, and then run the server.

**On windows use `python` instead of `python3`**

The server is up and running, clients can connect to it!

---

## But first run the wonderful bot!

**Open a new terminal/cmd window and paste the following commands to run the bot**

```
cd path/to/where/u/downloaded/this/folder
cd Bot/
python3 bot.py
```

---

## Now you can run the client code ( find that in another repo ), and play against other users!

# Online Games (better title soon)

<img width="1312" alt="Screen Shot 2021-12-27 at 10 17 03 PM" src="https://user-images.githubusercontent.com/86181184/147491543-f2435aaa-967a-4307-9ef6-c4d81240cdd4.png">

<img width="1312" alt="Screen Shot 2021-12-27 at 10 16 59 PM" src="https://user-images.githubusercontent.com/86181184/147491572-39d02a18-6848-437f-b32c-4bf165c8c8dd.png">

Online Tic Tac Toe and Connect4.

## Setup

If you dont have python3 installed, then go to https://www.python.org/downloads/ and install `python3.8` or `python3.9`. cuz I'm not sure if it'll work on other versions.

Once you have that, download this client folder's zip on your `Desktop` and unzip it. (It will prolly be named `client-public-main`, rename it to `client`)

Next, Open a new terminal or command prompt, and paste in the following commands:

```
cd Desktop/client
```

👆🏻 This will switch your current directory to the client folder.

```
python3 -m pip install -r requirements.txt
```

This will install the dependencies required to play the game. **Use only `python` instead of `python3` on Windows**

## Play the game

### Run the client.py file by:

```
python3 client.py
```

on mac

OR

```
python client.py
```

on windows

The client will ask for the server's details, paste them in (right click), and you'll be good to go!
