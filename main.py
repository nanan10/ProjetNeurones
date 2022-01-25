import streamlit as st
import pandas as pd
import numpy as np
from copy import deepcopy
#from tensorflow.keras.utils import to_categorical
from Dashboard import Tableau_de_Bord
from Accueil import welcome


EnteteProcessing = st.container()
Agro = st.container()
Lien_parente = st.container()
Type_structure = st.container()
Status_occupation = st.container()
Reconstruction = st.container()


def main():
    selected_box = st.sidebar.selectbox(
        'Choisir une des options',
        ('Bienvenue',"Preprocessing","Dashboard")
    )
    if selected_box == "Bienvenue":
        welcome()
    if selected_box == "Preprocessing":
        Traitement()
    if selected_box == "Dashboard":
        Tableau_de_Bord()

def Traitement():
    with EnteteProcessing:
        st.title('PREDICTION DES DONNEES MANQUANTES')
        st.write('Le but de ce travail est de prédire les valeurs '
                 'manquantes de notre jeu de données en utilisant'
                 ' les réseaux de neurones.'
                 ' Pour des raisons de compréhension,'
                 ' nous expliquerons les différents codes pour'
                 ' les variables dont nous allons faire le traitement.')

        st.markdown('---')
        df = pd.read_csv("Habitat.csv", sep=";", encoding='latin1')
        df = df.loc[1:]
        st.dataframe(df.head())

        st.write('''** Ce dataframe  Habitat ** : est composé de :''', df.shape[0], ''' Obserbations
                  et de ''', df.shape[1], '''Variables''')
        st.write("Nous remarquons que nous avons plusieurs valeurs manquantes qui se présente comme suite : ")
        st.dataframe(df.isna().sum().sort_values(ascending=False))

        st.text(''
                ''
                ''
                ''
                ''
                '')

        st.write('Les variables ayant des valeurs manquantes sont :')
        st.write(' **Type de structure** , **Arrondissement** , **Statut d occupation** , ** Lien Parenté**')
        st.write('Par ailleurs, nous remarquons que la variable **Activité Agropastorale**'
                 ' a 12 valeurs manquantes. '
                 'Nous allons imputer ces '
                 'valeurs manquante par la moyenne.')

    with Agro:
        st.write('''
           #### Activité Agropastorale
         ''')
        st.image("images/Agro.PNG")
        st.write('''
        nous allons imputer ces valeurs manquante par la moyenne qui est 1
        ''')
        df["Activité Agropastorale"].fillna(1, inplace=True)
        st.dataframe(df.isna().sum().sort_values(ascending=False))

        st.write('''
        Pour déterminer les valeurs manquantes, nous allons procéder variables après variables. 
        Ce qui signifie que pour chaque variable dont nous voulons prédire les valeurs manquantes, 
        nous allons élaborer un réseau de neurones. Et supprimer les autres variables ayant des valeurs manquantes.
        ''')

    with Lien_parente:
        st.write('''
                     ### I - Lien Parenté 
                   ''')
        st.write('''
        Variable représentant le lien de parenté d'un individu à l'interieur d'un ménage.Elle est codée comme suit : 
                    ''')
        st.write('''
                             - ** 1 : Chef de Menage **
                            ''')

        st.write('''
                                 - ** 2 : Conjoint du chef de Menage **
                                ''')
        st.write('''
                             - ** 3 : Enfant du chef de Menage **
                            ''')
        st.write('''
                             - ** 5 : Beau fils ou belle fille du CM **
                            ''')
        st.write('''
                             - ** 6 : Père ou Mère du CM **
                            ''')
        st.write('''
                             - ** 7 : Neveux ou Nièce du CM **
                            ''')
        st.write('''
                             - ** 8 : Autre Membre **
                            ''')
        st.write('''
        ** Traitement du jeu de données **
        ''')
        st.write('''** étape 1 ** ''')
        st.write('''
        Nous allons retirer les autres variables avec les valeurs manqauntes de notre jeu de données
         et ensuite nous allons prendre la variable Lien Parenté comme la variable cible de notre réseau.
        ''')
        data1 = df.drop(["Type de structure", "Statut d'occupation"], axis=1)
        st.write(data1.isna().sum())
        st.text(''
                ''
                '')
        st.write('''** étape 2 ** ''')
        st.write('''
        Nous allons maintenant retirer de notre jeu de données les lignes contenant 
        les valeurs manquantes pour la variable Lien Parenté. 
        Ces lignes vont constituer notre jeu à predire.
        ''')
        # recuperons les lignes ayant les valeurs manquantes pour la variables Lien Parenté
        ind = np.where(data1["Lien Parenté"].isna())[0]

        # recuperons le dataframe correspondant a ces lignes
        to_pred = deepcopy(data1.iloc[ind])

        # Supprimons ces lignes de notre dataframe d'apprentissage
        data1 = data1[data1['Lien Parenté'].notna()]
        # Recuperons la variable cible et supprimons là de notre dataframe d'apprentissage
        cible = data1['Lien Parenté'].values.astype('int8')
        cible[np.where(cible == 0)] = 1

        data1.drop(["Lien Parenté"], inplace=True, axis=1)
        to_pred.drop(["Lien Parenté"], inplace=True, axis=1)
        st.write('''** étape 3 ** ''')
        st.write('''
        Nous allons maintenant catégoriser notre variable variable cible
        ''')



        st.write('''** étape 4 ** ''')
        st.write('''
        **Construction de la structure du réseau de neurones**
        ''')

        st.write('''
                Notre réseau sera composé de trois **couches cachées** de respectivement **50,40 et 30 neurones**
                . et une **couche de sortie** de **8 neurones** au lieu de **3**, car il n'y a que **8** classes à predire..
                ''')
        st.write('''
                Les couches cachées auront comme fonction d'**actiavtion relu**.
                Et la couche de sortie aura comme fonction d'**activation softmax**
                ''')
        st.image("images/model.PNG")

        st.write('''** étape 5 ** ''')
        st.write('''
        **Apprentissage du réseau de neurones**
        ''')
        st.write('''
                Après l'apprentissage nous obtenons ces résultats sont :
                ''')
        st.image("images/classLien.PNG")

    with Type_structure:
        st.write('''
      ### II - Type de Structure
    ''')
        st.write('''Variable représentant les différents type d'habitation des ménages.Elle est codée comme suit : 
            ''')
        st.write('''
                     - ** 1 : Cabane **
                    ''')

        st.write('''
                         - ** 2 : Maison Isolée **
                        ''')
        st.write('''
                     - ** 3 : Villa Moderne **
                    ''')
        st.write('''
                     - ** 4 : Château **
                    ''')
        st.write('''
                     - ** 5 : Maison à plusieurs logements **
                    ''')
        st.write('''
                     - ** 6 : Immeuble **
                    ''')
        st.write('''
                     - ** 7 : Autre **
                    ''')
        st.write('''
        ** a) Traitement du jeu de données **  
        ''')
        st.write('''
        Nous utiliserons notre fonction de traitement de jeu de données qui affichera les modalités que nous essayerons prédire
        ''')
        st.image("images/vS.PNG")
        st.write('''
        ** b) Construction de la structure du réseau de neurones**
        ''')
        st.write('''
        Notre réseau sera composé de trois **couches cachées** de respectivement **50 , 40  et 25 neurones**.
        Et une **couche de sortie** de **7 neurones**.
        Les couches cachées auront comme fonction d'**actiavtion relu**.
        Et la couche de sortie aura comme fonction d'**activation softmax**.
        ''')
        st.image("images/ModelTy.PNG")
        st.write('''
        ** Apprentissage du réseau de neurones **
        ''')
        st.write('''
        Après l'apprentissage nous avons obtenues :
        ''')
        st.image("images/ClassStructure.PNG")
        st.write('''
        Nous remarquons que le réseau à prédit 6 classe qui sont destinés pour la plupart  au Marché local 
        et le reste est destiné à l'autoconsommation.
        ''')

    with Status_occupation:
        st.write('''
             ### III - Status d'occupation
           ''')

        st.write('''Variable représentant le status d'occupations des lieux d'habitations par les ménages.Elle est codée comme suit : 
                   ''')
        st.write('''
                            - ** 1 : Propriétaire **
                           ''')

        st.write('''
                                - ** 2 : Locataire **
                               ''')
        st.write('''
                            - ** 3 : Autre **
                           ''')
        st.write('''
         ** 
         a) Traitement du jeu de données
         **
        ''')

        st.write('''
                Nous utiliserons notre fonction de traitement de jeu de données 
                ''')

        st.write('''
        ** b) Construction de la structure du réseau de neurones  **
        ''')
        st.write('''
        Notre réseau sera composé de trois  **couches cachées** de respectivement **50 ,40 et 20 neurones**.
        et une **couche de sortie** de **3 neurones**.
        Les couches cachées auront comme fonction d'**actiavtion relu**. 
        Et la couche de sortie aura comme fonction d'**activation softmax**

        ''')

        st.image("images/Model3.PNG")

        st.write('''
        ** Apprentissage du réseau de neurones **

        ''')
        st.write('''
        nous obtenons les résultats suivant après l'apprentissage.
        ''')
        st.image("images/predictOccu.PNG")
        st.write('''
        Le réseau à prédit que dans la plupart des productions, l'implication des Statut d'occupation est Importantes
        ''')
    with Reconstruction:
        st.write('''
        ###  Reconstitution du jeu de données
        ''')
        st.write('''
        Après avoir fait toutes les prédictions, 
        nous allons reconstituer notre jeu de données en remplacant 
        les valeurs manquantes par leurs prédictions
        ''')
        dataok = pd.read_csv("habitat_viz.csv", sep=';', encoding='latin1')
        st.write(dataok.isna().sum())

if __name__ == "__main__":
    main()





