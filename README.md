# WeConnect-Backend
We Connect is an online booking platform for hotels. As the name, we connect users who are in search of hotels  and hotels showcase their services!

## Author

* [Atieno Obwanda](https://github.com/AtienoObwanda)


## Getting Started

To get a copy of Masomo Popote running locally on your end, you can:

1. Clone this repository, by running git clone then:

for ssh:
```
git@github.com:AtienoObwanda/MasomoPopote.git
```

or for https: 
```
https://github.com/.git
```

2. Set up a python environment to run the application:
```
$ python3 -m venv env
$ source env/bin/activate
(env) $ pip install Django
```

### Prerequisites

Before you begin running the application, you must first install all the dependencies listed in the requirements.txt file.

```
 (env) $ pip install -r requirements.txt

```

### Installing

1. Create a database:
  ```
(env) $ psql CREATE DATABASE *DATABASE_NAME*;
(env) $ pip install psycopg2

```

2. Create a new .env file and set up the following configurations:

 * Database name, host, password and user.

3. Make your first migrations: 


```
(env) $ python manage.py migrate 
```


4. Make migrations for the tutors application: 

```
(env) $ python manage.py makemigrations tutors
(env) $ python manage.py migrate
```
5. Create a super user / admin:


```
(env) $ python manage.py createsuperuser
```


#API ENDPOINTS: 
**** 

1. Sign up as a user: https://weconnekt.herokuapp.com/api/signup/customer/
**** 
<!-- 2. Login as a user: -->
<!-- **** -->

2. Sign up as an admin: https://weconnekt.herokuapp.com/api/signup/admin/

**** 
<!-- 4. Login as admin: -->
<!-- ****  -->
**** 
3. Admin dashboard: https://weconnekt.herokuapp.com/api/admin/dashboard/
**** 
**** 
**** 
**** 
**** 
