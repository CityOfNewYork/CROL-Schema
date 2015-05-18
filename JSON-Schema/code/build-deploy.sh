#!env bash

DEPLOY_DIR="$(dirname `pwd`)/deploy"
APP_DIR="$(dirname `pwd`)/browser"

echo "Source from: $APP_DIR"
echo "Deploying to: $DEPLOY_DIR"

[ -d $DEPLOY_DIR ] && echo 'Deployment Folder exists already' && exit

mkdir $DEPLOY_DIR

cp -R $APP_DIR/docson $DEPLOY_DIR
cp -R $APP_DIR/public $DEPLOY_DIR
cp $APP_DIR/Procfile $DEPLOY_DIR
cp $APP_DIR/README.md $DEPLOY_DIR
cp $APP_DIR/app.json $DEPLOY_DIR
cp $APP_DIR/index.js $DEPLOY_DIR
cp $APP_DIR/package.json $DEPLOY_DIR
cp .sample-schema.json $DEPLOY_DIR/docson/schema.json
cd $DEPLOY_DIR
git init
git add .
git commit -am "initial push"
echo 'Deployment folder created!'
echo "Ready for Heroku!"
