from flask import Flask, render_template, request, jsonify
import subprocess
app = Flask(__name__, template_folder='Templates')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Contact')
def contact():
    return render_template('Contact.html')

@app.route('/About')
def about():
    return render_template('About.html')

@app.route('/run-script')
def run_script():
    try:
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
        return jsonify({'output': result.stdout})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
