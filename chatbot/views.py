import google.generativeai as genai
from decouple import config
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


genai.configure(api_key=config('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

@api_view(['POST'])
def chat(request):
    user_msg = request.data.get('message')
    if not user_msg:
        return Response({
            'success':False,
            'error':'Message is required'
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        chat = model.start_chat()
        response = chat.send_message(user_msg)
        bot_resp = response.text

        return Response({
            'success':True,
            'response':bot_resp
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'error':f'An error occurred: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
