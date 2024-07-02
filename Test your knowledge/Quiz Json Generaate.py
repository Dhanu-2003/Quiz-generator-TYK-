"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""
import json
import google.generativeai as genai

genai.configure(api_key="AIzaSyDxu8aIqEc_k8LG37XiDePSTA2hrAeM59o")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

response = model.generate_content([
  "input: Generate {} MCQ on the subject {} title {} for grade {} ".format(int(input("Number of Questions : ")),input("Subject : "),input("Title : "),input("Grade : ")),
  "output:{{Question:Question,option:[option a,option b,option c,option d],answer:optionNo},{Question:Question,option:[option a,option b,option c,option d],answer:optionNo}{Question:Question,option:[option a,option b,option c,option d],answer:optionNo}{Question:Question,option:[option a,option b,option c,option d],answer:optionNo}....... }",
])

data = response.text
print(data)
""" json_formatted_str = json.dumps(obj, indent=4)
print(json_formatted_str) """