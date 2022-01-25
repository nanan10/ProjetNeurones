import streamlit as st
import pandas as pd

def welcome():
    img,imm,imd = st.columns(3)
    with img:
        st.image("images/idsi.jpg")

    with imm:
        st.title("  ")

    with imd:
        st.image("images/rn.jpg")

    st.title("PROJET RESEAU DE NEURONES")
    st.write('''
    
 
L’institut National de la Statistique a effectué un recensement des ménages et des individus qui vivent dans ces ménages, seulement elle fait face à un problème de données manquantes sur trois (03) des vingt-quatre variables observées. Pour cela elle dispose d’un fichier au format cvs appelé « Habitat » contenant 1 002 579 lignes.  
Vous êtes sollicités pour résoudre le problème : 
##### Aider l’INS à faire une prédiction pour toutes les observations ayant une donnée manquante ; 
#####	Proposer des dashboard qui présenteront :  
-	la répartition des chefs de ménages par arrondissement selon leur âge ; 
-	la répartition des chefs de ménages par arrondissement selon leur diplôme le plus élevé ; 
-	la répartition des ménages par arrondissement selon le milieu de résidence ; 
- la répartition des ménages par arrondissement selon l’état matrimoniale ; 
- la répartition des ménages par arrondissement selon l’état de santé ; 
-	la répartition des ménages par arrondissement selon la pratique d’une activité agropastorale ; 
-	la répartition des ménages par arrondissement selon la religion, le nombre de langue parlé et le nombre d’enfant ; 
-	la répartition des ménages par arrondissement selon le type de structure ;
- la répartition des ménages par arrondissement selon le statut d’occupation et selon que le  répondant est autochtone ou pas. 

    
    
    
    
    ''')
