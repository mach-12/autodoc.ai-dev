import openai

prompt3 = ""


def getExplanation(prompt, tokens):
    """
    Calling the OpenAI API
    """

    # Set the API key
    openai.api_key = "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"
    # openai.api_key = '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'

    parameters = {
        'model' : "text-davinci-003",
        'prompt' : prompt,
        'temperature' : 1,
        'max_tokens' : tokens
    }

    # Call the API and get the response
    response = openai.Completion.create(**parameters)

    # Extract the generated text from the response
    generated_text = response.choices[0].text

    return generated_text


def buildDoc(repo):
    prompt1 = f"give a minimal code documentation of files from {repo} format: Name, Short description, parameters, return values. In markdown format."
    prompt1_result = getExplanation(prompt1, 2000)

    prompt2 = f"List all directories ignoring .py files from {prompt1_result} as comma separated Github URL"

    return prompt1_result
