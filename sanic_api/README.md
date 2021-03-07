# Sanic normalize API
A Python web-server implemented with Sanic Which:

* Create a login method for a user, and implement a JWT authentication mechanism 
* The web-server should accept input POST data to /normalize and return a normalized version of it.

# How to run the code
pip install -rrequirements.txt
create a config.json file with username and passord following this format:
```json
{
  "username": "admin",
  "password": "password"
}
```
run:

`python sanic_app.py`


# How to test
pip install -rrequirements_dev.txt
pytest tests
