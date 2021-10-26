# :pie: LearnPy
A simple system to learn python

# How can I get it up and running?
First install python and then just follow these simple steps:

1. Clone this project
- ```git clone git@github.com:tnicacio/ifc-learnpy.git```

2. Initialize the backend
- Open the backend folder
- Optionally create a python virtual environment ```python -m venv env``` and activate it ```env\scripts\activate```
- Install the project dependencies ```python -m pip install -r requirements.txt```
- run backend.py

3. Initialize the frontend
- Open the frontend folder
- open courses.html or run it with [live server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

4. Make popcorn and have fun listing and registering awesome new courses

## Video with the steps above (except step 4)
https://user-images.githubusercontent.com/50798315/138598192-c1a2a627-f610-4aba-a9d4-c531837a9ff4.mp4

# Can I test only the backend?
Sure! The backend available routes are:

## [GET] /courses
To see a list with all the courses

## [GET] /courses/<course_id>
To find your course by its id

## [POST] /courses
To include a new awesome course
``` 
{
    "name": "New fun course",
    "imgUri": "image_uri.jpeg",
    "imgGrayUri": "image_course_completed_uri.jpeg"
}
```

## Video testing using [Postman](https://www.postman.com/)
https://user-images.githubusercontent.com/50798315/138597262-ed8066ce-f665-4953-a833-78304e9d9d00.mp4


