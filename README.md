# CHINA-DB
Application to visualize Christian missionary activity in China over time.

USAGE:

```
cd src
mkdir backend
virtualenv -p python3 cdb-env
cd ..
pip install -r requirements.txt

cd frontend
npm install
npm run build

cd ..
FLASK_APP=wsgi.py FLASK_DEBUG=1 flask run
```