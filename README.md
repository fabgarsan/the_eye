<h1 align="center">Welcome to The Eye 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
</p>

> A dockerized app built to track every move from different apps. It's called The Eye.

## Stack

### Build with

* Python
* Docker
* JavaScript
* Celery
* Django Rest Framework
* [Django](https://www.djangoproject.com/)
* [Vue](https://vuejs.org/)

## Install

### Run with docker

You must have Docker installed, and you must be run at the root of the project. This project is dockerized and uses
docker-compose as an orchestrator:

```
docker-compose up
```

## Usage

### Backend Admin

You will be able to access to the admin panel in http://0.0.0.0:8000/admin

#### Default User

Admin

#### Default Password

1234567890

### Allowed Hosts

The allowed host will be created using the control admin provided below.

In other to add a new allowed host to be tracked, you must create it in http://0.0.0.0:8000/admin/events/application/

By default, the domain www.consumeraffairs.com will be allowed.

### Allowed Filters

Three kinds of filters are possible with The Eye through GET method.

- Category using `category`
- Session using `session__id`
- Date Range using `date_from` and `date_to`

`http://0.0.0.0:8000/api/events/?category=page interaction&session__id=e2085be5-9137-4e4e-80b5-f1ffddc25423&date_from=2020-01-01&date_to=2021-02-02`

## Frontend

To get into the frontend you will be able to do it with http://0.0.0.0:8000/admin/events/application/

### Events

You will be able to trigger some events. Buttons and forms will be available.

On the other hand, "Set your session id" will give you the way to set your own session id. Also, "Set your application
name" will let you set the application name. REMEMBER, if you want to get the backend to save the event, you must first
create the application in the admin.

There is also a way to simulate the timestamp for the events.

### Filters

You will be able to filter the events in the backend. If any of the fields is empty, so, I will ignore the filter.

#### Category

Set the category you want to filter, then push "Fetch Events"

#### Session Id

Set the session id you want to filter, then push "Fetch Events"

#### Date Range

Set the range you want to filter, then push "Fetch Events"



## Author

👤 **Fabio Garcia Sanchez**

* Github: [@fabgarsan](https://github.com/fabgarsan)
* LinkedIn: [@fabgarsan](https://linkedin.com/in/fabgarsan)

## Conclusions

The Eye will be a not-blocking app that will allow saving data from each event.

It will always return a success status code in order of being transparent. Nobody likes to be observed; even those whos
have advanced knowledge for using the developer console in explorers.

In addition, The Eye will silently filter each host that calls each endpoint. Since it is something transparent, the
organization does not want to warn anybody.

On the other hand, it is important to let the developers know that something happens if The Eye gets any trouble with
the request. Hence, when an issue with the responses is found, the errors will be sent to the admins to take care of
them.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_