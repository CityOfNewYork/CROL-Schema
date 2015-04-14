#!env bash

[ -f ../browser/docson/crow-schema.json ] && rm ../browser/deploy/docson/schema.json
`which python3` ./schema.py > ../browser/deploy/docson/schema.json

(cd ../browser/deploy && git commit -am "deploy" && git push heroku master && heroku open)


