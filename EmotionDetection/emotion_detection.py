import requests

def emotion_detection(text_to_analyse):
    '''a function to check the text sentiment '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, headers=headers, json = input_json)
    
    output_json = response.json()["emotionPredictions"][0]["emotion"]

    dominant_emotion = max(output_json, key = lambda key: output_json[key])
    output_json['dominant_emotion'] = dominant_emotion
    
    return output_json
