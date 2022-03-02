import requests


r = requests.get(
    "https://api.github.com/repos/dward2/BME547/branches"
)

print(r)
print(type(r))
print("Status code = {}".format(r.status_code))
print("Text = {}".format(r.text))

if r.status != 200:
    print("There was a problem")
    print(r.text)
    exit()

answer = r.json()  # answer is a long string

for branch in answer:
    print(branch["name"])


print("done")
