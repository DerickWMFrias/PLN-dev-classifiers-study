import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

def printhello():
    print("HELLO!")


""" ESTA CLASSE NÃO ESTA SENDO UTILIZADA NO EP1

ISSUES: A implementação, para ser compativel com SKLearn Pipelines, tem de implementar os métodos: 'fit' e 'transform'.
Logo, essa classe ainda não pode ser usada nas Pipelines de treinamento, pois sua logica não esta resolvida p/ esses "gateways". 
"""

class NLP_feature_maker():
    """
    Esta classe recebe a referência para um dataframe e fornece métodos
    para gerar diferentes representações textuais (BoW, TF, TF-IDF, N-Gram).
    """
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def makeBoW(self, feature_column: str):
        """
        Gera matriz Bag of Words (contagem bruta de tokens).
        """
        count_vect = CountVectorizer()
        X = count_vect.fit_transform(self.df[feature_column].fillna("")) # features
        return X, count_vect

    def makeTF(self, feature_column: str):
        """
        Gera matriz de Term Frequency (TF).
        Cada valor representa a frequência normalizada de cada termo.
        """
        count_vect = CountVectorizer()
        X_train_counts = count_vect.fit_transform(self.df[feature_column].fillna(""))

        tf_transformer = TfidfTransformer()
        X = tf_transformer.fit_transform(X_train_counts, use_idf=False)

        return X, count_vect

    def makeTF_IDF(self, feature_column: str):
        """
        Gera matriz TF-IDF (Term Frequency – Inverse Document Frequency).
        Reduz a importância de termos muito frequentes e comuns.
        """
        count_vect = CountVectorizer()
        X_train_counts = count_vect.fit_transform(self.df[feature_column].fillna(""))

        tf_transformer = TfidfTransformer()
        X = tf_transformer.fit_transform(X_train_counts, use_idf=True)

        return X, count_vect

    def makeNGramsWord(self, feature_column: str, N_lo: int, N_hi: int):
        """
        Gera matriz Bag of N-Grams (unigramas, bigramas, trigramas, etc.).
        Exemplo: N=2 -> bigramas, N=3 -> trigramas.
        """
        count_vect = CountVectorizer(ngram_range=(N_lo, N_hi), analyzer="word")
        X = count_vect.fit_transform(self.df[feature_column].fillna(""))
        return X, count_vect
    
    def makeNGramsChar(self, feature_column: str, N_lo: int, N_hi: int):
        """
        Gera matriz Bag of N-Grams (unigramas, bigramas, trigramas, etc.).
        Exemplo: N=2 -> bigramas, N=3 -> trigramas.
        """
        count_vect = CountVectorizer(ngram_range=(N_lo, N_hi), analyzer="char")
        X = count_vect.fit_transform(self.df[feature_column].fillna(""))
        return X, count_vect

    def fit(self, mode:str = "BoW"):
        return mode

    def transform(self):
        pass

    def selectTrainLabels(self, label_column: str):
        y = self.df[label_column].values
        return y
