import os
import sys
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# On a rajouté le chemin au sys.path pour que le code tourne sur le script
sys.path.insert(0,"\\".join(os.getcwd().split("\\")[:-1]))
from bin.classes.LoadTfidf import LoadTfidf
from bin.classes.WordProcessor import WordProcessor
from sklearn.metrics.pairwise import cosine_similarity

tfidf_load = LoadTfidf()
wordProcessor = WordProcessor()

queryList = ["ceci EST un test de COntentieux"]
queryList = wordProcessor.process(queryList)
print("requete transformé : " + str(queryList))

dataY = tfidf_load.tfidf_model_fited.toarray()
# calcul le score de tfidf pour chaque terme de la query
Y_query = tfidf_load.sklearn_tfidf.transform(queryList)

# Creation du vecteur tfidf de query_list, le vecteur est de taille du dictionnaire
# Pour chaque parametre du vecteur correspondant au terme du dictionnaire present dans la query_list on lui donne comme valeur
# son score de tfidf calculé plus haut
dataY_query = Y_query.toarray()[0]
concat = np.append(dataY, [dataY_query], axis=0)
cosine_score = cosine_similarity(concat, concat[-1].reshape(1, -1))
cosine_score = np.concatenate(cosine_score, axis=0)


# score_list = np.array(cosine_score)
# score_list = np.sort(score_list)
# # print(score_list[0:5])
# # print(score_list.argsort()[0:10])
# reversed_score_list = score_list[::-1]
# print(reversed_score_list[0:5])
# # print(reversed_score_list.argsort())
# print(cosine_score.argsort()[-10:][::-1][0:5])

top_id_list = []
# for numero in range(1, 10):
#     id_list.append(cosine_score.argsort()[-10:][::-1][numero])
for numero in range(1,len(cosine_score)):
    top_id_list.append(cosine_score.argsort()[:][::-1][numero])

print(top_id_list[0:10])

path_list = tfidf_load.path_list
result_list = []
top_score = []
for id in top_id_list:
    result_list.append(path_list[id])
    top_score.append(cosine_score[id])

# print(result_list[0:5])
print(top_score[0:5])



# print(the_list)
print(cosine_score[1879])
print(cosine_score[3566])
print(cosine_score[1908])
# path_list = tfidf_load.path_list
# print(path_list[1879])
