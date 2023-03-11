import pandas as pd
import io
import zipfile


def import_klant(file1_path):
    client_export = pd.read_excel(file1_path)
    return client_export


def submit_columns(idon, idog, eistitel, eistekst,
                   toelichting_tekst, vereiste_verificatie,
                   toelichting_vereiste_verificatie, typering_eis, initiator_org,
                   brondocument, status_eis, analyse_verantwoordelijk, smart, toelichting_smart, verificatiemethode,
                   toelichting_ver_methode, verificatiecriterium,
                   frequentie, verificator, verificator_functie, resultaat_veri,
                   verificatiedatum, uitgevoerd_door, toelichting_ver, bewijsdoc,
                   controleur, status_controle, activiteit_id, activiteit_naam,
                   projectfase, object_id_on, object_id_og, objectpo, file1_path):
    path_step_3 = 'https://raw.githubusercontent.com/christos1991t/python_test/master/Stap%203%20import.xlsx'
    path_step_6 = 'https://raw.githubusercontent.com/christos1991t/python_test/master/Stap%206%20import.xlsx'
    path_step_7 = 'https://raw.githubusercontent.com/christos1991t/python_test/master/Stap%207%20import.xlsx'
    path_step_8 = 'https://raw.githubusercontent.com/christos1991t/python_test/master/Stap%208%20import.xlsx'

    Step_3_Import = pd.read_excel(path_step_3)
    Step_6_Import = pd.read_excel(path_step_6)
    Step_7_Import = pd.read_excel(path_step_7)
    Step_8_Import = pd.read_excel(path_step_8)

    if activiteit_id != '' and idon != '' \
            and idog != '' and eistitel != '' \
            and eistekst != '' and toelichting_tekst != '' \
            and vereiste_verificatie != '' \
            and toelichting_vereiste_verificatie != '' and typering_eis != '' \
            and initiator_org != '' and brondocument != '' and status_eis != '' \
            and analyse_verantwoordelijk != '' \
            and smart != '' and toelichting_smart != '' and activiteit_naam != '' and projectfase != '' \
            and object_id_on != '' and object_id_og != '' and objectpo != '' and verificatiemethode != '' \
            and toelichting_ver_methode != '' and verificatiecriterium != '' and frequentie != '' \
            and verificator != '' and verificator_functie != '' and resultaat_veri != '' \
            and verificatiedatum != '' and uitgevoerd_door != '' and toelichting_ver != '' \
            and bewijsdoc != '' and controleur != '' and status_controle != '':

        Step_8_Import.loc[:, 'Eis ID ON'] = Step_7_Import.loc[:, 'Eis ID ON'] = Step_6_Import.loc[:, 'Eis ID ON'] = \
            Step_3_Import.loc[:, 'ID ON'] = import_klant(file1_path).loc[:, idon]

        Step_8_Import.loc[:, 'Eis ID OG'] = Step_7_Import.loc[:, 'Eis ID OG'] = \
            Step_6_Import.loc[:, 'Eis ID OG'] = Step_3_Import.loc[:, 'ID OG'] = import_klant(file1_path).loc[:, idog]

        Step_8_Import.loc[:, 'Eistitel'] = Step_7_Import.loc[:, 'Eistitel'] = \
            Step_6_Import.loc[:, 'Eistitel'] = Step_3_Import.loc[:, 'Eistitel'] = \
            import_klant(file1_path).loc[:, eistitel]

        Step_8_Import.loc[:, 'Eistekst'] = Step_7_Import.loc[:, 'Eistekst'] = \
            Step_6_Import.loc[:, 'Eistekst'] = Step_3_Import.loc[:, 'Eistekst'] = \
            import_klant(file1_path).loc[:, eistekst]

        Step_8_Import.loc[:, 'Toelichting eistekst'] = Step_7_Import.loc[:, 'Toelichting eistekst'] = \
            Step_6_Import.loc[:, 'Toelichting eistekst'] = Step_3_Import.loc[:, 'Toelichting eistekst'] = \
            import_klant(file1_path).loc[:, toelichting_tekst]

        Step_7_Import.loc[:, 'Vereiste verificatie OG'] = Step_3_Import.loc[:, 'Vereiste verificatie OG'] = \
            import_klant(file1_path).loc[:, vereiste_verificatie]

        Step_7_Import.loc[:, 'Toelichting vereiste verificatie OG'] = \
            Step_3_Import.loc[:, 'Toelichting vereiste verificatie OG'] = \
            import_klant(file1_path).loc[:, toelichting_vereiste_verificatie]

        Step_8_Import.loc[:, 'Typering eis'] = Step_7_Import.loc[:, 'Typering eis'] = \
            Step_6_Import.loc[:, 'Typering eis'] = Step_3_Import.loc[:, 'Typering eis'] = \
            import_klant(file1_path).loc[:, typering_eis]

        Step_3_Import.loc[:, 'Initiator Externe Organisatie'] = import_klant(file1_path).loc[:, initiator_org]

        Step_8_Import.loc[:, 'Brondocument'] = Step_7_Import.loc[:, 'Brondocument'] = \
            Step_6_Import.loc[:, 'Brondocument'] = Step_3_Import.loc[:, 'Brondocument'] = \
            import_klant(file1_path).loc[:, brondocument]

        Step_8_Import.loc[:, 'Status eis'] = Step_7_Import.loc[:, 'Status eis'] = Step_3_Import.loc[:, 'Status eis'] = \
            import_klant(file1_path).loc[:, status_eis]

        Step_3_Import.loc[:, 'Analyse verantwoordelijk'] = import_klant(file1_path).loc[:, analyse_verantwoordelijk]

        Step_7_Import.loc[:, 'Eis SMART'] = Step_3_Import.loc[:, 'SMART'] = import_klant(file1_path).loc[:, smart]

        Step_7_Import.loc[:, 'Eis SMART toelichting'] = Step_3_Import.loc[:, 'Toelichting SMART'] = \
            import_klant(file1_path).loc[:, toelichting_smart]

        Step_8_Import.loc[:, 'Activiteit ID ON'] = Step_7_Import.loc[:, 'Activiteit ID ON'] = \
            Step_6_Import.loc[:, 'Activiteit ID ON'] = import_klant(file1_path).loc[:, activiteit_id]

        Step_8_Import.loc[:, 'Activiteit'] = Step_7_Import.loc[:, 'Activiteit'] = \
            Step_6_Import.loc[:, 'Activiteit naam'] = import_klant(file1_path).loc[:, activiteit_naam]

        Step_8_Import.loc[:, 'Projectfase'] = Step_7_Import.loc[:, 'Projectfase'] = \
            Step_6_Import.loc[:, 'Projectfase'] = import_klant(file1_path).loc[:, projectfase]

        Step_8_Import.loc[:, 'Object ID ON'] = Step_7_Import.loc[:, 'Object ID ON'] = \
            Step_6_Import.loc[:, 'Object ID ON'] = import_klant(file1_path).loc[:, object_id_on]

        Step_8_Import.loc[:, 'Object ID OG'] = Step_7_Import.loc[:, 'Object ID OG'] = \
            Step_6_Import.loc[:, 'Object ID OG'] = import_klant(file1_path).loc[:, object_id_og]

        Step_8_Import.loc[:, 'Object'] = Step_7_Import.loc[:, 'Object'] = Step_6_Import.loc[:, 'Object'] = \
            import_klant(file1_path).loc[:, objectpo]

        Step_8_Import.loc[:, 'Verificatiemethode'] = Step_7_Import.loc[:, 'Verificatiemethode'] = \
            import_klant(file1_path).loc[:, verificatiemethode]

        Step_8_Import.loc[:, 'Toelichting verificatiemethode'] = \
            Step_7_Import.loc[:, 'Toelichting verificatiemethode'] = \
            import_klant(file1_path).loc[:, toelichting_ver_methode]

        Step_8_Import.loc[:, 'Verificatiecriterium'] = Step_7_Import.loc[:, 'Verificatiecriterium'] = \
            import_klant(file1_path).loc[:, verificatiecriterium]

        Step_8_Import.loc[:, 'Frequentie'] = Step_7_Import.loc[:, 'Frequentie'] = \
            import_klant(file1_path).loc[:, frequentie]

        Step_8_Import.loc[:, 'Verificator'] = Step_7_Import.loc[:, 'Verificator'] = \
            import_klant(file1_path).loc[:, verificator]

        Step_8_Import.loc[:, 'Verificator Functie'] = import_klant(file1_path).loc[:, verificator_functie]

        Step_8_Import.loc[:, 'Resultaat verificatie'] = import_klant(file1_path).loc[:, resultaat_veri]

        Step_8_Import.loc[:, 'Verificatiedatum'] = import_klant(file1_path).loc[:, verificatiedatum]

        Step_8_Import.loc[:, 'Uitgevoerd door'] = import_klant(file1_path).loc[:, uitgevoerd_door]

        Step_8_Import.loc[:, 'Toelichting verificatie'] = import_klant(file1_path).loc[:, toelichting_ver]

        Step_8_Import.loc[:, 'Bewijsdocument'] = import_klant(file1_path).loc[:, bewijsdoc]

        Step_8_Import.loc[:, 'Controleur'] = import_klant(file1_path).loc[:, controleur]

        Step_8_Import.loc[:, 'Status controle'] = import_klant(file1_path).loc[:, status_controle]
    elif activiteit_id == '' and idon == '' \
            and idog == '' and eistitel == '' \
            and eistekst == '' and toelichting_tekst == '' \
            and vereiste_verificatie == '' \
            and toelichting_vereiste_verificatie == '' and typering_eis == '' \
            and initiator_org == '' and brondocument == '' and status_eis == '' \
            and analyse_verantwoordelijk == '' \
            and smart == '' and toelichting_smart == '' and activiteit_naam == '' and projectfase == '' \
            and object_id_on == '' and object_id_og == '' and objectpo == '' and verificatiemethode == '' \
            and toelichting_ver_methode == '' and verificatiecriterium == '' and frequentie == '' \
            and verificator == '' and verificator_functie == '' and resultaat_veri == '' \
            and verificatiedatum == '' and uitgevoerd_door == '' and toelichting_ver == '' \
            and bewijsdoc == '' and controleur == '' and status_controle == '':
        pass
    else:
        if idon == '':
            Step_8_Import.loc[:, 'Eis ID ON'] = Step_7_Import.loc[:, 'Eis ID ON'] = \
                Step_6_Import.loc[:, 'Eis ID ON'] = Step_3_Import.loc[:, 'ID ON']
        else:
            Step_8_Import.loc[:, 'Eis ID ON'] = Step_7_Import.loc[:, 'Eis ID ON'] = \
                Step_6_Import.loc[:, 'Eis ID ON'] = Step_3_Import.loc[:, 'ID ON'] = \
                import_klant(file1_path).loc[:, idon]

        if idog == '':
            Step_8_Import.loc[:, 'Eis ID OG'] = Step_7_Import.loc[:, 'Eis ID OG'] = \
                Step_6_Import.loc[:, 'Eis ID OG'] = Step_3_Import.loc[:, 'ID OG']
        else:
            Step_8_Import.loc[:, 'Eis ID OG'] = Step_7_Import.loc[:, 'Eis ID OG'] = \
                Step_6_Import.loc[:, 'Eis ID OG'] = Step_3_Import.loc[:, 'ID OG'] = \
                import_klant(file1_path).loc[:, idog]

        if eistitel == '':
            Step_8_Import.loc[:, 'Eistitel'] = Step_7_Import.loc[:, 'Eistitel'] = Step_6_Import.loc[:, 'Eistitel'] = \
                Step_3_Import.loc[:, 'Eistitel']
        else:
            Step_8_Import.loc[:, 'Eistitel'] = Step_7_Import.loc[:, 'Eistitel'] = \
                Step_6_Import.loc[:, 'Eistitel'] = Step_3_Import.loc[:, 'Eistitel'] = \
                import_klant(file1_path).loc[:, eistitel]

        if eistekst == '':
            Step_8_Import.loc[:, 'Eistekst'] = Step_7_Import.loc[:, 'Eistekst'] = Step_6_Import.loc[:, 'Eistekst'] = \
                Step_3_Import.loc[:, 'Eistekst']
        else:
            Step_8_Import.loc[:, 'Eistekst'] = Step_7_Import.loc[:, 'Eistekst'] = Step_6_Import.loc[:, 'Eistekst'] = \
                Step_3_Import.loc[:, 'Eistekst'] = import_klant(file1_path).loc[:, eistekst]

        if toelichting_tekst == '':
            Step_8_Import.loc[:, 'Toelichting eistekst'] = Step_7_Import.loc[:, 'Toelichting eistekst'] = \
                Step_6_Import.loc[:, 'Toelichting eistekst'] = Step_3_Import.loc[:, 'Toelichting eistekst']
        else:
            Step_8_Import.loc[:, 'Toelichting eistekst'] = Step_7_Import.loc[:, 'Toelichting eistekst'] = \
                Step_6_Import.loc[:, 'Toelichting eistekst'] = Step_3_Import.loc[:, 'Toelichting eistekst'] = \
                import_klant(file1_path).loc[:, toelichting_tekst]

        if vereiste_verificatie == '':
            Step_7_Import.loc[:, 'Vereiste verificatie OG'] = Step_3_Import.loc[:, 'Vereiste verificatie OG']
        else:
            Step_7_Import.loc[:, 'Vereiste verificatie OG'] = Step_3_Import.loc[:, 'Vereiste verificatie OG'] = \
                import_klant(file1_path).loc[:, vereiste_verificatie]

        if typering_eis == '':
            Step_8_Import.loc[:, 'Typering eis'] = Step_7_Import.loc[:, 'Typering eis'] = \
                Step_6_Import.loc[:, 'Typering eis'] = Step_3_Import.loc[:, 'Typering eis']
        else:
            Step_8_Import.loc[:, 'Typering eis'] = Step_7_Import.loc[:, 'Typering eis'] = \
                Step_6_Import.loc[:, 'Typering eis'] = Step_3_Import.loc[:, 'Typering eis'] = \
                import_klant(file1_path).loc[:, typering_eis]

        if initiator_org == '':
            Step_3_Import.loc[:, 'Initiator Externe Organisatie'] = \
                Step_3_Import.loc[:, 'Initiator Externe Organisatie']
        else:
            Step_3_Import.loc[:, 'Initiator Externe Organisatie'] = import_klant(file1_path).loc[:, initiator_org]

        if brondocument == '':
            Step_8_Import.loc[:, 'Brondocument'] = Step_7_Import.loc[:, 'Brondocument'] = \
                Step_6_Import.loc[:, 'Brondocument'] = Step_3_Import.loc[:, 'Brondocument']
        else:
            Step_8_Import.loc[:, 'Brondocument'] = Step_7_Import.loc[:, 'Brondocument'] = \
                Step_6_Import.loc[:, 'Brondocument'] = Step_3_Import.loc[:, 'Brondocument'] = \
                import_klant(file1_path).loc[:, brondocument]

        if status_eis == '':
            Step_8_Import.loc[:, 'Status eis'] = Step_7_Import.loc[:, 'Status eis'] = \
                Step_3_Import.loc[:, 'Status eis']
        else:
            Step_8_Import.loc[:, 'Status eis'] = Step_7_Import.loc[:, 'Status eis'] = \
                Step_3_Import.loc[:, 'Status eis'] = import_klant(file1_path).loc[:, status_eis]

        if analyse_verantwoordelijk == '':
            Step_3_Import.loc[:, 'Analyse verantwoordelijk'] = Step_3_Import.loc[:, 'Analyse verantwoordelijk']
        else:
            Step_3_Import.loc[:, 'Analyse verantwoordelijk'] = import_klant(file1_path).loc[:, analyse_verantwoordelijk]

        if smart == '':
            Step_7_Import.loc[:, 'Eis SMART'] = Step_3_Import.loc[:, 'SMART']
        else:
            Step_7_Import.loc[:, 'Eis SMART'] = Step_3_Import.loc[:, 'SMART'] = import_klant(file1_path).loc[:, smart]

        if toelichting_smart == '':
            Step_7_Import.loc[:, 'Eis SMART toelichting'] = Step_3_Import.loc[:, 'Toelichting SMART']
        else:
            Step_7_Import.loc[:, 'Eis SMART toelichting'] = Step_3_Import.loc[:, 'Toelichting SMART'] = \
                import_klant(file1_path).loc[:, toelichting_smart]

        if activiteit_id == '':
            Step_8_Import.loc[:, 'Activiteit ID ON'] = Step_7_Import.loc[:, 'Activiteit ID ON'] = \
                Step_6_Import.loc[:, 'Activiteit ID ON']
        else:
            Step_8_Import.loc[:, 'Activiteit ID ON'] = Step_7_Import.loc[:, 'Activiteit ID ON'] = \
                Step_6_Import.loc[:, 'Activiteit ID ON'] = import_klant(file1_path).loc[:, activiteit_id]

        if activiteit_naam == '':
            Step_8_Import.loc[:, 'Activiteit'] = Step_7_Import.loc[:, 'Activiteit'] = \
                Step_6_Import.loc[:, 'Activiteit naam']
        else:

            Step_8_Import.loc[:, 'Activiteit'] = Step_7_Import.loc[:, 'Activiteit'] = \
                Step_6_Import.loc[:, 'Activiteit naam'] = \
                import_klant(file1_path).loc[:, activiteit_naam]

        if projectfase == '':
            Step_8_Import.loc[:, 'Projectfase'] = Step_7_Import.loc[:, 'Projectfase'] = \
                Step_6_Import.loc[:, 'Projectfase']
        else:
            Step_8_Import.loc[:, 'Projectfase'] = Step_7_Import.loc[:, 'Projectfase'] = \
                Step_6_Import.loc[:, 'Projectfase'] = import_klant(file1_path).loc[:, projectfase]

        if object_id_on == '':
            Step_8_Import.loc[:, 'Object ID ON'] = Step_7_Import.loc[:, 'Object ID ON'] = \
                Step_6_Import.loc[:, 'Object ID ON']
        else:
            Step_8_Import.loc[:, 'Object ID ON'] = Step_7_Import.loc[:, 'Object ID ON'] = \
                Step_6_Import.loc[:, 'Object ID ON'] = import_klant(file1_path).loc[:, object_id_on]

        if object_id_og == '':
            Step_8_Import.loc[:, 'Object ID OG'] = Step_7_Import.loc[:, 'Object ID OG'] = \
                Step_6_Import.loc[:, 'Object ID OG']
        else:
            Step_8_Import.loc[:, 'Object ID OG'] = Step_7_Import.loc[:, 'Object ID OG'] = \
                Step_6_Import.loc[:, 'Object ID OG'] = import_klant(file1_path).loc[:, object_id_og]

        if objectpo == '':
            Step_8_Import.loc[:, 'Object'] = Step_7_Import.loc[:, 'Object'] = \
                Step_6_Import.loc[:, 'Object']
        else:
            Step_8_Import.loc[:, 'Object'] = Step_7_Import.loc[:, 'Object'] = \
                Step_6_Import.loc[:, 'Object'] = import_klant(file1_path).loc[:, objectpo]

        if verificatiemethode == '':
            Step_8_Import.loc[:, 'Verificatiemethode'] = Step_7_Import.loc[:, 'Verificatiemethode']
        else:
            Step_8_Import.loc[:, 'Verificatiemethode'] = Step_7_Import.loc[:, 'Verificatiemethode'] = \
                import_klant(file1_path).loc[:, verificatiemethode]

        if toelichting_ver_methode == '':
            Step_8_Import.loc[:, 'Toelichting verificatiemethode'] = \
                Step_7_Import.loc[:, 'Toelichting verificatiemethode']
        else:
            Step_8_Import.loc[:, 'Toelichting verificatiemethode'] = \
                Step_7_Import.loc[:, 'Toelichting verificatiemethode'] = \
                import_klant(file1_path).loc[:, toelichting_ver_methode]

        if verificatiecriterium == '':
            Step_8_Import.loc[:, 'Verificatiecriterium'] = Step_7_Import.loc[:, 'Verificatiecriterium']
        else:
            Step_8_Import.loc[:, 'Verificatiecriterium'] = Step_7_Import.loc[:, 'Verificatiecriterium'] = \
                import_klant(file1_path).loc[:, verificatiecriterium]

        if frequentie == '':
            Step_8_Import.loc[:, 'Frequentie'] = Step_7_Import.loc[:, 'Frequentie']
        else:
            Step_8_Import.loc[:, 'Frequentie'] = Step_7_Import.loc[:, 'Frequentie'] = \
                import_klant(file1_path).loc[:, frequentie ]

        if verificator == '':
            Step_8_Import.loc[:, 'Verificator'] = Step_7_Import.loc[:, 'Verificator']
        else:
            Step_8_Import.loc[:, 'Verificator'] = Step_7_Import.loc[:, 'Verificator'] = \
                import_klant(file1_path).loc[:, verificator]

        if verificator_functie == '':
            Step_8_Import.loc[:, 'Verificator Functie'] = Step_8_Import.loc[:, 'Verificator Functie']
        else:
            Step_8_Import.loc[:, 'Verificator Functie'] = import_klant(file1_path).loc[:, verificator_functie]

        if resultaat_veri == '':
            Step_8_Import.loc[:, 'Resultaat verificatie'] = Step_8_Import.loc[:, 'Resultaat verificatie']
        else:
            Step_8_Import.loc[:, 'Resultaat verificatie'] = import_klant(file1_path).loc[:, resultaat_veri]

        if verificatiedatum == '':
            Step_8_Import.loc[:, 'Verificatiedatum'] = Step_8_Import.loc[:, 'Verificatiedatum']
        else:
            Step_8_Import.loc[:, 'Verificatiedatum'] = import_klant(file1_path).loc[:, verificatiedatum]

        if uitgevoerd_door == '':
            Step_8_Import.loc[:, 'Uitgevoerd door'] = Step_8_Import.loc[:, 'Uitgevoerd door']
        else:
            Step_8_Import.loc[:, 'Uitgevoerd door'] = import_klant(file1_path).loc[:, uitgevoerd_door]

        if toelichting_ver == '':
            Step_8_Import.loc[:, 'Toelichting verificatie'] = Step_8_Import.loc[:, 'Toelichting verificatie']
        else:
            Step_8_Import.loc[:, 'Toelichting verificatie'] = import_klant(file1_path).loc[:, toelichting_ver]

        if bewijsdoc == '':
            Step_8_Import.loc[:, 'Bewijsdocument'] = Step_8_Import.loc[:, 'Bewijsdocument']
        else:
            Step_8_Import.loc[:, 'Bewijsdocument'] = import_klant(file1_path).loc[:, bewijsdoc]

        if controleur == '':
            Step_8_Import.loc[:, 'Controleur'] = Step_8_Import.loc[:, 'Controleur']
        else:
            Step_8_Import.loc[:, 'Controleur'] = import_klant(file1_path).loc[:, controleur]

        if status_controle == '':
            Step_8_Import.loc[:, 'Status controle'] = Step_8_Import.loc[:, 'Status controle']
        else:
            Step_8_Import.loc[:, 'Status controle'] = import_klant(file1_path).loc[:, status_controle]

    return Step_3_Import, Step_6_Import, Step_7_Import, Step_8_Import


def imports_maken(df1, df2, df3, df4):
    with io.BytesIO() as output:
        with zipfile.ZipFile(output, mode="w") as zip_file:
            with zip_file.open("Step 3 Import.xlsx", "w") as file1:
                df1.to_excel(file1, index=False)
            with zip_file.open("Step 6 Import.xlsx", "w") as file2:
                df2.to_excel(file2, index=False)
            with zip_file.open("Step 7 Import.xlsx", "w") as file3:
                df3.to_excel(file3, index=False)
            with zip_file.open("Step 8 Import.xlsx", "w") as file4:
                df4.to_excel(file4, index=False)
        zip_contents = output.getvalue()

    return zip_contents
