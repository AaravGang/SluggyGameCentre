# $${\color{lightgreen} SLUGGY \space GAME \space CENTRE}$$

---

Sluggy Game Centre is an online pygame "app" created by me!
You can not only play TIC TAC TOE but also CONNECT-FOUR!
Not just with your friends, but also with a Bot to test your skills!

---

## To Play

First off you need to download all the code-

If you plan on hosting the server, download the entire repo.

If you only wanna connect to the server and play,

just downloading the `client-public/` folder will suffice.

---

## First Time Setup

Follow these steps to initialise a virtual env

```
cd <path/to/the/repo/>
```

**For Mac/Linux**

```
python3 -m pip install virtualvenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

**For Windows**

```
python -m pip install virtualenv
virtualenv venv
venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

---

## Non-first time Setup

```
cd <path/to/repo/>
```

**For Mac/Linux**

```
source venv/bin/activate
```

**For Windows**

```
venv\Scripts\activate.bat
```

## Let's start with the server

After downloading the entire repo,

and activating the virtual env follow these steps:

```
cd server-public/
python3 server.py
```

And Voila! Now the server is up and alive!
(unless u fked up. don't blame me😗)

---

### If you want to start the Bot

Make sure no users are connected when you fire up the bot.

Once you run the `server.py` file, you can run the `bot.py` file in `Bot/` folder

Run these commands in your `server-public/` folder:

```
cd Bot/
python3 bot.py
```

---

## To join as a player

In your terminal change directories to your client-public folder.

```
cd <path/to/client-public/>
```

> Note: If you have only downloded the client-public folder, make sure to follow the steps listed above to activate your virtual env

---

### Finally you can now run the client file

In you `client-public/` folder,

```
python3 client.py
```

---

### Connect to the server

<img width="1312" alt="Screen Shot 2023-02-20 at 2 25 36 PM" src="https://user-images.githubusercontent.com/86181184/220061644-9c10e696-cdc8-4a85-91b3-b8beccb06914.png">

### Know who's online

<img width="1312" alt="Screen Shot 2023-02-20 at 2 28 15 PM" src="https://user-images.githubusercontent.com/86181184/220063104-cbaff12b-89bf-41d2-b7ce-4c164a6ea7ea.png">

### Challenge your skill

<img width="1312" alt="Screen Shot 2023-02-20 at 2 28 20 PM" src="https://user-images.githubusercontent.com/86181184/220063718-cb98d4ba-88fa-43cb-b980-531ef1d1b847.png">
