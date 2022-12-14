# Script to download the latest artifact from a DevOps build pipeline
#------------------------------------------------------------
. .\inputVariables.ps1
$MyPat
$DefinitionName
$Branch
$Company
$Project
$ArtifactName
$DownloadTo
#------------------------------------------------------------
# Build Auth header
$B64Pat = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes(":$MyPat"))
$h = @{'Authorization' = 'Basic ' + $B64Pat}

# Get build definition id
$response = Invoke-WebRequest -Uri "https://dev.azure.com/$($Company)/$($Project)/_apis/build/definitions?name=$($DefinitionName)&api-version=6.0" -Method 'GET' -Headers $h -UseBasicParsing
$response_json = ($response.Content | ConvertFrom-Json)
$DefinitionId = $response_json.value.id

# Get latest build id for named branch
$response = Invoke-WebRequest -Uri "https://dev.azure.com/$($Company)/$($Project)/_apis/build/latest/$($DefinitionId)?branchName=$($Branch)&api-version=6.0-preview" -Method 'GET' -Headers $h -UseBasicParsing
$response_json = ($response.Content | ConvertFrom-Json)
$BuildId = $response_json.id

# Download latest named artifact
$response = Invoke-WebRequest -Uri "https://dev.azure.com/$($Company)/$($Project)/_apis/build/builds/$($BuildId)/artifacts?artifactName=$($ArtifactName)&api-version=7.0" -Method 'GET' -Headers $h -UseBasicParsing
$response_json = ($response.Content | ConvertFrom-Json)
$response_json.resource.downloadUrl
$response_artifact = Invoke-WebRequest -Uri $response_json.resource.downloadUrl -Method 'GET' -Headers $h -UseBasicParsing -OutFile "$($DownloadTo)"