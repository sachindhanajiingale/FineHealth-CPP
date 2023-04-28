# FineHealth-CPP

**Login Credentials:**
Username: sachin
Password: admin

Dependencies to run my project on local machine and as well as on AWS Cloud9 or deploying on Elastic Beanstalk is mentioned in my Requirements.txt file.

**Basic Commands for the project if you download it on local machine to test:**

python -m venv ven  

.\ven\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver


**Deployment Steps**
1.First i developed my application on VSCode, Then i ran my code on AWS Cloud9 and created a requirements file to create the requirements for Amazon linux 2 machine.

2. Then i Pushed my code to my github repository: https://github.com/sachindhanajiingale/FineHealth-CPP

3. After that i created a CI/CD pipeline for which i created codebuild and added my source as github with the above mentioned repository.

4. Then i created buildspec.yml file for codebuild and .ebextentions file along with django.config file which points to my root directory and then i created AWS EBS 
application and AWS EBS environment from AWS CLOUD9 using eb cli and aws cli.

5. Then i created the Codepipeline where i mentioned the Deployment on AWS Elastic Beanstalk where i choose my AWS EBS.

6. After successfully creating my pipeline i have made changes to code to check if the pipeline is working correctly or not.

7. Hurray! This is how i deployed my application.

8. Note: Remember i used all the roles mentioned by NCI that has to be used for AWS Codebuild, AWS Codepipeline and AWS ElasticBeanstalk.


