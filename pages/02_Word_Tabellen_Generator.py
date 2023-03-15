import io
import pandas as pd
import streamlit as st
import functions_tabel as fnt

st.set_page_config(page_title="Word tabellen Generator App", layout="wide")
st.title("Word tabellen Generator App")
st.markdown(""" Hebben jullie een Excel vol met eisen en willen jullie per eis een tabel maken voor een Word-rapport?
Dan kunnen jullie dit aapje gebruiken. Let op! De structuur van de excel moet dezelfde met het voorbeeld zijn. Anders 
werkt dit appje niet. Mocht jullie een ander structuur willen, maken jullie dan gebruik van de Contact pagina en ik kom 
zo snel mogelijk met een oplossing bij jullie terug!""")

st.header("BELANGRIJK!")
st.markdown(""" - Maak aub gebruik van de **Excel_Template**.""")

buffer = io.BytesIO()
df_temp = pd.read_excel("Excel_Template_Word.xlsx", keep_default_na=False, na_values=['_'])

with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
    # Write each dataframe to a different worksheet.
    df_temp.to_excel(writer, index=False, sheet_name='Sheet1')
    # Close the Pandas Excel writer and output the Excel file to the buffer
    writer.save()
st.download_button(
    label="Download Excel_Template",
    data=buffer,
    file_name="Excel_Template.xlsx",
    mime="application/vnd.ms-excel"
)

file_path = st.file_uploader("Bestaand kiezen", key="up2")
if file_path:
    Initial_file = fnt.import_excel(file_path).fillna("")
    if st.button("Tabellen Maken"):
        word_doc = fnt.tabel_maken(Initial_file)
        word_doc.save(buffer)
        st.success("Tabellen zijn gemaakt")
    if st.download_button("Word Downloaden", data=buffer.getvalue(), file_name="Tabel_Export.docx",
                          mime="docx"):
        st.success("Uw bestand staat in Downloads")
else:
    pass
