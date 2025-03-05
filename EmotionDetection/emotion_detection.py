import json
import requests
"""
This is a emotion detection module
"""
def emotion_detector(text_to_analyse):
    """
    This function calls the iBM watson emotion detector model and returns the response
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    anger = None 
    disgust = None
    fear = None
    joy = None
    sadness = None
    dominant_emotion = None
    if response.status_code == 200:
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        for emo, score in formatted_response['emotionPredictions'][0]['emotion'].items():
            if score == max(formatted_response['emotionPredictions'][0]['emotion'].values()):
                dominant_emotion = emo 
    # If the response status code is 500, set label and score to None
    elif response.status_code == 400:
        anger = None 
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None
        formatted_response1 = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}
    return formatted_response1
