from sklearn.feature_extraction.text import TfidfVectorizer
import io
import unidecode
import pickle
import os

class BuildTfidf :
    def __init__(self,filename):
        print("Construction des listes...")
        self.content_list = self.content_list_build(filename)
        self.path_list = self.path_list_build(filename)
        print("Done.")
        print("Construction du modèle tfidf...")
        self.tfidf_model = self.tfidf_model_build(self.content_list)[0]
        self.sklearn_tfidf = self.tfidf_model_build(self.content_list)[1]
        print("Done.")

    def content_list_build(self,filename):
        content_list = []
        with io.open(filename, "r", encoding="utf-8") as f:
            for l in f.readlines():
                content_list.append(l.split("?*?")[1])
        cwd = os.getcwd()
        cwd = "\\".join(cwd.split("\\")[:-1])
        data_path = cwd + "\\data\\content_list.pkl"
        with open(data_path, "wb") as f:
            pickle.dump(content_list,f)
        return content_list

    def path_list_build(self,filename):
        path_list = []
        with io.open(filename,"r",encoding="utf-8") as f:
            for l in f.readlines():
                path_list.append(l.split("?*?")[0])
        cwd = os.getcwd()
        cwd = "\\".join(cwd.split("\\")[:-1])
        data_path = cwd + "\\data\\path_list.pkl"
        with open(data_path, "wb") as f:
            pickle.dump(path_list,f)
        return path_list

    # pour le parametre tokenizer de TfidfVectorizer. Si on ne fait pas comme ça il est impossible de pickle le sklearn_tfidf
    def myFunc(self, test):
        return test.lower().split(" ")

    def tfidf_model_build(self,content_list):
        sklearn_tfidf = TfidfVectorizer(norm='l2', min_df=15, max_df=0.8, use_idf=True, smooth_idf=False, sublinear_tf=True, tokenizer=self.myFunc)
        tfidf_model_fited = sklearn_tfidf.fit_transform(content_list)
        cwd = os.getcwd()
        cwd = "\\".join(cwd.split("\\")[:-1])
        data_path = cwd + "\\data\\tfidf_model_fited.pkl"
        with open(data_path, "wb") as f:
            pickle.dump(tfidf_model_fited, f)
        data_path = cwd + "\\data\\sklearn_tfidf.pkl"
        with open(data_path, "wb") as f:
            pickle.dump(sklearn_tfidf, f, protocol=pickle.HIGHEST_PROTOCOL)
        return tfidf_model_fited, sklearn_tfidf
