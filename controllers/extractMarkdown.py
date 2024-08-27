import re

def extract_markdown(markdown_content):
    # Regex to find all code blocks enclosed in triple backticks
    code_blocks = re.findall(r'%%%(.*?)%%%', markdown_content, re.DOTALL)
    return '\n\n'.join(code_blocks)