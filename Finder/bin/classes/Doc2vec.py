import os
import string
import re
import string
import math
import json
import sys
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import gensim
from gensim.models import doc2vec
from collections import namedtuple
import random
from os.path import expanduser
import io
import unidecode
home = expanduser("~")
print(home)

class Doc2vec:
    def __init__(self, Filename, model):
        # self.Donnee,self.IdDonnee,self.ContDonnee = self.Transfo_File()

        # self.Regroup(self.ContDonnee,Filename)
        self.Travaux = self.Fichier_Travail(Filename)
        # self.Model_TF_IDF = self.TF_IDF(self.Travaux)
        print("chargement du model : " + model)
        self.Model_Doc2Vec = gensim.models.doc2vec.Doc2Vec.load(model)
        # self.Model_Doc2Vec_moyenneVec = self.DOC2VEC_moyenneVec(self.Travaux)

    def Transfo_File(self):
        path = "fichier"
        donnus = [open(path + "/" + f).read().split('&&&') for f in os.listdir(path)]
        donnus = np.array(donnus)

        IdDoc = [i[0] for i in donnus if len(i) > 1]
        ContDoc = [i[1] for i in donnus if len(i) > 1]
        for i in range(0, len(IdDoc)):
            IdDoc[i] = IdDoc[i][:-1]

        return donnus, IdDoc, ContDoc

    def Nettoyage(self, fichier):
        with open('stop3.txt', encoding='utf-8') as f:
            stop = f.read().splitlines()

        ponctu = re.sub("\W", " ", fichier).lower()
        accent = unidecode.unidecode(ponctu)
        doublespace = re.sub(' +', ' ', accent)
        tiret_ = re.sub('_', ' ', doublespace)
        chiffre = re.sub("\d+", " ", tiret_)
        retire_stop = [i for i in chiffre.lower().split() if i not in stop]
        reliure = ' '.join(retire_stop)
        return reliure

    def Regroup(self, Documents, Filename):
        f = open(Filename, 'w')
        for i in Documents:
            f.write((self.Nettoyage(i)))
            f.write('\n')
        f.close()

    def Fichier_Travail(self, Filename):
        with open(Filename, encoding='utf-8') as f:
            Travaux = f.read().splitlines()
        return Travaux

    def DOC2VEC_moyenneVec(self, Travaux):
        Vector = [i.split(" ") for i in Travaux]

        Vectoriseur = []
        for i in Vector:
            Vectorise = []
            for j in i:
                Vectorise.append(self.Model_Doc2Vec.wv[j])
            Vectoriseur.append(Vectorise)
        DataUse = np.array(Vectoriseur)

        VectorSortie = []
        for i in Vectoriseur:
            VectorSortie.append(np.array(i).mean(axis=0))

        return VectorSortie

    def TF_IDF(self, Travaux):
        tokenize = lambda doc: doc.lower().split(" ")
        sklearn_tfidf = TfidfVectorizer(norm='l2', min_df=0, use_idf=True, smooth_idf=False, sublinear_tf=True,
                                        tokenizer=tokenize)
        sklearn_representation = sklearn_tfidf.fit_transform(Travaux)
        return sklearn_representation

    def Doc2VEC(self, Travaux, nb_passes, models,
                size):  # /!\ argument size ou vector_size, depend de la version gensim
        doc1 = Travaux
        docs = []
        analyzedDocument = namedtuple('AnalyzedDocument', 'words tags')

        for i, text in enumerate(doc1):
            words = text.lower().split()
            tags = [i]
            # print(tags)
            docs.append(analyzedDocument(words, tags))

        return model