# nlp-chat-api
Creation of a Flask API that serves as backend for a chat service that, besides allowing user signup, the communication among them or the creation of groups, also analyses the feelings of the registered chats using NLTK sentiment analysis. All the data added to this API is saved on a SQL database.

# Run API
$ export FLASK_ENV=development
$ export FLASK_APP=main.py
$ flask run

# SignIn

http://127.0.0.1:5000/signin?user_name=admin_n2&user_lastname=admin_ln2&user_mail=admin_2@gmail.com&user_nick=admin_2&user_pass=admin_2

# LogIn

http://127.0.0.1:5000/login?user_nick=admin&user_pass=admin

