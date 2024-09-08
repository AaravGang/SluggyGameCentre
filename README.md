# $${\color{lightgreen} SLUGGY \space GAME \space CENTRE}$$

Sluggy Game Centre is an online pygame "app" created by me to play Tic Tac Toe and Connect-Four. You can play against your friends or even a bot!
---
## To Play

First off you need to download all the code-
If you plan on hosting the server, download the entire repo.

If you only wanna connect to the server and play, just downloading the `client-public/` folder will suffice. 

---
## Let's start with the server

Follow these steps to host the server:

After downloading the entire repo, follow these steps:

--
### If this is your first time
Follow these steps to initialise a virtual env

```
python3 -m pip install virtualvenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
--
### Now you are ready to run the server

```
cd <path/to/server-public>
```

Once you are in the server-public folder:

```
python3 server.py
```

---
### If you want to start the Bot

Make sure no users are connected, when you fire up the bot
Once you run the `server.py` file, you can run the `bot.py` file in `Bot/` folder

In your `server-public/` folder

```
cd Bot/
python3 bot.py
```

---
## To join as a player

In your terminal change directories to your client-public folder.

```
cd <path/to/client-public>
```

If you haven't done so already in the main `SLUGGYGAMECENTRE\` folder
follow these steps to start a virtual env for the first time:

```
python3 -m pip install virtualvenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

If you have already created a virtual env, follow these steps to activate it before you can play:

```
source venv/bin/activate
```

--
### Finally you can now run the client file

In you `client-public/` folder,

```
python3 client.py
````