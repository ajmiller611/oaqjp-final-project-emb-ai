import requests
import json

def emotion_detector(text_to_analyse):
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotions_dict = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions_dict['anger']
    disgust_score = emotions_dict['disgust']
    fear_score = emotions_dict['fear']
    joy_score = emotions_dict['joy']
    sadness_score = emotions_dict['sadness']
    
    scores_dict = emotions_dict.values()
    max_score = max(scores_dict)

    for key, value in emotions_dict.items():
        if value == max_score:
            dominant_emotion = key

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
        }