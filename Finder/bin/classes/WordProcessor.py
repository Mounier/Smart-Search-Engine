import re
import os
import sys
import unidecode

class WordProcessor:
    def process(self, query_list):
        cwd = os.getcwd()
        cwd = "\\".join(cwd.split("\\")[:-1])
        data_path = cwd + "\\data\\stopwords-fr.txt"
        with open(data_path,encoding='utf-8') as f:
            stop = f.read().splitlines()
        new_query = query_list[0].lower() # met tout en minuscule
        new_query = unidecode.unidecode(new_query) # remplace tous les accents par un espace
        new_query = re.sub('[^\w]',' ', new_query) # remplace tous les caractères spéciaux par un espace
        new_query = re.sub('\d+',' ', new_query) # remplace tous les nombres par des espaces
        new_query = re.sub(' +',' ', new_query) # remplaces tous les 2 ou plus espaces par un espace
        new_query = [i for i in new_query.split() if i not in stop]
        new_query = [i for i in new_query if len(i)>2]
        new_query = " ".join(new_query)
        new_query_list = []
        new_query_list.append(new_query)
        return new_query_list
