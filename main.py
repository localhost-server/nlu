import os
import streamlit as st

def layout():
    # with st.form("Home"):
    dashbrd ,NER, txtsmlrtymtrx, dpndnctree, clsifrs, tknfetrs, tknembd, sntnsembd, enttembd = st.tabs(
        ["Dashboard","NER","Text-Similarity-Matrix","Dependency-Tree","Classifiers","Token-Features","Token-Embedding-Manifolds","Sentence-Embedding-Manifolds","Entity-Embedding-Manifolds"])
    
    if dashbrd:
        with dashbrd:
            from examples.streamlit.dashboard import layout
            layout()

    if NER:
        with NER:
            from examples.streamlit.NER import layout
            layout()

    if txtsmlrtymtrx:
        with txtsmlrtymtrx:
            from examples.streamlit.text_similarity_matrix import layout
            layout()

    if dpndnctree:
        with dpndnctree:
            from examples.streamlit.dependency_tree import layout
            layout()

    if clsifrs:
        with clsifrs:
            from examples.streamlit.classifiers import layout
            layout()

    if tknfetrs:
        with tknfetrs:
            from examples.streamlit.token_features import layout
            layout()

    if tknembd:
        with tknembd:
            from examples.streamlit.token_embedding_manifolds import layout
            layout()

    if sntnsembd:
        with sntnsembd:
            from examples.streamlit.sentence_embedding_manifolds import layout
            layout()

    if enttembd:
        with enttembd:
            from examples.streamlit.entity_embedding_manifolds import layout
            layout()

if __name__ == '__main__':
    layout()