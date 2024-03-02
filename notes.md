1. Created our project!
2. Created submodule shortner which is our main app!
3. Add a templates directory and configured the setting.py in urlshortner app
4. Created our template index.html
5. Created a route to a link that points to our "shortner.urls"
6. Created a views and used the template html page as our response
7. Add routing for the model in shortener.urls.py
8. Created a simple fronte-end and a form, POST form
9. Created a script to redirect the response data to /create routes
10. Add shortened url redirection
11. Add url parser in shortner/views
12. Query to avoid multiple url with diffrent shortened url

## NOTE:
* I'm saving URL/Link as URL in the database!!

## instruction to host this web application online!
1. we are going to use ***gunicorn*** and ***django-heroku***

## random generator sucks!
* using uuid4 and taking first 5 character from the uuid4 is bad, randomness < 16 ^ 5!
* using random.choice() on (26 + 26 + 10) alphabet + number is bad too, randomness < 62 ^ 5 as we are not randomizing the static main character string>.
> abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890

> abcdefghixyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890jklmnopqrstuvw

> bcdefghixyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890jklmnopqrstuvwa...
* final, using python's **secrets** library

``` python
import secrets

random_string = secrets.token_urlsafe(5)
```