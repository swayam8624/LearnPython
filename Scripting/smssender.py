#41TFZ3MGMFK7G6SKFW4YZRU2
'''
from twilio.rest import Client

acc_sid = "..s.dabs.dsg.s"
auth_token="[auth token]"

client = Client(acc_sid , auth_token

message = client.message.create(
from _ = "+.....", # should be verified
body = "helloooooo",
to= "+919830130032" #should be verified
)
print(message.sid)

#message will be : sent from a twilio trial account - helloooooo
'''

# better api - nfty