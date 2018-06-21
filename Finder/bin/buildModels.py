
import os
import sys

# On a rajouté le chemin au sys.path pour que le code tourne sur le script
sys.path.insert(0,"\\".join(os.getcwd().split("\\")[:-1]))
from bin.classes.BuildTfidf import BuildTfidf


cwd = os.getcwd()
cwd = "\\".join(cwd.split("\\")[:-1])
data_path = cwd + "\\data\\final_only_doc_without_lemma.txt"
# Autre maniere de definir le path
# script_path = os.path.abspath(__file__)
# script_dir = os.path.split(script_path)[0]
# rel_path = "data"
# data_path = os.path.join(script_dir, "../", rel_path + "/final_only_doc_without_lemma.txt/")

build = BuildTfidf(data_path)
