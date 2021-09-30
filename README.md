## Python Twitter API

### Pre-requsites:
1. Python3.6 or higher
2. version control (git)

### Installation steps (assuming linux terminal):
```
1. git init
2. git clone https://github.com/gummadidala/tweets.git
3. cd tweets
4. cd twitter
5. pip install -r python-requirements.txt
6. python manage.py runserver 0:8002
```

### Usage:

1. #### Get tweets by a hashtag:
    **Endpoint URL**
    ``` http://localhost:8002/twitter/api/byhashtag/ ```
    **Query Parameters**
    _limit_ (integer)
    _hashtag_ (string) (**with out #**)
    **Example**
    ``` curl "http://localhost:8002/twitter/api/byhashtag/?limit=20&hashtag=playbold" ```

2. #### Get user tweets:
    **Endpoint URL**
    ``` http://localhost:8002/twitter/api/byuser/ ```
    **Query Parameters**
    _limit_ (integer)
    _username_ (string)
    **Example**
    ``` curl "http://localhost:8002/twitter/api/byuser/?limit=20&username=twitter" ```


