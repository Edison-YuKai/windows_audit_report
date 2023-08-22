from flask import Flask, render_template, url_for
import plotly.express as px
import pandas as pd
import plotly.offline as pyo
from jinja2 import Environment, FileSystemLoader
from tabulate import tabulate

# Create a Flask app instance
app = Flask(__name__, static_folder='static')

# Sample data
data = {
    'Category': ['Successful Remediations', 'Failed Remediations'],
    'Value': [35, 25]
}

df = pd.DataFrame(data)

# Create a pie chart
fig = px.pie(df, values='Value', names='Category', title='Remediations Summary')

# Generate HTML code for the chart
chart_html = pyo.plot(fig, output_type='div')

# Define your Flask routes
@app.route("/")
def index():
    # Create a Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))

    # Load the template
    index_template = env.get_template('index.html')

    # Render the template with the chart HTML
    rendered_template = index_template.render(chart_html=chart_html, url_for=url_for)

    return rendered_template

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
