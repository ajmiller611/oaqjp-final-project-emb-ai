import requests
import json

def emotion_detector(text_to_analyse):
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotions_dict = formatted_response['emotionPredictions'][0]['emotion']
    elif response.status_code == 400:
        emotions_dict = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None}

    anger_score = emotions_dict['anger']
    disgust_score = emotions_dict['disgust']
    fear_score = emotions_dict['fear']
    joy_score = emotions_dict['joy']
    sadness_score = emotions_dict['sadness']
    
    scores_list = emotions_dict.values()
    # Check for all elements in the scores list to have type None
    if not all(isinstance(value, type(None)) for value in scores_list):
        max_score = max(scores_list)

        for key, value in emotions_dict.items():
            if value == max_score:
                dominant_emotion = key
    else:
        dominant_emotion = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
        }