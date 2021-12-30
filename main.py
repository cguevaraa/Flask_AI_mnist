from flask import Flask, render_template, request
import db
from csv_stats import get_stats
import tools

app = Flask(__name__)
model = tools.load_model()

@app.route('/')
def home():
    return render_template('index.html', msg='Hello visitor!')

@app.route('/test-form')
def user_form():
    return render_template('user_form.html', msg='')

@app.route('/test-form', methods=['POST'])
def user_form_return():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    nickname = request.form['nickname']
    gender = request.form['gender']
    msg = db.db_create_user(firstname,lastname,nickname,gender) # Load info into DB
    if msg == 'SUCCESS':
        return render_template('user_form_return.html', firstname=firstname, lastname=lastname, nickname=nickname, gender=gender)
    else:
        return render_template('user_form.html', msg=msg)

@app.route('/registered-users')
def get_users():
    users=db.get_users()
    return render_template('registered_users.html', users=users)

@app.route('/csv-stats')
def upload_csv():
    return render_template('csv_stats.html', msg='')

@app.route('/csv-stats', methods=['POST'])
def upload_csv_return():
    file = request.files['file']
    separator = request.form['separator']
    stats = get_stats(file, separator)
    print('***** FILE *****')
    print(type(file), separator)
    return render_template('csv_stats_return.html', tables=[stats.to_html(classes='data')], title=str(file).split("'")[1])

@app.route('/draw')
def draw():
    return render_template('draw.html')

@app.route('/draw', methods=['POST'])
def predict_img():
    dataURL = request.form['data_url']
    tools.save_img(dataURL)
    img = tools.img_to_arr().flatten().reshape(1,-1)
    digit = model.predict(img)

    return render_template('draw_return.html', digit=digit)

if __name__ == '__main__':
    app.run()