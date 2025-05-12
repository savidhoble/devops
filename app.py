from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        return f"Thank you, {name}! You have registered with email: {email}"
    return render_template('register.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
