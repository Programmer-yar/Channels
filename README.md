# Chat app (Django Channels)
- To develop a simple  chat app following tutorial at https://channels.readthedocs.io/en/stable/tutorial/index.html
- Understand ASGI and Websockets.
- Follow the documentation and build on top

## Initial Setup:
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Setup redis-server and enter url in 'settings.py' in dict 'CHANNEL_LAYERS'

## TODO:
- User Authentication
- Get or create Chat room (for 2 people only)
- Save messages to database


### Test accounts:
- test_user -> testpass1
- test_user2  -> testpass2
