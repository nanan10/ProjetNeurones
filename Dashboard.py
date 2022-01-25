import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def Tableau_de_Bord():
    data1 = pd.read_csv("habitat_viz.csv",sep=';',encoding='latin1')
    n = "Combien d'enfant"
    st.title("Dashboard")
    st.sidebar.header("Choisir vos filtres")
    Milieu_Residence = st.sidebar.multiselect(
        "selectionner selon le Milieu de Résidence:",
         options = data1["Milieu_Residence"].unique(),
         default= data1["Milieu_Residence"].unique()
    )
    Arrondissement = st.sidebar.multiselect(
        "Filtrer selon l'arrondissement",
        options=data1["Arrondissement"].unique(),
        default=[180,303]
    )
    Diplome_plus_eleve = st.sidebar.multiselect(
        "Filtrer selon Diplome",
        options=data1["Diplome_plus_eleve "].unique(),
        default=["BAC","LICENCE","BTS"]

    )
    Combien_enfant = st.sidebar.multiselect(
        "Filtrer selon Nombre d'enfants",
        options=data1["Combien_enfant"].unique(),
        default=[3,4,5]
    )

    data_selection = data1.query(
        " Milieu_Residence == @Milieu_Residence"
    )

    data2 = data1[data1["Lien_Parente"] =="Chef de Menage"]
    fd = data2.groupby(["Arrondissement", "Age"])[["Religion"]].count()
    fd = fd.reset_index()

    data_selectionfd = fd.query(
        "Arrondissement == @Arrondissement"
    )
    gauche, droite = st.columns(2)
    fig4 = px.bar(
        data_selectionfd,
        x="Age",
        y="Religion",
        width=600,
        color="Arrondissement",
        labels={"Religion": "Nombre de Personnes"},
        orientation="v",
        title="<b>Chef Ménages par Arrondissement selon leur Age </b>",
        color_discrete_sequence=["#0083B8"] * len(fd),
        template="plotly_white",
    )
    gauche.plotly_chart(fig4,use_container_width=False)

    fd1 = data2.groupby(["Arrondissement","Diplome_plus_eleve "])[["Religion"]].count()
    fd1 = fd1.reset_index()
    data_selectionfd1 = fd1.query(
        "Arrondissement == @Arrondissement "
    )

    fig1 = px.scatter(
        data_selectionfd1,
        x="Diplome_plus_eleve ",
        y="Religion",
        orientation="h",
        width=600,
        size="Religion",
        color="Arrondissement",
        labels={"Religion": "Nombre de Personnes"},
        title="<b>Chef de Menage par  arrondissement selon le diplome</b>",
        color_discrete_sequence=["skyblue"] * len(fd1),
        template="plotly_white",
    )
    droite.plotly_chart(fig1,use_container_width=False)


    p3 = data1.groupby(by=["Arrondissement","Activite_Agropastorale"])[["Religion"]].count()
    p3 = p3.reset_index()
    data_selectionfd2 = p3.query(
        "Arrondissement == @Arrondissement"
    )
    gauche1,droite1 = st.columns(2)
    fig3 = px.histogram(
        data_selectionfd2,
        x="Religion",
        y="Activite_Agropastorale",
        width=600,
        orientation="h",
        labels={"Religion":"Nombre de ménage"},
        title="<b> Arrondissement selon Activité Agropastorale </b>",
        color_discrete_sequence=["skyblue"] * len(data_selectionfd2),
        template="plotly_white",
    )
    gauche1.plotly_chart(fig3,use_container_width=False)
    p4 = data1.groupby(by=["Arrondissement", "Etat_matrimonial"])[["Religion"]].count()
    p4 = p4.reset_index()
    data_selectionfd3 = p4.query(
        "Arrondissement == @Arrondissement"
    )
    fig5 = px.sunburst(
        data_selectionfd3,
        path=["Arrondissement","Etat_matrimonial"],
        width=600,
        values="Religion",
        color="Arrondissement",
        labels={"Religion": "Nombre de ménage"},
        title="<b> Arrondissement selon l' Etat Matrimonial </b>",
        color_discrete_sequence=["brown"] * len(data_selectionfd2),
        template="plotly_white",
    )
    droite1.plotly_chart(fig5,use_container_width=False)
    p5 = data1.groupby(by=["Arrondissement", "Milieu_Residence"])[["Religion"]].count()
    p5 = p5.reset_index()
    data_selectionfd4 = p5.query(
        "Arrondissement == @Arrondissement"
    )
    gauche2,droite2 = st.columns(2)
    fig6 = px.bar(
        data_selectionfd4,
        x="Religion",
        y="Milieu_Residence",
        width=600,
        pattern_shape="Milieu_Residence",
        pattern_shape_sequence=[".", "x"],
        labels={"Religion": "Nombre de ménage"},
        title="<b> Arrondissement selon le Milieu Residence </b>",
        color_discrete_sequence=["lightgreen"] * len(data_selectionfd4),
        template="plotly_white",
    )
    gauche2.plotly_chart(fig6,use_container_width=False)
    p6 = data1.groupby(by=["Arrondissement","Etat_Sante"])[["Religion"]].count()
    p6 = p6.reset_index()
    data_selectionfd5 = p6.query(
        "Arrondissement == @Arrondissement"
    )
    fig7 = px.funnel(
        data_selectionfd5,
        x="Religion",
        y="Etat_Sante",
        width=600,
        orientation="h",
        color="Arrondissement",
        labels={"Religion": "Nombre de ménage"},
        title="<b> Arrondissement selon l'Etat de Sante </b>",
        color_discrete_sequence=["lightblue"] * len(data_selectionfd5),
        template="plotly_white",
    )
    droite2.plotly_chart(fig7, use_container_width=False)
    p7 = data1.groupby(by=["Arrondissement", "Type_structure"])[["Religion"]].count()
    p7 = p7.reset_index()
    data_selectionfd6 = p7.query(
        "Arrondissement == @Arrondissement"
    )
    fig8 = px.funnel(
        data_selectionfd6,
        x="Religion",
        y="Type_structure",
        width=600,
        orientation="h",
        color="Arrondissement",
        labels={"Religion": "Nombre de ménage"},
        title="<b> Arrondissement selon le Type de Structure </b>",
        color_discrete_sequence=["lightblue"] * len(data_selectionfd6),
        template="plotly_white",
    )
    droite3, gauche3 = st.columns(2)
    gauche3.plotly_chart(fig8, use_container_width=False)
    p8 = data1.groupby(by=["Arrondissement", "Religion"
        ,"Parle_plusieurs_langues","Combien_enfant"])[["Sexe"]].count()
    p8 = p8.reset_index()
    data_selectionfd7 = p8.query(
        "Arrondissement == @Arrondissement & Combien_enfant ==@Combien_enfant"
    )
    fig9 = px.sunburst(
        data_selectionfd7,
        path=["Arrondissement", "Religion","Parle_plusieurs_langues"],
        width=600,
        values="Sexe",
        color="Arrondissement",
        labels={"Sexe": "Nombre de ménage"},
        title="<b> Arrondissement selon Religion ,langues et le nombre d'enfant </b>",
        color_discrete_sequence=["brown"] * len(data_selectionfd7),
        template="plotly_white",
    )
    droite3.plotly_chart(fig9, use_container_width=False)

    p9 = data1.groupby(by=["Arrondissement","Statut_occupation","Autochtone"])[["Sexe"]].count()
    p9 = p9.reset_index()
    data_selectionfd8 = p9.query(
        "Arrondissement == @Arrondissement"
    )
    fig10 = px.sunburst(
        data_selectionfd8,
        path=["Arrondissement","Statut_occupation","Autochtone"],
        width=600,
        values="Sexe",
        color="Autochtone",
        labels={"Sexe": "Nombre de ménage"},
        title="<b> Arrondissement selon le status d'occupation et s'il est autochone</b>",
        template="plotly_white",
    )
    st.plotly_chart(fig10, use_container_width=False)





























