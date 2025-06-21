# flask_routing_assignment
A simple Flask web application that demonstrates web page routing and HTML template rendering. This project includes routes for a home page, about page, contact page with a form, and an optional name submission form. The application uses Flask routes to handle GET and POST requests and renders Jinja-based templates for each page.
# Flask Routing Web App

This project demonstrates basic Flask routing and template rendering for IT112 Spring 2025. It includes:

- `/` – Home Page  
- `/about` – About Page  
- `/contact` – Contact Page with form handling (GET/POST)  
- `/name` – Optional Flask-WTF name form

Each route renders a corresponding HTML file from the `templates/` folder.

## Technologies Used
- Python 3
- Flask
- Jinja2 Templates
- (Optional) Flask-WTF

## How Routing Works
Flask uses the `@app.route` decorator to match a URL to a view function. When a URL is visited in the browser, Flask runs the associated function and renders the corresponding HTML template.
