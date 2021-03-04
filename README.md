# NLP-chat-api

This Flask API I developed serves as backend for a chat service that, besides allowing users to sign and log in the service, send messages to other users or create and admin groups, also performs a sentiment analysis of each of the messages had been sent, using the Vader Sentiment Analysis function from [NLTK library](https://www.nltk.org/_modules/nltk/sentiment/vader.html). 

The cool tool of this API is that user is able to check on that analysis with just hovering the mouse over the specific message. This will display a tooltip with the compound data, a value ranging from 1 to -1, depending on how positive or negative is the message, among some other information.

## Security

The user's data is well protected on this API, as some personal data such as name, lastname, email and, of course, password are hashed in the moment of the registration. 

This process is performed throug Python's library 'hashlib'. The data is encrypted with its ['pbkdf2_hmac'](https://docs.python.org/3/library/hashlib.html#hashlib.pbkdf2_hmac) function, which provides PKCS#5 password-based key derivation. I use a [‘sha256’](https://en.wikipedia.org/wiki/SHA-2) hash digest algorithm for HMAC, and a ['salt'](https://en.wikipedia.org/wiki/Salt_(cryptography)) of 32 bytes, randomly generated through os' ['urandom'](https://docs.python.org/3/library/os.html#os.urandom) library.

Both the salt and the hashed data is stored as an hexadecimal string, and the latter has also a length of 128 bytes.

## Data Storage

All the data this API generates (users, chats, groups and messages) is stored on a SQL database through Flask-SQLAlchemy library, which implies the creation of models (classes) for each of the different kinds of registers named before.

Given the latter, the SQL schema for this particular database has five different tables; and following the Flask-SQLAlchemy principles, each of those tables has its own model (class):

 - Table 'users': has a model named 'User', with 13 columns -id (the assigned identification number of the registred user), name (user's name, HASHED), lastname (user's last name, HASHED), email (the user's mail, HASHED), username (has to be unique), password (the HASHED password), confirmed_at (date of the user's registration), last_login_at (date of the user's last login), login_count (counts the number of times the user has been logged in)-.

 Each of those hashed entries has its own salt stored on its contiguous column.

 Besides that, each entry has different functions such as a password and an email checker, in order to help the login or authentication tasks; or two functions to get the opened chats and the groups where the user is included. 

 - Table 'users_has_chats': with a model called 'Chat', has four different columns -id (unique assigned identifier of the chat), user_a_id (id of the user that opened the chat and sent the first message), user_b_id (id of the user that received the first message of the chat), create_at (date when the chat had been created)-.

 In order to avoid the creation of two chats with both users but registered on different columns, I added an extra function ('chat_exists') to the 'User' model.  that is able to check wether the user already has a chat with the other selected user or not. 
 
 In the 'Chats' menu of the API, the user has the option of creating a new chat (choosing the receiver from a dropdown search menu) or select an already opened one. Thanks to that function, In case the user selects a receiver with whom already has an opened chat, this will redirect him to that existant chat instead of open a new one.

 There is also another function that returns the object of the chat's other user.
 
 The fact that one user is named 'a' and the other 'b' makes no different at all, as both users have the same permissions over the chat. 

 - Table 'users_has_groups': with it model, called 'Group'. It has 13 columns -id (unique assigned identifier of the group), group_name (the name of the group), group_admin_id (the user id of the group's creator), user_b/j_id (the ids of the rest of the users), created_at (date of creation) -.

 Each group could has up to 10 users, admin included, who also can delete some users and include new ones.

 There are four functions implemented on this class: 'get_users', that gets a list with the objects of all the users included in the group; 'get_empties', that returns the still-available places of the group, 'user_place', that returns the place where a specific user is in the group; and 'update', which deals with the task of assign a place to a new user.

 - Tables 'chat_messages' & 'group_messages': with the models 'Cmessage' and 'Gmessage'. Both classes have the same columns -id (unique assigned identifier of the message), chat_id(the id of the chat where the message has been sent), user_id (the id of the sender), message (the string with the message itself), neg_score (the neagtive score of the message, from 0 to 1), neu_score (the neutral score of the message), pos_score (the positive score of the message), compound (the compound valu of the message's sentiment analysis, which ranges from 1 or pòsitive to -1 or negative)-.

 Both classes have just a function, 'compound_color', which returns the assigned color for the resultant compound value of the message's sentiment analysis. I will explain this color-gradient below.

## Forms

Each of the API's froms (Sign and Log In, Group tasks or Messages) have been created and implemented with ['Flask_WTForms'](https://flask-wtf.readthedocs.io/en/stable/) library, which helps out with the validation tasks and the alerts.

## End Points and templates

This API has 10 different endpoints, rendered in eight different HTML templates. The latter have a really simple design, as this is the first project in which I use HTML, CSS and JS code. As simple the design is, it also makes the the user experience easier.

Besides the login/logout and sign in endpoints, and the user's home page, which are similar to the typical ones that could be seen in any other API, I would like to explain the endpoints for any given chat or group.

As the user is logged in, the Home endpoint is opened, with just a topbar where, from left to right, can be seen: 

 - The user's name, in green, which is static in every endpoint and gives access to this very page when clicked.
 - The links for the Chats/Groups menus.
 - The Logout button, on the far right.

This topbar will be fixed for each of the menus.

### Chats menu

It will add to the top bar the name of the chat's other user, in green, and show a side navigation bar with two sub-menus: New Chat, with a search-bar dropdown menu that shows all the registered users; and Chats, with the list of the opened chats. When a user for a new chat or an available chat is selected/clicked, the Chat menu is opened. This will deploy the message box and the 'Send' button on the first case; and also the already exchanged messages in the second. 

### Groups menu

It also adds the name of the group to the top bar, which in this case is clickable. It will deploy a new side navigation bar with the groups options. In case the user is the group's administrator, it will first show the list of the users included in the group (clicking on them will directly open a chat with that user); then the option to add a new user/s to the group, and also the option for removing a user/s. In case the user is not the group's admin, it will show just the list of users and the button to exit the group.

The permanent side navigation bar will have a sub-menu for creating a New Group, giving a form for the name of the group, a dropdown menu with multiple selection, giving the option of choosing more than one user at a time, and the button to create the group. Below that menu is the Groups menu, listing the groups in which the user is has been included.

## Messages and [NLTK-Vader Sentiment Analysis](https://www.nltk.org/_modules/nltk/sentiment/vader.html)

The messages will be shown in order, from most recent at the bottom of the scroll bar, to oldest at the top. Every chat/group will be charged from the bottom of the scroll bar. 

The dates of the messages will be shown in separators, as a container with a green background, once per date. The messages will include the name of the sender in case of the groups, the text and the time in which it was sent right below. If the user hovers the cursor over a message, a tooltip will be deployed with information about the sentiment analysis of the chosen message. It will have five parts:

 - The compound mark: measures the positivity or negativity of a message with a value comprehended between -1 (Negative) and 1 (Positive). There is a [really good explaination](https://stackoverflow.com/a/40337646) on how the model calculates this mark on StackOverflow.
 - The Tooltip's background: it will vary over 201 distinct color tones from red (-1/Negative) to green (1/positive), passing through yellow (0/neutral), depending on the compound value of the message, rounded to two decimals.
 - Positive, neutral and negative values: the values the model assigns to the message. It is a percentage of those three characteristics. 

# Further improvements

 - Show the usernames of the groups messages with different colors for each of the users.
 - Option to stop/delete the group for admins, keeping the messages for the users until the also delete the group.

