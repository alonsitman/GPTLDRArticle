# GPT Sanity check - "What is the most populated country in the world?"

from newspaper import Article

import sys
import path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
import GPTLDRCore.gptldr_core as gptldr_core


def validate_url(url):
    
    space = ' '
    if space in url:
        return False    
    
    return True


def get_article(url): #using newspaper module

    article = Article(url)
    article.download()
    article.parse()
    
    return article


def extract_title(article):
    
    title = article.title
    
    return title


def extract_text(article):
    
    text = article.text #perhaps it should be article.text
    
    return text


def extract_title_text(url):

    # Check that the URL is vald:
    if not validate_url(url):
        print("Please insert URL without spaces") 
        return None
   
    # Download and parse the article:
    article = get_article(url)
    
    # Extract title and text from article + tldr configurations from JSON:
    title = extract_title(article)
    text = extract_text(article)

    return title, text


def run(url):
    title, text = extract_title_text(url)
    gptldr_core.run(title, text)