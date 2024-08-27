from groq import Groq
from dotenv import load_dotenv
from extractMarkdown import extract_markdown
import os


client = Groq(
    api_key = os.getenv('API_KEY')
)


def ask(query):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages= [
            {
                'role': 'user',
                'content': query
            } 
        ],
        temperature=0.7,
        max_tokens=1024,
        top_p=0.9,
        stream=False,
        stop=None
    )
    
    markdown_content = response.choices[0].message.content

    return extract_markdown(markdown_content)