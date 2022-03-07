# Django Mini Project
A mini project of implementing basic CRUD functionalities using Django framework. 


## Steps to reproduce in your local:

### Installing

A step by step guide on how to setup your local environment/setting.


1: Create a local venv(virtualenv)

```
$ python3 -m venv <envName>
```

2: Activate the venv

```
$ source <envName>/bin/activate
```

3: Install all the modules listed within requirements.txt

```
$ pip install -r requirements.txt
```

4. `cd` into **tutorialProject** and make `manage.py` file executable by:

```
$ chmod +x manage.py
```

4: To run the Django server at localhost:

```
$ ./manage.py runserver
```

5: To activate Django shell:

```
$ ./manage.py shell
```


### List of TODOs:

* [ ] Add class-based views.

* [ ] Implement [DRF Router](https://www.django-rest-framework.org/api-guide/routers/) for mapping of URL with views.

* [ ] Implement unit-testing for views (using [APITestCase](https://www.django-rest-framework.org/api-guide/testing/#api-test-cases) from DRF and [model_mommy](https://model-mommy.readthedocs.io/en/latest/basic_usage.html)).

* [ ] Implement front-end frameworks/libraries, i.e: React.

* [ ] Add custom scripts to automate some stuffs (i.e: updating records in DB).

* [ ] Deploy this project/app onto Heroku, Azure or other platforms.

* [ ] Setup Github Actions YAML file for automating integration testing.

* [ ] Add codecoverage tools in Github Action's workflow.

* [ ] Setup Docker for this project.
