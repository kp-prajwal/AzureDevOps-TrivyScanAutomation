#!/bin/bash

powershell ./inputVariables.ps1
#download scan artifiacts
powershell ./downloadTrivyJson.ps1
#vulnerability scanning
python getScanDetails.py
$SHELL

#to run this script : ./run.sh