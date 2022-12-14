# Scan Automation from AzureDevOps

A personal project to analyze the vulnerabilites for Trivy Scan from Azure DevOps Pipelines.

#### -- Project Status: [Completed]

## Project Objective
The artifacts provided in Azure DevOps(Pipelines) platform consists of 2000+ lines of complex JSON structure which is hard to navigate and look for vulnerabilties if any. This step was done for every repo our team owned. the objective was to solve this problem by reducing the time taken to analyze the vulnerabilties in those files. **This method could be used for any vulnerabilty scan, this one is specialized for Trivy Scan.**

 

## Project Description
Trivy scans code projects and build artifacts for security issues such as vulnerabilities, IaC misconfigurations, secrets, and more. This is generated for every build that is generated from the pipelines.
The steps that I have taken to mitigate the problem are : 
1. Acquire the required artifacts from the Azure DevOps platform even without migrating to it. [Powershell does this job]
2. As the artifacts are in zip format, files are being extracted and analysed for the mention of Vulnerabilties if there are any [Python does this job]
3. In the same Python script, the analyzed result is written concisely to a .txt file for further action to be taken i.e. to solve the vulnerabilties. [Same guy, Mr.Python]
4. A Shell script to execute the above Powershell and Python scripts - one command to rule them all and get the results in roughly about 3 seconds.
    
## Getting Started
  - Firstly, you'll need to generate PAT - Personal Access Token from Azure DevOps!
 ![PAT procedure](Images/PAT.png)

  - Create a file 'inputVariables.ps1' under Scripts folder and add in the credentials.
  
      Credentials        | Example
      ------------------ | -------------
      $MyPat =           | Personal Access token
      $DefinitionName =  | Repository Name
      $Branch =          | Branch Name
      $Company =         | Organisation Name under which Azure DevOps is registered
      $Project =         | Team Name registered under AzureDevOps
      $ArtifactName =    | Scan name to be analyzed. Name to be referred from artifacts under Azure Pipelines
      $DownloadTo =      | Download path - where the artifacts zip file is downloaded.

## Installation

Head over to Scripts folder and open an integrated terminal and run this command to get the results:
```bash
  ./run.sh
```
Sample output images generated under Output folder.

## Output

* Output if there are vulnerabilties : 
  ![Without vulnerabilties - output](Images/OutputWithVuls.jpg)
* Output if there are NO vulnerabilties :
  ![With vulnerabilties - output](Images/OutputWithoutVuls.png)
## Roadmap
- Try to explore Metadefender, Blackduck and other scans.
## License

[MIT](https://choosealicense.com/licenses/mit/)
