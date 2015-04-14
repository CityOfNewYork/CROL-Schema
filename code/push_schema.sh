#!env bash


# write new schema in deploy and local folder
[ -f ../browser/docson/crow-schema.json ] && rm ../browser/deploy/docson/schema.json
`which python3` ./schema.py > ../browser/deploy/docson/schema.json

# copy to local
cp ../browser/deploy/docson/schema.json ../browser/docson

(cd ../browser/deploy && git commit -am "deploy" && git push heroku master && heroku open)


