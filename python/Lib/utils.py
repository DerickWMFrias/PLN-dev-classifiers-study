import pandas as pd
import numpy as np
import re

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

def printhello():
    print("HELLO!")


def clean_text(text, do_lowercase: bool, rem_emails: bool, rem_urls: bool, normalize_whitespaces: bool):
    """
    Esta função recebe um texto - supostamente advindo de uma coluna de um dataframe - e aplica
    algumas operações de limpeza de dados sobre o texto. Notadamente
    """
    if not isinstance(text, str):
        return "" 
    
    # Converte tudo para minúsculas
    if do_lowercase:
        text = text.lower()
    
    # Remove endereços de e-mail (regex simples para e-mail)
    if rem_emails:
        text = re.sub(r'\S*@\S*\s?', '', text)
    
    # Remove URLs (regex simples para URLs http/https)
    if rem_urls:
        text = re.sub(r'http\S+|https\S+', '', text)
    
    # Remove espaços em branco extras (normaliza a formatação)
    if normalize_whitespaces:
        text = re.sub(r'\s+', ' ', text).strip()
    
    return text


