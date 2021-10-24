# LearnPy
A simple system to learn python

# How can I get it up and running?
First install python and then just follow these simple steps:

1. Clone this project
- ```git clone git@github.com:tnicacio/ifc-learnpy.git```

2. Initialize the backend
- Open the backend folder
- Optionally create a python virtual environment ```python -m venv env```
- Install the project dependencies ```python -m pip install -r requirements.txt```
- run backend.py

3. Initialize the frontend
- Open the frontend folder
- run courses.html with [live server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)

4. Make popcorn and have fun listing and registering awesome new courses

# Can I test only the backend with Postman?
Sure! The available routes on backend are:

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
