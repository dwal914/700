import openai
import json

def get_api_key(file_path="testkey.txt"):
    """Read API key from a file."""
    with open(file_path, "r") as file:
        return file.read().strip()

def call_chatgpt(prompt, model="gpt-4o", temperature=0.7):
    """Send a prompt to the ChatGPT API and return the response."""
    api_key = get_api_key()
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": "You are an expert engineer."},
                  {"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message.content

def process_prompts(input_file="prompts.txt", output_file="answers.json"):
    """Read prompts from a file, get responses, and save them to a JSON file."""
    with open(input_file, "r", encoding="utf-8") as infile:
        prompts = [line.strip() for line in infile if line.strip()]
    
    responses = {prompt: call_chatgpt(prompt) for prompt in prompts}
    
    with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(responses, outfile, indent=4)

if __name__ == "__main__":
    process_prompts()
