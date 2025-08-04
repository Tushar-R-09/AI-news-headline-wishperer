from newspaper import Article
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import re

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
model = model.to(device)

summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, device=-1)


# Function to extract and summarize article
def get_summary(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text
        if not text:
            return "Error: Could not extract text from the article."
        
        # Clean and limit text length for summarization
        text = clean_text(text)
        max_input_length = 1024  # BART's max input length
        text = text[:max_input_length]
        
        # Summarize the text
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
        return summary
    except Exception as e:
        return f"Error processing article: {str(e)}"
    
# Function to clean text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text).strip()
    return text