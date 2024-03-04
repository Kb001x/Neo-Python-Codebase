import os
import openai

# Get the API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')

# Check if the API key is not None
if api_key is None:
    print("The 'OPENAI_API_KEY' environment variable is not set.")
else:
    print("Your 'OPENAI_API_KEY' is set.")

    # Configure OpenAI library with your API key
    openai.api_key = api_key

    # Now you can make calls to OpenAI API
    try:
        # Just an example call to OpenAI API to list engines
        response = openai.models.list()
        print(response)
    except openai.AuthenticationError as e:
        print(f"An error occurred: {e}")
