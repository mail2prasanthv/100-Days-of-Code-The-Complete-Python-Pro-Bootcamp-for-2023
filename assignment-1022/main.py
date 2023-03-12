#Integration with pixela - Record and Track your habits or effort. All by API.
# Create user account
import requests
base_url ="https://pixe.la/"
version = "v1"
uri = "/users"

complete_url = base_url + version + uri
data = {
"token":"mysecretcode",
"username":"learnpython",
"agreeTermsOfService":"yes",
"notMinor": "yes"
}

r = requests.post(complete_url, json=data)
print(r.status_code,r.content)