from sklearn.feature_extraction.text import TfidfVectorizer
import io
import unidecode
import pickle
import os

class LoadTfidf :
    def __init__(self):
        print("Chargement du modele tfidf...")
        self.content_list = self.content_list_load()
        # self.content_list_tokenized = self.content_list_tokenized_load()
        self.path_list = self.path_list_load()
        self.tfidf_model_fited = self.tfidf_model_fited_load()
        self.sklearn_tfidf = self.sklearn_tfidf_load()
        print("Done.")

    def content_list_load(self):
        content_list = []
        cwd = os.getcwd()
        cwd = "\\".join(cwd.split("\\")[:-1])
        data_path = cwd + "\\data\\content_list.pkl"
        with open(data_path, "rb") as f:
            content_list = pickle.load(f)
        return content_list

    def path_list_load(self):
        path_list = []
        cwd = os.getcwd()
        cwd = "\\".join(cwd.split("\\")[:-1])
        data_path = cwd + "\\data\\path_list.pkl"
        with open(data_path, "rb") as f:
            path_list = pickle.load(f)
        return path_list

    def tfidf_model_fited_load(self):
        cwd = os.getcwd()
        cwd = "\\".join(cwd.split("\\")[:-1])
        data_path = cwd + "\\data\\tfidf_model_fited.pkl"
        with open(data_path, "rb") as f:
            tfidf_model_fited = pickle.load(f)
        return tfidf_model_fited

    def sklearn_tfidf_load(self):
        cwd = os.getcwd()
        cwd = "\\".join(cwd.split("\\")[:-1])
        data_path = cwd + "\\data\\sklearn_tfidf.pkl"
        with open(data_path, "rb") as f:
            sklearn_tfidf = pickle.load(f)
        return sklearn_tfidf
