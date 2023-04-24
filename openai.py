# [0.0] install openai lib?
'''
!pip install openai
'''

# [0.1] import openai lib

import openai

# [1.0] API Key, and model

'''
You can get your API Key from this link 
https://beta.openai.com/account/api-keys
'''

openai.api_key = "your api"

model_engine = "text-davinci-002"

# [1.1] run your api and get ans

def _get_ans_from_response(response:openai.openai_object.OpenAIObject) -> str:
    first = dict(response)['choices']
    sec = dict(first[0])
    return sec['text']

def _getter(model_engine:str = model_engine,prompt:str = "") -> str:
    # Send the request to the Chat GPT API
    response = openai.Completion.create(
                          engine=model_engine,
                          prompt=prompt,
                          max_tokens=1024
                          )
    return _get_ans_from_response(response)

# [2] Done

print(_getter(prompt="what's Kaggle?"))

'''
output::
Kaggle is a platform for predictive modeling and analytics competitions in which companies and researchers post data and statisticians and data miners compete to produce the best models for predicting and describing the data.
'''