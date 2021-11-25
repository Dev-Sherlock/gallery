# gallery
## How to run the project locally:
To run this project, follow these steps:

1.  (optional) Create and activate a virtualenv.

2.  Clone this repo:
```
https://github.com/Dev-Sherlock/gallery
```
3.  Install dependencies, create a development database and start the  development server:
```
sudo docker-compose up
```
4.  Open your browser and go to http://0.0.0.0:8000/. 

## How to use this project:
1.  Firstly, you have to create a UserProfile. You can follow the guide below: "How to create a UserProfile"
2.  From now on, you're ready to use this project. You can make GET request to get a list of images and POST request to save the image. Examples:
```
          curl -X GET \
          -H 'Accept: application/json' \
          -H 'Content-Type: multipart/form-data' \
          -u user1:your_password1 \
          http://0.0.0.0:8000/
```

```
        curl -X POST -S \
          -H 'Accept: application/json' \
          -H 'Content-Type: multipart/form-data' \
          -u user1:your_password1 \
          -F "image=@/directory/of_the_image/goes_here;type=image/jpeg" \
          http://0.0.0.0:8000/

```



## How to create a UserProfile:
1.  Firstly, you have to create a superuser using the following command:
```
sudo docker exec gallery_service ./manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('user1',  'your_email@example.com', 'your_password1')"
```
2.  Go to the admin page at  http://0.0.0.0:8000/admin and enter the following credentials:
LOGIN:    user1
PASSWORD: your_password1

3.  Go to the UserProfiles section.

4.  Click add UserProfile.

5.  In a User field, select user1. In a Type field, select the type of account you prefer.

6.  Click Save.


## Important:

Before following setting it up, docker and docker-compose must be installed.

