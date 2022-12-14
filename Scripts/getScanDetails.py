# importing required modules
from zipfile import ZipFile
import json
#----------------------------------------------------------------

def extractZipfolder():
    # specifying the zip file name
    file_name = "C:\scanAnalysis\Input\TrivyScanReport.zip"
    # opening the zip file in READ mode
    with ZipFile(file_name, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()
        # extracting all the files
        zip.extractall()
        print('Done! Files have been extracted.')

#----------------------------------------------------------------
def getVulnerabilityDetails():
    # sample file with errors
    # with open("trivySampleError.json","r") as file:
    #     jsonData = json.load(file)

    path = './edge-sceuitool-trivy/trivy.json'
    file=open(path, "r")
    # with open("trivy.json","r") as file:
    jsonData = json.load(file)

    vulnerabilityCount = 0
    length = len(jsonData["Results"])
    for i in range(length):
        if "Vulnerabilities" in jsonData['Results'][i]:
            vulnerabilityCount+=1
            #print('There are Vulnerabilities in level' ,i)
            vulnerabilityDetails = jsonData['Results'][i]['Vulnerabilities']
            vulnerabilityID = vulnerabilityDetails[0]["VulnerabilityID"]
            vulnerabilityPkgName = vulnerabilityDetails[0]["PkgName"]
            vulnerabilityInstalledVersion = vulnerabilityDetails[0]["InstalledVersion"]
            vulnerabilityFixedVersion = vulnerabilityDetails[0]["FixedVersion"]
            vulnerabilityTitle = vulnerabilityDetails[0]["Title"]
            vulnerabilitySeverity = vulnerabilityDetails[0]["Severity"]
            with open("../Output/scan_results.txt", "a") as f:
                print("Vulnerability Details {}\n---\nVulnerability ID :  {} \nVulnerability Package Name : {} \nSeverity Level : {} \nInstalled Version : {} \nFixed Version : {} \nVulnerability Title : {} \n---".format(vulnerabilityCount,vulnerabilityID,vulnerabilityPkgName,vulnerabilitySeverity,vulnerabilityInstalledVersion,vulnerabilityFixedVersion,vulnerabilityTitle),file=f)
    if vulnerabilityCount == 0:
         with open("../Output/scan_results.txt", "a") as f:
            print('There are no vulnerabilities for this repository!', file=f)
            
#----------------------------------------------------------------
if __name__ == "__main__":
    extractZipfolder()
    getVulnerabilityDetails()