from flask import Flask, render_template_string, send_file
import time

app = Flask(__name__)


@app.route('/<int:number>')
def index(number):
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta property="og:image" content="{{ url_for('og_image', number=number) }}">
    </head>
    <body>
        <h1>OG image loading should take {{number}} ms</h1>
    </body>
    </html>
    '''
    return render_template_string(html, number=number)


@app.route('/og/<int:number>')
def og_image(number):
    time.sleep(number / 1000.0)  # Delay in seconds
    return send_file('static/og_image.jpg', mimetype='image/jpeg')


if __name__ == '__main__':
    app.run()
