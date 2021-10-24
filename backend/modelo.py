from config import *

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    img_uri = db.Column(db.String(255))
    img_gray_uri = db.Column(db.String(255))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return str(self.id)+") "+ self.name + ", " +\
            self.img_uri + ", " + self.img_gray_uri
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "imgUri": self.img_uri,
            "imgGrayUri": self.img_gray_uri
        }

# teste
if __name__ == "__main__":
    
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    def get_random_boolean():
        return bool(random.getrandbits(1))

    def get_course_name_with_random_begin_or_ending(course_name, with_random_begin):
        begins = ["Design of ", "Math with ", "Learn to ", "Dive with ",
        "From Zero to Hero with "]
        endings = [" 101", "'s Course", "'s Fun Lessons"]

        if (with_random_begin):
            return random.choice(begins) + course_name
        return course_name + random.choice(endings)

    def get_random_course_name(course_name):
        return get_course_name_with_random_begin_or_ending(course_name, get_random_boolean())


    stringJpeg = ".jpeg"
    for i in range(0, 10000):
        name_wannabe = names.get_last_name()    
        lower_name_wannabe = name_wannabe.lower()

        name = get_random_course_name(course_name = name_wannabe)
        img_uri = lower_name_wannabe + stringJpeg 
        img_gray_uri = lower_name_wannabe + "_gray" + stringJpeg

        course = Course(name = name, img_uri = img_uri, img_gray_uri = img_gray_uri)
        db.session.add(course)
        
    db.session.commit()
    
    for course in db.session.query(Course).all():
        print(course)
