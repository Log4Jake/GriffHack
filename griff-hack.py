import os
import sys
os.system("pip install -U scratchattach")
import os.path
import scratchattach as scratch3
from scratchattach import Encoding
from time import sleep
username = 'YourUsername' #add your username The username field is case sensitive
sessionId = "sessionID" #add your sessionID
session = scratch3.Session(sessionId, username=username)
conn = session.connect_cloud('Your Remix project ID') #add your remixed project ID
variables = scratch3.get_cloud('Your Remix project ID') #add your remixed project ID 
conn = session.connect_cloud('843162693') #add Original Project ID

def run_forever():
        try:
                while True:
                        for key in variables:
                                conn = scratch3.TwCloudConnection(project_id = "Your Remix project ID", username=username) #add your remixed project ID 
                                var = conn.get_var(key)
                                conn = session.connect_cloud('843162693') #add Original Project ID
                                if var == 'None':
                                        #do nothing
                                        print(var)
                                else:
                                        conn.set_var(key, var)
                                        print(var)
        except Exception:
                print("error")
                handle_exception()
                run_forever()
	
def handle_exception():
        # code here
        pass
    
run_forever()
