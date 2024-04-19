.. Orange_County_Lettings documentation master file, created by
   sphinx-quickstart on Fri Apr 12 13:08:30 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Orange_County_Lettings's documentation!
==================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

===========
Description
===========
OC Lettings is a startup specializing in real estate rental services.
Currently in the midst of expanding operations in the United States,
the company aims to enhance its website and deployment process
to meet the growing needs of its clientele.
In this regard, several key areas have been identified for improvement
and/or addition to optimize the user experience
and streamline internal management processes.

===========
Project Objectives
===========
1. Modular Architecture Refactoring: We aim to restructure the OC Lettings GitHub repository for better file organization and clear separation of modules and functionalities.

2. Reduction of Technical Debts: Actions will be taken to reduce technical debts present in the project, such as code cleanup, addressing performance issues, and updating obsolete dependencies.

3. Implementation of CI/CD Pipeline: We will establish a continuous integration and continuous deployment (CI/CD) pipeline to automate testing and code deployment, ensuring regular and reliable updates to the site.

4. Application Monitoring with Sentry: The Sentry application monitoring service will be integrated to track errors and performance of the site in real-time, enabling quick response to any malfunctions.

5. Creation of Technical Documentation: We will develop comprehensive technical documentation of the application using Read The Docs and Sphinx, facilitating understanding of the code and internal processes for team members and future developers.

============
Installation
============
Make sure you have Python installed on your machine.

Create and activate a virtual environment with the following commands:

For Linux and Mac :

   ``python -m venv venv``

   ``source venv/bin/activate``

   ``pip install -r requirements.txt``

For Windows :

   ``python -m venv venv``

   ``venv\Scripts\activate``

   ``pip install -r requirements.txt``

===========
Quickstart
===========

----------------
Test Environment
----------------

Create .env file to add SENTRY_DSN key and SECRET_KEY key, see the following example

   ``SENTRY_DSN=["insert_your_SENTRY_DSN"]``

   ``SECRET_KEY=["insert_your_SECRET_KEY"]``

Set ``DEBUG = True`` in settings.py

   ``python manage.py runserver``

Go to http://127.0.0.1:8000/

------------------------
Docker Local Environment
------------------------


Make sure you have the following in place before you begin deployment:

- An environment with Docker installed.
- A Docker Hub account with the necessary credentials.

Set ``DEBUG = False`` in settings.py

   ``docker build -t [image Docker name] .``

   ``docker run -p 80:80 [image Docker name]``

Go to http://127.0.0.1:80/

To stop and remove container, run the following commands

   ``docker stop [container Docker name]``

   ``docker rm [container Docker name]``


======================================
Technologies and Programming languages
======================================
Python==3.11.3

Django==3.0

gunicorn==21.2.0

nginx==1.22.1

sentry-sdk==1.40.6


*Services*
   Docker

   Github Actions

   Render

   Sentry

===================
Models and Database
===================
Database : SQLite3

**Class Address**

Fields:

- number: PositiveIntegerField, representing the street number.
- street: CharField, representing the street name.
- city: CharField, representing the city name.
- state: CharField, representing the state abbreviation.
- zip_code: PositiveIntegerField, representing the ZIP code.
- country_iso_code: CharField, representing the ISO code of the country.


**Class Lettings**

Fields:

- title: CharField, representing the title of the letting.
- address: OneToOneField, representing the address associated with the letting.


**Class Profiles**

Fields:

- user: OneToOneField, representing the associated user.
- favorite_city: CharField, representing the user's favorite city.

===========
Deployement
===========

To deploy and manage the oc_letting_site application in production,
you can follow the following steps:

-----------------
Deployment Steps
-----------------

Docker Image Build: Use GitHub Actions to trigger a Docker image build whenever the source code changes in the GitHub repository.

Publishing the Docker Image: After building the Docker image, publish the image to Docker Hub to make it accessible to Render.

Configuring Render: Use Render to build and deploy services using the Docker image published on Docker Hub. Include steps for creating a new service on Render, linking the service to your GitHub repository, specifying which Docker image to use, and more.

Continuous Deployment: Configure GitHub Actions to perform continuous deployment every time a new version of the code is pushed to the main branch of the GitHub repository. This might include steps like building the Docker image, publishing to Docker Hub, and updating the Render service.

Deploy the last commit

When the site is live, go to https://orangecountylettings-1.onrender.com/
