import text_extraction
import torch
import transformers
import sentence_transformers
from sentence_transformers import SentenceTransformer

import sklearn
from sklearn.metrics.pairwise import cosine_similarity
import scipy
from scipy.spatial.distance import cosine
import pandas as pd
import os

def Gatello_smart_matching(link_joboffer,link_resume):
    
    model=SentenceTransformer('paraphrase-distilroberta-base-v1')
    #joboffer part
    filename_j, file_extension_j = os.path.splitext(link_joboffer)
    doc_j = text_extraction.extract_text(link_joboffer,file_extension_j)
    doc_embedding_j= model.encode([doc_j])

    #resume part
    filename_r, file_extension_r = os.path.splitext(link_resume)
    doc_r = text_extraction.extract_text(link_resume,file_extension_r)
    doc_embedding_r= model.encode([doc_r])
    
    distance=cosine_similarity(doc_embedding_j,doc_embedding_r)
    
    return round(distance[0][0]*100)
    