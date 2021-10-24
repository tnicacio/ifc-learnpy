from config import *
from modelo import Course

@app.route("/")
def inicio():
    return 'Plataforma de ensino LearnPy. '+\
        '<a href="/courses">Listar Cursos</a>'

@app.route("/courses/<course_id>")
def find_by_id(course_id):
    id = course_id
    course = db.session.query(Course).filter(Course.id == id).one()
    response = jsonify(course.json())
    
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/courses")
def find():
    course_name = request.args.get('name')

    courses = []
    if (course_name is not None):
      courses = db.session.query(Course).filter(Course.name.ilike('%' + course_name.lower() + '%')).all()
    else:
      courses = db.session.query(Course).all()

    courses_in_json = [ c.json() for c in courses ]
    response = jsonify(courses_in_json)
    
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/courses", methods=['post'])
def insert():
    response = jsonify({"result": "ok", "details": "ok"})
    data = request.get_json()
    
    try:
        course = Course(name = data['name'], img_uri = data['imgUri'], img_gray_uri = data['imgGrayUri']) 
        db.session.add(course)
        db.session.commit()
    except Exception as e:
        response = jsonify({"result":"error", "details":str(e)})
    
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

app.run(debug=True, host='0.0.0.0')    
