''' 
Flask web server
'''
from flask import Flask, request,  render_template
from EmotionDetection.emotion_detection import emotion_detection

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    ''' render index page '''
    return render_template('index.html')

@app.route('/emotionDetector')
def display_response():
    ''' display emotions '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detection(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"


    anger = response['anger']
    sadness = response['sadness']
    fear = response['fear']
    joy = response['joy']
    disgust = response['disgust']
    dominant_emotion = response['dominant_emotion']

    return f'''
For the given statement, the system response is 'anger': \
{anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} \
and 'sadness': {sadness}. The dominant emotion is <b>{dominant_emotion}</b>.
'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
