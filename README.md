# nlp-chat-api
Creation of a Flask API that serves as backend for a chat service that, besides allowing user signup, the communication among them or the creation of groups, also analyses the feelings of the registered chats using NLTK sentiment analysis. All the data added to this API is saved on a SQL database.

# Run API

$ export FLASK_APP=main.py
$ flask run

# SignIn

http://127.0.0.1:5000/signin?user_name=admin_n3&user_lastname=admin_ln3&user_mail=eduardoportoalonso@gmail.com&user_nick=admin3&user_pass=admin3

# LogIn

http://127.0.0.1:5000/login?user_nick=admin3&user_pass=admin3

