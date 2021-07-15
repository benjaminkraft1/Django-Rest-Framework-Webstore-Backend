# Store Backend Project
This Project goes beyond the requirements for the udacity full stack javascript developer project. 
I decided to build the project based on the django rest framework to be more flexible and scalable.

# Installation

## Install postgres
If not already installed, install postgres to provide the database.

#### Create the file repository configuration:
`sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'`

#### Import the repository signing key:
`wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -`

#### Update the package lists:
`sudo apt-get update`

#### Install the latest version of PostgreSQL.
#### If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
`sudo apt-get -y install postgresql`

## Install python dependencies
Create python virtual environment and install required python packages.
```bash
install.sh
```

To activate the Environment call `source ena.sh`

## Setup Database
### Create postgresql database

Use `sudo -u postgres psql template1` to open up the postgres-command prompt and insert the following

```sql
  
  CREATE DATABASE store_db;
  CREATE ROLE store_db_admin WITH LOGIN PASSWORD 'store_db_pass'; 
  ALTER ROLE store_db_admin SET client_encoding TO 'utf8';
  ALTER ROLE store_db_admin SET default_transaction_isolation TO 'read committed';
  ALTER ROLE store_db_admin SET timezone TO 'UTC';


  GRANT ALL PRIVILEGES ON DATABASE store_db TO store_db_admin;
  ALTER USER store_db_admin CREATEDB;
```

## Migrate Databae
Migrate the Database using:

```
python manage.py migrate
```

## Create django super user
Create a super user to get access from the endpoints requiring permission. 

```
python manage.py createsuperuser --username admin
```

## Unittests
run tests
```
$ ./manage.py test
```

# Run the server
start server
```
$ ./manage.py runserver
```

# API
Some API endpoints offer filter and search possibilities. 
Filtering is done using django filter backend: 
`https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend`
Search Filters: 
`https://www.django-rest-framework.org/api-guide/filtering/#searchfilter`
Results can be ordered using Ordering Filters: 
`https://www.django-rest-framework.org/api-guide/filtering/#orderingfilter`

### Permissions
https://www.django-rest-framework.org/api-guide/permissions/#djangomodelpermissions

Endpoint | read | write |
--- | --- | --- | 
api/user | `user.is_staff` is `True` | `user.is_staff` is `True` |
api/group | `user.is_staff` is `True` | `user.is_staff` is `True` |
api/products | `AllowAny` | `user.is_staff` is `True` |
api/categories | `AllowAny` | `user.is_staff` is `True` |
api/orders | `only for current user` OR all if `user.is_staff` is `True` | `user.is_staff` is `True` |

## Users
If the currently logged in user has permissions (`user.is_staff` is `True`), this endpoint returns a list of users.
Authentication can be done by login or token (see below).
```
http://localhost:8000/api/groups/
```

### Filter and Search Options
You can search for specific fields in the user list. Search filters are activated for `name` and `email` and will use case-insensitive partial matches.

Example:
```
http://localhost:8000/api/users/?search=john
```

### Ordering
The Users Endpoint give the posibility to order results by the fields `name`, `email` and `groups`. Per default, users are ordered by `name`.

Example:
```
http://localhost:8000/api/users/?ordering=username
```

## Groups
If the currently logged in user has permissions (`user.is_staff` is `True`), this endpoint returns a list of user groups.
Authentication can be done by login or token (see below).
```
http://localhost:8000/api/groups/
```

## Products
The Products endpoint can be accessed by any user (logged in or not). Writing access requires special permissions (`user.is_staff` is `True`).
```
http://localhost:8000/api/products/
```

### Filter and Search Options
You can search for specific fields in the user list. Search filters are activated for `name` and `category_id` and will use case-insensitive partial matches.
Example:
```
http://localhost:8000/api/products/?name=Apple
http://localhost:8000/api/products/?category_id=1
```

## Categories
The Categories endpoint can be accessed by any user (logged in or not). Writing access requires special permissions (`user.is_staff` is `True`).
```
http://localhost:8000/api/categories/
```

## Orders
Users can access their orders if they are logged in. If `user.is_staff` is `True` (admin), all orders are displayed.
```
http://localhost:8000/api/orders/
```

### Filter Orders by user
Example:
```
http://localhost:8000/api/orders/?user_id=3
http://localhost:8000/api/orders/?complete=true
```


# JSON Web Token Authentication
JSON Web Token is a fairly new standard which can be used for token-based authentication. Unlike the django REST framework built-in TokenAuthentication scheme, JWT Authentication doesn't need to use a database to validate a token. A package for JWT authentication is `djangorestframework-simplejwt` which provides some features as well as a pluggable token blacklist app. https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html

## Usage
### Obtain Token
Hint(If you have not created a user yet, create a django super user)
To obtain a token for a user you can use the following API Endpoint
```
http://localhost:8000/api/token/
```
or use curl
```
curl -X POST -H "Content-Type: application/json" -d '{"username": "USERNAME", "password": "PASSWORD"}' http://localhost:8000/api/token/

```

response:
```
{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NzcxOTAxMSwianRpIjoiOGM5MDQyZjQ0YTM5NDQxNDlkZWYwOTM5NmZkZDkzMzkiLCJ1c2VyX2lkIjoxfQ._YirlQj0GBYCUL14ro1ASZ1sd7u5TDvE8GQSc7wDKsc","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3NzE5MDExLCJqdGkiOiJhMWUwMGI5OWMxZGM0ZWUwYWFlMWVhNWFmOTVkMjA2NCIsInVzZXJfaWQiOjF9.GbeDWAgJ00BnyEFKIPOzWc7rYIOcSITgqfRSK-n8K_4"}
```

### Refresh Token
```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NzcxOTAxMSwianRpIjoiOGM5MDQyZjQ0YTM5NDQxNDlkZWYwOTM5NmZkZDkzMzkiLCJ1c2VyX2lkIjoxfQ._YirlQj0GBYCUL14ro1ASZ1sd7u5TDvE8GQSc7wDKsc"}' \
  http://localhost:8000/api/token/refresh/
```


### Test without Authorization header
```
curl -X GET http://localhost:8000/api/users/ -H "Content-Type: application/json"
```

response:
```
HTTP/1.1 401 Unauthorized
Server: SimpleHTTP/0.6 Python/3.6.9
Date: Tue, 13 Jul 2021 13:25:47 GMT
Date: Tue, 13 Jul 2021 13:25:47 GMT
Server: WSGIServer/0.2 CPython/3.6.9
Content-Type: application/json
WWW-Authenticate: Basic realm="api"
Vary: Accept, Cookie
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 58
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{"detail":"Authentication credentials were not provided."}
```

### Test with Authorization header
```
curl -X GET http://localhost:8000/api/users/ -H "Content-Type: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3NzE5MDExLCJqdGkiOiJhMWUwMGI5OWMxZGM0ZWUwYWFlMWVhNWFmOTVkMjA2NCIsInVzZXJfaWQiOjF9.GbeDWAgJ00BnyEFKIPOzWc7rYIOcSITgqfRSK-n8K_4" 

```

response:
```
{"count":3,"next":null,"previous":null,"results":[{"url":"http://localhost:8000/api/users/1/","username":"admin","email":"","groups":[]}, ...]}
```

