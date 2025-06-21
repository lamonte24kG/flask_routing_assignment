from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#initialize the Flask application
app = Flask(__name__)

# Set a secret key for the application
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Define a simple form using Flask-WTF
class NameForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/name', methods=['GET', 'POST'])
def name():
    # Create an instance of the form
    form = NameForm()
    # Check if the form is submitted and valid
    if form.validate_on_submit():
        print("Rendering /name route")  # ← Add this
        return f"Hello, {form.name.data}!"
    # Render the form template
    return render_template('name.html', form=form)

# Define a route for the home page
@app.route('/')
def home():
    # Render the home page template
    return render_template('home.html')

# Define a route for the about page
@app.route('/about')
def about():
    # Render the about page template
    return render_template('about.html')

# Define a route for the contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return f"Thanks {name}, your message has been received!"
    return render_template('contact.html')


# Run the application
if __name__ == '__main__':
    app.run(debug=True)

# This code initializes a Flask application with four routes:
# - Home (/)
# - About (/about)
# - Contact (/contact)
# - Name form (/name)
# Each route renders a corresponding HTML template or handles form data.