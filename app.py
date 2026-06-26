from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
from openai import OpenAI

app = Flask(__name__)
model = YOLO('static/best.pt')

client = OpenAI()  # reads OPENAI_API_KEY from the environment


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
