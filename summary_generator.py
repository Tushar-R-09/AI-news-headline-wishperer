import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import re

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu") #For Apple Silicon Macs
#device = torch.device("cuda" if torch.cuda.is_available() else "cpu") # For windows users

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
model = model.to(device)

summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, device=-1)


# Function to clean text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text).strip() #Removes the white space
    return text

def summarize_text(text):
    cleaned_text = clean_text(text)
    summary = summarizer(cleaned_text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    return summary