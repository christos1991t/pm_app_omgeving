import streamlit as st
import functions as fn

st.set_page_config(page_title="ProcessMinded App Omgeving", layout="wide")

st.title("ProcessMinded App Omgeving")
st.text(""" Deze omgeving bevat klein aapjes die jullie leven makkelijker kunnen maken. 
Van import tools tot tabellen maken hier kunnen jullie wat vinden """)

text_import_export = """ Als jullie willen een groot antaal gegevens naar ProMise Online importeren kunnen jullie de 
volgende app gebruiken. Hier kunnen jullie de Export van een Klant toevoegen als bron en de Imports van stappen 3,6,7 en 
8 maken.de geproduceerde bestanden worden netjes in een map opgeslagen"""

with st.expander("Import/Export App"):
    st.text(text_import_export)
    file1_path = st.file_uploader("Bestaand kiezen")
    if file1_path:
        Initial_file = fn.import_klant(file1_path)
        table = st.table(Initial_file[:0])
    idon = st.text_input("Eis ID ON")
    idog = st.text_input("Eis ID OG")
    button2 = st.button("Match Columns", key="button2")
    end_df = []
    if button2:
        fn.submit_columns(idon, idog, file1_path)

    df1 = fn.submit_columns(idon, idog, file1_path)[0]
    df2 = fn.submit_columns(idon, idog, file1_path)[1]

    zip_contents = fn.imports_maken(df1, df2)
    st.download_button(label="Click here to download the file",
                       data=zip_contents,
                       file_name="file.zip",
                       mime="application/zip")
