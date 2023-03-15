import streamlit as st
import functions_import as fn

st.set_page_config(page_title="Import/Export App", layout="wide")
st.title("Import/Export App")
st.markdown(""" Als jullie willen een groot antaal gegevens naar ProMise Online importeren kunnen jullie de 
volgende app gebruiken. Hier kunnen jullie de Export van een Klant toevoegen als bron en de Imports van 
stappen 3,6,7 en 8 maken. De geproduceerde bestanden worden netjes in een zip-map opgeslagen""")


file1_path = st.file_uploader("Bestaand kiezen", key="up1")
if file1_path:
    Initial_file = fn.import_klant(file1_path)
    table = st.table(Initial_file[:0])

tab1, tab2, tab3, tab4 = st.tabs(["Stap 3 kolommen", "Stap 6 kolommen", "Stap 7 kolommen", "Stap 8 kolommen"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        idon = st.text_input("Eis ID ON")
        idog = st.text_input("Eis ID OG")
        eistitel = st.text_input("Eistitel")
        eistekst = st.text_input("Eistekst")
        toelichting_eistekst = st.text_input("Toelichting eistekst")
        vereiste_verificatie_og = st.text_input("Vereiste verificatie OG")
        toelichting_vereiste_verificatie_og = st.text_input("Toelichting vereiste verificatie OG")
    with col2:
        typering_eis = st.text_input("Typering Eis")
        initiator_externe_organisatie = st.text_input("Initiator Externe Organisatie")
        brondocument = st.text_input("Brondocument")
        status_eis = st.text_input("Status eis")
        analyse_verantwoordelijke = st.text_input("Analyse verantwoordelijke")
        smart = st.text_input("SMART")
        toelichting_smart = st.text_input("Toelichting SMART")

with tab2:
    col3, col4 = st.columns(2)
    with col3:
        activiteit_id_on = st.text_input("Activiteit ID ON")
        activiteit_naam = st.text_input("Activiteit naam ")
        projectfase = st.text_input("Projectfase")
    with col4:
        object_id_on = st.text_input("Object ID ON")
        object_id_og = st.text_input("Object ID OG")
        objectpo = st.text_input("Object")

with tab3:
    verificatiemethode = st.text_input("Verificatiemethode")
    toelichting_ver_meth = st.text_input("Toelichting verificatiemethode")
    verificatiecriterium = st.text_input("Verificatiecriterium")
    frequentie = st.text_input("Frequentie")
    verificator = st.text_input("Verificator")

with tab4:
    col5, col6 = st.columns(2)
    with col5:
        verificator_functie = st.text_input("Verificator Functie")
        resultaat_verificatie = st.text_input("Resultaat verificatie")
        verificatiedatum = st.text_input("Verificatiedatum")
        uitgevoerd_door = st.text_input("Uitgevoerd door")
    with col6:
        toelichting_ver = st.text_input("Toelichting verificatie")
        bewijsdoc = st.text_input("Bewijsdocument")
        controleur = st.text_input("Controleur")
        status_controle = st.text_input("Status controle")

button2 = st.button("Match Kolommen", key="button2")

if button2:
    fn.submit_columns(idon=idon, idog=idog, eistitel=eistitel, eistekst=eistekst,
                      toelichting_tekst=toelichting_eistekst, vereiste_verificatie=vereiste_verificatie_og,
                      toelichting_vereiste_verificatie=toelichting_vereiste_verificatie_og,
                      typering_eis=typering_eis, initiator_org=initiator_externe_organisatie,
                      brondocument=brondocument, status_eis=status_eis,
                      analyse_verantwoordelijk=analyse_verantwoordelijke, smart=smart,
                      toelichting_smart=toelichting_smart, verificatiemethode=verificatiemethode,
                      toelichting_ver_methode=toelichting_ver_meth, verificatiecriterium=verificatiecriterium,
                      frequentie=frequentie, verificator=verificator, verificator_functie=verificator_functie,
                      resultaat_veri=resultaat_verificatie, verificatiedatum=verificatiedatum,
                      uitgevoerd_door=uitgevoerd_door, toelichting_ver=toelichting_ver, bewijsdoc=bewijsdoc,
                      controleur=controleur, status_controle=status_controle, activiteit_id=activiteit_id_on,
                      activiteit_naam=activiteit_naam, projectfase=projectfase, object_id_on=object_id_on,
                      object_id_og=object_id_og, objectpo=objectpo, file1_path=file1_path)

df1 = fn.submit_columns(idon=idon, idog=idog, eistitel=eistitel, eistekst=eistekst,
                        toelichting_tekst=toelichting_eistekst, vereiste_verificatie=vereiste_verificatie_og,
                        toelichting_vereiste_verificatie=toelichting_vereiste_verificatie_og,
                        typering_eis=typering_eis, initiator_org=initiator_externe_organisatie,
                        brondocument=brondocument, status_eis=status_eis,
                        analyse_verantwoordelijk=analyse_verantwoordelijke, smart=smart,
                        toelichting_smart=toelichting_smart, verificatiemethode=verificatiemethode,
                        toelichting_ver_methode=toelichting_ver_meth, verificatiecriterium=verificatiecriterium,
                        frequentie=frequentie, verificator=verificator, verificator_functie=verificator_functie,
                        resultaat_veri=resultaat_verificatie, verificatiedatum=verificatiedatum,
                        uitgevoerd_door=uitgevoerd_door, toelichting_ver=toelichting_ver, bewijsdoc=bewijsdoc,
                        controleur=controleur, status_controle=status_controle, activiteit_id=activiteit_id_on,
                        activiteit_naam=activiteit_naam, projectfase=projectfase, object_id_on=object_id_on,
                        object_id_og=object_id_og, objectpo=objectpo, file1_path=file1_path)[0]
df2 = fn.submit_columns(idon=idon, idog=idog, eistitel=eistitel, eistekst=eistekst,
                        toelichting_tekst=toelichting_eistekst, vereiste_verificatie=vereiste_verificatie_og,
                        toelichting_vereiste_verificatie=toelichting_vereiste_verificatie_og,
                        typering_eis=typering_eis, initiator_org=initiator_externe_organisatie,
                        brondocument=brondocument, status_eis=status_eis,
                        analyse_verantwoordelijk=analyse_verantwoordelijke, smart=smart,
                        toelichting_smart=toelichting_smart, verificatiemethode=verificatiemethode,
                        toelichting_ver_methode=toelichting_ver_meth, verificatiecriterium=verificatiecriterium,
                        frequentie=frequentie, verificator=verificator, verificator_functie=verificator_functie,
                        resultaat_veri=resultaat_verificatie, verificatiedatum=verificatiedatum,
                        uitgevoerd_door=uitgevoerd_door, toelichting_ver=toelichting_ver, bewijsdoc=bewijsdoc,
                        controleur=controleur, status_controle=status_controle, activiteit_id=activiteit_id_on,
                        activiteit_naam=activiteit_naam, projectfase=projectfase, object_id_on=object_id_on,
                        object_id_og=object_id_og, objectpo=objectpo, file1_path=file1_path)[1]
df3 = fn.submit_columns(idon=idon, idog=idog, eistitel=eistitel, eistekst=eistekst,
                        toelichting_tekst=toelichting_eistekst, vereiste_verificatie=vereiste_verificatie_og,
                        toelichting_vereiste_verificatie=toelichting_vereiste_verificatie_og,
                        typering_eis=typering_eis, initiator_org=initiator_externe_organisatie,
                        brondocument=brondocument, status_eis=status_eis,
                        analyse_verantwoordelijk=analyse_verantwoordelijke, smart=smart,
                        toelichting_smart=toelichting_smart, verificatiemethode=verificatiemethode,
                        toelichting_ver_methode=toelichting_ver_meth, verificatiecriterium=verificatiecriterium,
                        frequentie=frequentie, verificator=verificator, verificator_functie=verificator_functie,
                        resultaat_veri=resultaat_verificatie, verificatiedatum=verificatiedatum,
                        uitgevoerd_door=uitgevoerd_door, toelichting_ver=toelichting_ver, bewijsdoc=bewijsdoc,
                        controleur=controleur, status_controle=status_controle, activiteit_id=activiteit_id_on,
                        activiteit_naam=activiteit_naam, projectfase=projectfase, object_id_on=object_id_on,
                        object_id_og=object_id_og, objectpo=objectpo, file1_path=file1_path)[2]
df4 = fn.submit_columns(idon=idon, idog=idog, eistitel=eistitel, eistekst=eistekst,
                        toelichting_tekst=toelichting_eistekst, vereiste_verificatie=vereiste_verificatie_og,
                        toelichting_vereiste_verificatie=toelichting_vereiste_verificatie_og,
                        typering_eis=typering_eis, initiator_org=initiator_externe_organisatie,
                        brondocument=brondocument, status_eis=status_eis,
                        analyse_verantwoordelijk=analyse_verantwoordelijke, smart=smart,
                        toelichting_smart=toelichting_smart, verificatiemethode=verificatiemethode,
                        toelichting_ver_methode=toelichting_ver_meth, verificatiecriterium=verificatiecriterium,
                        frequentie=frequentie, verificator=verificator, verificator_functie=verificator_functie,
                        resultaat_veri=resultaat_verificatie, verificatiedatum=verificatiedatum,
                        uitgevoerd_door=uitgevoerd_door, toelichting_ver=toelichting_ver, bewijsdoc=bewijsdoc,
                        controleur=controleur, status_controle=status_controle, activiteit_id=activiteit_id_on,
                        activiteit_naam=activiteit_naam, projectfase=projectfase, object_id_on=object_id_on,
                        object_id_og=object_id_og, objectpo=objectpo, file1_path=file1_path)[3]

zip_contents = fn.imports_maken(df1, df2, df3, df4)
st.download_button(label="Zip Downloaden",
                   data=zip_contents,
                   file_name="file.zip",
                   mime="application/zip")
