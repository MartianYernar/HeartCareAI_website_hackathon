from flask import Flask, render_template, request, jsonify
# import sqlite3
from ultralytics import YOLO
import openai
from openai import OpenAI
# import os

app = Flask(__name__)
model = YOLO('static/best.pt')

client = OpenAI()
# openai.api_key = 'sk-PBSrhB4qmYRsM_8PDaMaa-YZPMciFl3fQNtc9rGxjaT3BlbkFJGyDkXQdaJ1EA91AMINtJWFRZ3s3UxL7clAp60KqIcA'
openai.api_key = "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"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload-xray', methods=['POST'])
def upload_xray():
    file = request.files['xray']
    if file.filename == '':
        return jsonify({'message': 'No selected file'})
    file.save('static/saved.jpg')
    
    results = model('static/saved.png')
    for result in results:
        id = result.probs.top1
    name = result.names[id]
    

    return jsonify({'message': name, 'image_url': 'static/saved.jpg'})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')

    if not user_message:
        return jsonify({'reply': 'Sorry, I didn\'t understand your request.'})
    
    try:
        completion = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages = [
                {'role': 'system', 'content': 'You are kind doctor, medicine professional'},
                {'role': 'user', 'content': user_message}
            ]
        )

        
        reply = completion.choices[0].message.content.strip()
        return jsonify({'reply': reply})

    except Exception as e:
        print(e)
        return jsonify({'reply': f'An error occurred: {str(e)}'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
