import pandas as pd
from docx import Document


def import_excel(file_path):
    client_export = pd.read_excel(file_path)
    return client_export


def tabel_maken(df):
    doc = Document('word_file.docx')
    for index, row in df.iterrows():
        table = doc.add_table(rows=5, cols=2)
        table.style = 'PythonStyle'
        m_cell_1 = table.cell(1, 0)
        m_cell_2 = table.cell(1, 1)
        merge_1 = m_cell_1.merge(m_cell_2)
        m_cell_3 = table.cell(2, 0)
        m_cell_4 = table.cell(2, 1)
        merge_2 = m_cell_3.merge(m_cell_4)
        m_cell_5 = table.cell(3, 0)
        m_cell_6 = table.cell(3, 1)
        merge_3 = m_cell_5.merge(m_cell_6)
        m_cell_7 = table.cell(4, 0)
        m_cell_8 = table.cell(4, 1)
        merge_4 = m_cell_7.merge(m_cell_8)

        # assing variable to non merged cells
        cell_1 = table.cell(0, 0)
        cell_2 = table.cell(0, 1)

        # Add a paragraph between tables
        doc.add_paragraph()

        # Populate the table with data from the current row
        for j, col in enumerate(df.columns):
            cell_value = row[col]

            # Paste the cell value into the appropriate table cell
            if j == 0:
                cell_1.text = str('Eis-ID: ' + '\n' + str(cell_value))
            elif j == 1:
                merge_1.text = str('Eistekst: ' + '\n' + str(cell_value))
            elif j == 2:
                if cell_value != "":
                    merge_2.text = str(
                        'Eistoelichting: ' + '\n' + str(cell_value))
                else:
                    merge_2.text = 'Eistoelichting: '
            elif j == 3:
                cell_2.text = str('Onderwerp: ' + str(cell_value))
            elif j == 4:
                merge_3.text = str('Oordeel verificatie:' + '\n')
            elif j == 5:
                merge_4.text = str(
                    'Toelichting oordeel verificatie:' + '\n')
    return doc
