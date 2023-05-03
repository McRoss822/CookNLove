from django.shortcuts import render
import openai
from cooknlove.settings import OPENAI_API_KEY 

apiKey=OPENAI_API_KEY

def aiResponse(request):
     response=None
     if apiKey is not None and request.method == 'POST':
        openai.api_key = apiKey
        userInput = request.POST.get('user-input')
        prompt=userInput

        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens = 256
        )
        print(response)
        return render(request, 'index.html')
     else:
         print("tu loh")