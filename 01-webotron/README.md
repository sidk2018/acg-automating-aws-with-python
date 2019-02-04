# acg-automating-aws-with-python
Repository for the A CLOUD GURU course * Automating AWS with python

## 01-webotron
webeotron is a script that will sych a local directory to an s3 bucket,  nad optionally 
configure Route 53 and cloud front as well.

###  Features
webotron currently has the following features

- List Buckets
- List contents bucket of the bucket
- create and setup-bucket 


## sid-note
pipenv --three
 #create python 3 env
pipenv install boto3
 # boto3
pipenv install -d ipython
 # ipython -d dev env use
 # Installing ipython…
  #Adding ipython to Pipfile's [dev-packages]…
pipenv run ipython -i .\ipythonsession.py
  # run ipython in dev environment with session settings
pipenv run python webotron/webotron.py
   # or
pipenv shell 
python webotron/webotron.py

# create bucket with var regiion not self
 new_bucket = s3.create_bucket(Bucket= "ttgen-python-automation-lab-01",CreateBucketConfigur
   ...: ation={"LocationConstraint":session.region_name})