from flask import Flask,render_template,request,session
import uuid
import os
import schedule
app = Flask(__name__)
app.secret_key = "SecretKey"


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/design")
def design():
    return render_template("design.html")

@app.route("/form/<string:design>", methods = ["GET","POST"])
def form(design):
    session["design_sess"] = design
    return render_template("form.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/design1")
def design1():
    return render_template("design1.html")

@app.route("/design2")
def design2():
    return render_template("design2.html")

@app.route("/design3")
def design3():
    return render_template("design3.html")

@app.route("/design4")
def design4():
    return render_template("design4.html")


@app.route("/upload" , methods=["GET","POST"])
def upload():
    desging_upload = session.get("design_sess")
    if desging_upload == "design1":
        design_name="design1.html"
    elif desging_upload == "design2":
        design_name="design2.html"
    elif desging_upload == "design3" :
        design_name="design3.html"
    elif desging_upload=="design4":
        design_name="design4.html"
    if request.method == "POST":
        name = request.form.get("firstname")
        lastname = request.form.get("lastname")
        Collage = request.form.get("Collage")
        School = request.form.get("School")
        phone = request.form.get("phone")
        email = request.form.get("email")
        Skills = request.form.get("Skills")
        about = request.form.get("about")
        job_role = request.form.get("job_role")
        github = request.form.get("github")
        LinkedIn = request.form.get("LinkedIn")
        img_new_name = request.form.get("img_new_name")
        
        key = uuid.uuid1()
        #image uploading methood
        img = request.files["image"]
        img.save(f"static/images/{img.filename}")
        img_new_name = f"{key}{img.filename}"
        os.rename(f"static/images/{img.filename}",f"static/images/{img_new_name}")

    return render_template(design_name, uname = name, ulname = lastname, ubname = Collage,ukname = School ,image = img_new_name, ucname = phone
                           ,udname = email,uename = Skills,ufname = about, git = github, Link = LinkedIn, job = job_role)   

def delete():
    files = os.listdir("static/images")
    for f in files:
        os.remove(f"static/images/{f}")        
        
if __name__ == "__main__": 
    schedule.every().day.at("23:59").do(delete)
    app.run(debug=True)
