from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    id_user = StringField('ID астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = StringField('ID капитана', validators=[DataRequired()])
    token = PasswordField('Токен капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/')
def basement():
    return render_template('base.html', title='страницы чтоб без ошибки')

@app.route('/<a>')
@app.route('/index/<a>')
def first(a):
    return render_template('base.html', title=a)


@app.route('/success')
def success():
    return render_template('success.html', key=1)

@app.route('/unsuccess')
def unsuccess():
    return render_template('success.html', key=0)

@app.route('/training/<prof>')
def training(prof):
    profession = prof
    if 'инженер' in prof:
        profession = 'инженер'
    elif 'строитель' in prof:
        profession = 'строитель'
    else:
        profession = prof 
    
    return render_template('training.html', prof=profession)


@app.route('/list_prof/<a>')
def list_prof(a):
    list_of_prof = ['шут', 'музыкант', 'учитель', 'строитель', 'депутат']
    return render_template('list_prof.html', list=a, job_list=list_of_prof)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    title = 'анкета'
    surname = 'бобов'
    name = 'боб'
    education = 'бобовое'
    profession = 'бобоист'
    sex = 'бобоин'
    motivation = 'мечтаю заниматься бобоением'
    ready = 'БОБ-ТРУ'
    Dict = {'Заголовок': title, 'Фамилия': surname, 'Имя': name,'Образование': education,
            'Профессия': profession, 'Пол': sex, 'Мотивация': motivation, 'Готовы остаться на Марсе?': ready}
    
    return render_template('auto_answer.html', Dict=Dict)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    spis = ['Альберт', 'Крис', 'Анам', 'Эндриу', 'неТейт']
    return render_template('distribution.html', spis=spis)


@app.route('/table/<sex>/<age>')
def tables(sex, age):
    if not age.isdigit():
        return
    else:
        if sex == "male" and int(age) < 21:
            count = 1
        elif sex == "female" and int(age) < 21:
            count = 2
        elif sex == "male" and int(age) >= 21:
            count = 3
        elif sex == "female" and int(age) >= 21:
            count = 4
        else:
            count = 5
        return render_template('table.html', type=count)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')