from flask import Flask, request, url_for, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return('<h1>Hola Mundo!<h1>')

# GET, POST, PUT, PATCH, DELETE
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def lala(post_id):
    if request.method == 'GET':
        return 'El id del post es: '+ post_id
    else:
        return 'Este es otro método y no GET'

# @app.route('/post/<post_id>', methods=['POST'])
# def lili(post_id):
#     return 'El id del post es: '+ post_id

@app.route('/lele', methods=['POST', 'GET'])
def lele():
    return redirect(url_for('lala', post_id = 2))
    # print(url_for('lala', post_id = 2))
    # print(request.form)
    # print(request.form['llave1'])
    # print(request.form['llave2'])
    return('lele')

# if __name__ == "__main__":
#     app.run(debug=True, port=3000)