# WeConnect-Backend
We Connect is an online booking platform for hotels. As the name, we connect users who are in search of hotels  and hotels showcase their services!

****

## Author

 [Atieno Obwanda](https://github.com/AtienoObwanda)

****

## Getting Started

To get a copy of Masomo Popote running locally on your end, you can:

1. Clone this repository, by running git clone then:

for ssh:
```
git@github.com:SarahK95/WeConnect-Backend.git
```

or for https: 
```
https://github.com/SarahK95/WeConnect-Backend.git
```

2. Set up a python environment to run the application:
```
$ python3 -m venv env
$ source env/bin/activate
(env) $ pip install Django
```

****
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

4. Create a super user / admin:


```
(env) $ python manage.py createsuperuser
```

****

#API ENDPOINTS: 

1. Sign up as a user: https://weconnekt.herokuapp.com/api/signup/customer/
<!-- 2. Login as a user: -->
<!-- **** -->

2. Sign up as an admin: https://weconnekt.herokuapp.com/api/signup/admin/

<!-- 4. Login as admin: -->
<!-- ****  -->
3. Admin dashboard: https://weconnekt.herokuapp.com/api/admin/dashboard/

**** 

## Deployment

To get this application deployed live on a server, you can follow the following guide: [How to Deploy Django Applications on Heroku
](https://gist.github.com/AtienoObwanda/5c506e167e3672a1cc93bbf55fac984b)

**** 


## Built With

* Python3.9 - Backend

* Django4 - Python Framework

* Django Rest Framework - API end points

* PostgreSQL - Database 

* Heroku - Deployment

**** 


## User Stories:
**Users can:**
Sign up and login
Receive welcome email notifications
View hotels and add bookings
Receive bookings email confirmation
View their recent bookings and the total amount charged.
Update their profile
Cancel booking

**Hotel Admins can:**
Sign up and login
Update their profiles
Add, Edit and delete hotels
Add and delete rooms
View recent reservations
View charged amount for each resevation
View their reservations subtotal 
****


# Contributors:
* [Atieno Obwanda](https://github.com/AtienoObwanda)
* [Austin Omondi](https://github.com/aust1inn)
* [Maureen Njunge](https://github.com/MugureNjunge)
* [Sarah Kamunya](https://github.com/SarahK95)
* [Joyce Njoroge](https://github.com/joey57)

**** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

