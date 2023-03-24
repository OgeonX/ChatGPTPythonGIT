import openai
import config

# Load OpenAI API key from config file
openai.api_key = config.OPENAI_API_KEY

def generate_response(context, user_input):
    # Call OpenAI API to generate a response
    response = openai.Completion.create(
        engine="davinci",
        prompt="Context: {}\n\nUser Input: {}".format(context, user_input),
        max_tokens=2000,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n", " Human:", " AI:"],
        n=1,
    )
    return response.choices[0].text.strip()
