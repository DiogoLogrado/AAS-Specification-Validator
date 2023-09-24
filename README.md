# AAS-Specification-Validator
Executable Program that checks AAS Implementations conformance with the AAS Specification

# Usage
Download both files and use an IDE (for example Microsoft Visual Studio) to open the aas_json_validator.py.

Setup your AAS endpoint of preference and inside the "USER INPUT" of the Python code change the variables "endpoint" and "interface_operation" with the endpoint that you are using and then the path of the operation you want to test (check #Supported-Operations).
You also need to change inside the file reading statement with the location of the aas_specification_schema.json on your computer.

# Supported-Operations
-GetAssetAdministrationShell
-GetSubmodelElementById
-GetAllAssetAdministrationShells
-GetAssetAdministrationShellById
-GetAllSubmodels
-GetSubmodelById
