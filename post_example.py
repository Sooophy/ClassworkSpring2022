from types import WrapperDescriptorType
import requests

# out_data = {
#     "name": "David Ward",
#     "net_id":"daw74",
#     "e-mail": "111@duke.edu",
# }
# r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
# print(r.text)

# r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
# print(r.text)


# message = {
#     "user": "Sophie",
#     "message": "Hello",
# }

# r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
# json=message)
# print(r.text)

# r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/Maxine")
# print(r.text)


# id = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/ys331")
# print(id.text)

# p1 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F4")
# print(p1.text)  # B-

# p2 = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M7")
# print(p2.text)  # AB+

bloodinfo = {
    "Name": "ys331",
    "Match": "Yes"
}

r = requests.post(
    "http://vcm-7631.vm.duke.edu:5002/match_check", json=bloodinfo)
print(r.text)
