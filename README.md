###Note : dependencies has been provides in requirement.txt file

Go to the Directory and run the following command for django setup 
    
    virtualenv venv
    
    source venv/bin/activate

    pip3 intall -r requirements.txt
    
    python manage.py migrate


#Task 1: Login/logout using jwt
###### step 1:

    create one superuser using python manage.py createsuperuser
    
###### step 2:  

    create mutilple users from shell
    
    command:
    python3 manage.py shell
    from django.contrib.auth.models import User
    user = User.objects.create_user(dummy, dummy@dummy.com, dummy@123)
    user.is_staff = True
    user.save() #if you want to set first and last name that can also be done

###### step 3:
API endpoint for login

    endpoint: /login
    
Goto api endpoint and pass username and password you will get a set a token in the below format(jwt) usign package simple-jwt, this credential can be used for django admin login
    
    {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwMjc5ODIwNiwianRpIjoiMDVmMzYxMTZjNzVlNDFlMTkxNTNhYjQ1YmMwYTRlMzIiLCJ1c2VyX2lkIjoyfQ.GvZhJxDqnqJgadIwhsSqdlMWf9XmISGUIAKsTyvnWIE",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAyNzEyMTA2LCJqdGkiOiIzNzkzMWE5MTE4ZTg0ZGNhODc0ZDUzYWFlNmQ3MWYzOSIsInVzZXJfaWQiOjJ9.hAK5Dy0a1R-t9n3LC4hQMnmBp6nmabNDU_hzC4Z8-FY"   
    }
    
###### step 4:    
API endpoint for logout

    endpoint: /logout
    
    
#Task 2: Gmail Scraping

###### Step 1: Enable the Gmail API follow link 

    https://developers.google.com/gmail/api/quickstart/python

    copy the downloaded credentials.json data and paste again variable `GMAIL_SCRAPING_CREDENTIALS` in setting.py file
    
    Credential of default gmail has been provided in settings.py
    
###### Step 2: Install the Google Client Library

Run the following command to install the library using pip:

    pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

###### Step 3: Access the API to scrap the mails

API url is 
    
    endpoint : /gmail-scraping
    
    once you hit the endpoint it will ask you email id and password in order to cretae a pickle file
    
    you can use these creds for login cred sent in the email
    
    
Request Params are:

    email_limit : 20
    query_text: invoice OR subcription or bill or amount

    http://localhost:8000/gmail-scraping?email_limit=5&query_text="invoice OR subscription OR bill OR amount"
    
