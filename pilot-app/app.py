from flask import *
from models.service import Service
from mlab import mlab_connect

app = Flask(__name__)
app.config["SECRET_KEY"] = "439234738 fdshkfs"
# 1. Connect
mlab_connect()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/service/<int:gender>')
def search(gender):
    filtered_services = Service.objects(gender=gender, occupied=False)
    return render_template('search.html', all_services=filtered_services)

@app.route("/admin")
def admin():
    return render_template('admin.html', services=Service.objects())

@app.route("/delete/<service_id>")
def delete(service_id):
    service = Service.objects().with_id(service_id)
    if service is None:
        return "Not found"
    else:
        service.delete()
        return redirect(url_for('admin'))


@app.route("/new_service", methods=['GET', 'POST'])
def new_service():
    if request.method == 'GET':
        return render_template('new_service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        phone = form['phone']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        print(name, phone, yob, gender, height)

        new_service = Service(name=name, phone=phone, yob=yob, gender=gender, height=height, occupied=False)
        new_service.save()
        flash("Da dang ki thanh cong")
        return redirect(url_for('new_service'))

@app.route('/edit/<service_id>', methods=['GET', 'POST'])
def edit_service(service_id):
    service=Service.objects().with_id(service_id)
    if service is None:
        return "Not found"
    else:
        if request.method == 'GET':
            return render_template("edit_service.html", service=service)
        elif request.method == 'POST':
            form = request.form
            name = form['name']
            phone = form['phone']
            yob = form['yob']
            gender = form['gender']
            height = form['height']
            service.update(set__name=name, set__phone=phone, set__yob=yob, set__gender=gender, set__height=height)
            flash("Da cap nhat thanh cong")
            return redirect(url_for('edit_service', service_id=service.id))



if __name__ == '__main__':
  app.run(debug=True)
