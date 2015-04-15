# City Record Online Workgroup (CROW) - Schema

This is the main repository containing efforts pertaining to the schema development of CROW. For parsing libraries, see https://github.com/CityOfNewYork/CROL-Parsing. 

Disclaimer. In case of conflicting document versions, please refer to documents mentioned in GitHub as the latest version.


## About
This repo will consolodate and house the Schema related aspect of the City Record Online Project


* Documentation

* Schema publishing [website](https://crow-schema.herokuapp.com/#schema.json)
  * Create a build environment to allow our schema authors to
    focus on the schema and not the tools


## Requirements

* A [Python](https://www.python.org/downloads/) installation.
  * Python's [pip](https://pip.pypa.io/en/latest/installing.html) package managemer.
    run "pip --version" from the commandline/terminal to check if it is installed.
  * [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
  * [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)
* [nodejs](https://nodejs.org/)
* [heroku](https://toolbelt.heroku.com/)
* [JSL](https://pypi.python.org/pypi/jsl), A python DSL for defining JSON Schemas


## Setup

**Note: You only have to do this once!**

### Create the heroku deployment app and folder

   * Open Terminal and navigate to the code folder

   1. Stage the app
    ```sh
    $ ./build-deploy.sh
    Source from: /Users/cds/dev/python/crow/Schema/browser
    Deploying to: /Users/cds/dev/python/crow/Schema/deploy
    .
    Deployment folder created!
    Ready for Heroku!
    $
    ```

   2. Bind the app to Heroku, and take note of the name.
      In the example below the appName is **immense-plateau-2012**
    ```sh
    $ cd  ../deploy
    $ heroku create 
    Creating immense-plateau-2012... done, stack is cedar-14
    https://immense-plateau-2012.herokuapp.com/ | https://git.heroku.com/immense-plateau-2012.git
    Git remote heroku added
    $
    ```

   3. Deploy the app to Heroku
    ```sh
    $ git push heroku master
    .
    remote: Verifying deploy... done.
    To https://git.heroku.com/immense-plateau-2012.git
     * [new branch]      master -> master
    $
    ```

   4. Browse to the app on Heroku

    ```sh
    $ heroku open
    ```

## Building the Schema

   * Open Terminal and navigate to the code folder

   1. Generate & push the schema
      **If there are no errors...** Your browser will open to the app page, 
      enter and submit 'schema.json' to view the JSON schema

    ```sh
    $ ./push-schema.sh
    [master 48bb874] deploy
     1 file changed, 51 insertions(+), 51 deletions(-)
    remote: Verifying deploy... done.
    To https://git.heroku.com/immense-plateau-2012.git
    Opening immense-plateau-2012... done
    $
    ```

## Run the App locally


  * Open Terminal and navigate to the deploy folder

  1. Install express dependency
    ```sh
    $ pwd
    ~/Schema/deploy

    $ npm install express
    .
    └── accepts@1.1.4 (negotiator@0.4.9, mime-types@2.0.10)
    ```

  2. Run the app locally
    ```sh
    $ node index.js
    Node app is running at localhost:5000
    ```

  3. view your schema at [localhost:5000](http://localhost:5000/#schema.json)
