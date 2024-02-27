from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def mission_title():
    return "Миссия Колонизация Марса"


@app.route('/index')
def mission_motto():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def advertising_campaign():
    promotion = ["Человечество вырастает из детства.",
                 "Человечеству мала одна планета.",
                 "Мы сделаем обитаемыми безжизненные пока планеты.",
                 "И начнем с Марса!", "Присоединяйся!"]
    return '</br>'.join(promotion)


@app.route('/image_mars')
def mars_image():
    return render_template('mars.html')


if __name__ == '__main__':
    app.run(port=8090, host='127.0.0.1')
