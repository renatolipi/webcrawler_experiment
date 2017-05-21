# webcrawler_experiment
temporary experiment; this should be replaced by another repo(s)

-----


##### Before get started:

System packages required:

`sudo apt-get install python-pip virtualenv`

It's recommended to use a virtualenv. Create one and activate it.

`virtualenv VENV`

`source VENV/bin/activate`



## How to run?

Clone this repo, then go to its main folder (where you'll find `app.py`):

`cd /path/to/webcrawler_experiment`



#### Running with Docker:

`docker build -t ubuntu:latest .`

`docker run -d -p 8088:8088 ubuntu:latest`


#### Running directly on your computer

  First, install the requirements:

  `pip install -r requirements.txt`

  Then, run:

  `python app.py`

  or

  `gunicorn -w 2 -b 0.0.0.0:8088 app:app`



### How to access?

  Go to your web browser and try:

  _http://127.0.0.1:8088/_  (to check if it works)

  _http://127.0.0.1:8088/feed/autoesporte/_ (to get your json)
