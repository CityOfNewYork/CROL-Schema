#!env bash

DEPLOY_DIR="$(dirname `pwd`)/deploy"
APP_DIR="$(dirname `pwd`)/browser"

# write new schema in deploy and local folder
[ -f $DEPLOY_DIR/docson/crow-schema.json ] && rm $DEPLOY_DIR/docson/schema.json
python ./schema.py > $DEPLOY_DIR/docson/schema.json

# copy to local
(cd $DEPLOY_DIR && git commit -am "deploy" && git push heroku master && heroku open)
