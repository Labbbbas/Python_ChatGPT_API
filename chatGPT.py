# No va a servir si no upgradeamos a la versión plus :(

# Antes se debe instalar: pip3 install openai

import openai

openai.api_key = ""     # Se obtiene de: https://platform.openai.com/ > Personal > View API keys > Create new secret key

completion = openai.Completion.create(engine="text-davinci-003", 
                        prompt="¿Qué es ChatGPT?",
                        max_tokens="2048")

print(completion.choices[0].text)