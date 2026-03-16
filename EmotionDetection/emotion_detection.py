import requests
import json

def emotion_detector(text_to_analyze):
    response = requests.post('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
                              headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
                              json = {"raw_document": { "text": text_to_analyze } })
    formatted_text = json.loads(response.text)
    emotion = formatted_text['emotionPredictions'][0]['emotion']
    anger_score = emotion.get('anger')
    disgust_score = emotion.get('disgust')
    fear_score = emotion.get('fear')
    joy_score = emotion.get('joy')
    sadness_score = emotion.get('sadness')
    dominant_emotion = max(emotion, key=emotion.get)
    return { 'anger': anger_score,
             'disgust': disgust_score,
             'fear': fear_score,
             'joy': joy_score,
             'sadness': sadness_score,
             'dominant_emotion': dominant_emotion
             }