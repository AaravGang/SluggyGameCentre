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
python3 -m pip install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
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

In your `client-public/` folder,

```
python3 client.py
```

---

### Connect to the server

<img width="1312" alt="Screen Shot 2024-09-14 at 9 15 18 PM" src="https://github.com/user-attachments/assets/4b8d01d7-bbff-4622-a80b-403bbbaca62a">

### Know who's online

<img width="1312" alt="Screen Shot 2024-09-14 at 9 25 22 PM" src="https://github.com/user-attachments/assets/94e19f3a-e79d-4bb3-8722-60e25fe2520e">

### Challenge your skill

<img width="1312" alt="Screen Shot 2024-09-14 at 9 23 14 PM" src="https://github.com/user-attachments/assets/b2678794-f135-4b7f-99c8-a0ff0094a62d">

---

**Confession**
Comments were added by GPT, but trust me bro the code itself is 1000% original.
Don't believe? Yu can verify by checking out my individual repos for the client and server.

> server: https://github.com/AaravGang/server-public
> client: https://github.com/AaravGang/client-public

---

Well then, I hope this is good enuf for yu to induct me😘
