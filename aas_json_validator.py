import jsonschema
import json
import requests

#----------------USER INPUT----------------

#User endpoint input
endpoint = "http://localhost:..."

#Method / Operation
interface_operation = "Get..."

#Load AAS JSON Schema
with open('FILE LOCATION AAS SCHEMA') as f:
    schema_str = f.read()

#----------------DO NOT ALTER BELOW----------------

#API Request
status_code = str(requests.get(endpoint).status_code)
json_data = None
if status_code == "200" or status_code == "201" :
    json_data= json.loads(requests.get(endpoint).text)

#Fetch Operation Path
json_schema= json.loads(schema_str)
schema_for_path = json_schema.get("paths", {}).get(interface_operation, {}).get("get", {}).get("responses", {}).get(status_code, {}).get("schema")

#Validate JSON against the extracted schema
if json_data:
    try:
        jsonschema.validate(json_data, schema_for_path)
        print("JSON is valid according to the schema.")
    except jsonschema.ValidationError as e:
        print("JSON is not valid according to the schema.")
        print(e)
else:
    print(schema_for_path.get("description", {}))
