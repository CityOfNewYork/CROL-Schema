City Record Online Schema Repo

This repo will consolodate and house the Schema related aspect of the City Record Online Project


* Documentation

* Schema publishing [website](https://crow-schema.herokuapp.com/#schema.json)
  * Create a build environment to allow our schema authors to
    focus on the schema and not the tools


Requirements
------------
* A [Python](https://www.python.org/downloads/) installation.
  * Python's [pip](https://pip.pypa.io/en/latest/installing.html) package managemer.
    run "pip --version" from the commandline/terminal to check if it is installed.
  * [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
  * [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)
* [nodejs](https://nodejs.org/)
* [heroku](https://toolbelt.heroku.com/)
* [JSL](https://pypi.python.org/pypi/jsl), A python DSL for defining JSON Schemas

Setup
-----

**Note: You only have to do this once!**

* Create the heroku deployment app and folder
   * Open Terminal and navigate to the code folder
   * bash build-deploy.sh
   * cd ../deploy
   * heroku create
     * enter your heroku details
     * take note of your appName
   * git push heroku master
   * heroku open

Building the Schema
-------------------

* Open Terminal and navigate to the code folder
* bash push-schema.sh
  * hopefully you will see no errors
* heroku open --app <appName>
  * the appName that you took note in the Setup above


Run the App locally
-------------------

* Open Terminal and navigate to the deploy folder
* npm install express
* node index.js
* view your schema at [localhost](http://localhost:5000/#schema.json)






