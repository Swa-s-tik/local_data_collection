from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    prompt = request.form['prompt']
    commands = request.form['commands']
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([prompt, commands])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
