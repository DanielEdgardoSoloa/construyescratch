import os
import sys
import json
import xml.etree.ElementTree as ET
import zipfile

# # Alias de la Org registrada con SFDX o Usuario que identifica la Org registrada con SFDX
origen = sys.argv[1]

########## comentar desde de aqui si solo se busca el XML#################################
os.system("sfdx force:mdapi:retrieve -r ./ -u " + origen + " -k ./package.xml")

with zipfile.ZipFile("./unpackaged.zip", "r") as zip_ref:
    zip_ref.extractall("./")
try:
    if os.listdir('./unpackaged/audience/'):
        os.system('rm -r ./unpackaged/audience/')
except:
    print('audience no existe')
try:
    if os.listdir('./unpackaged/customindex/'):
        os.system('rm -r ./unpackaged/customindex/')
except:
    print('customindex no existe')
try:
    if os.listdir('./unpackaged/uiObjectRelationConfigs/'):
        os.system('rm -r ./unpackaged/uiObjectRelationConfigs/')
except:
    print('uiObjectRelationConfigs no existe')
os.system("sfdx force:mdapi:convert --rootdir ./unpackaged --outputdir ./Salesforce")