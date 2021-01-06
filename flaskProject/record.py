# Author: Autumnhui
def log_request(req:'flask_request',res:'str'):
    with open('vsearch.log','a') as log:
        print(req,res,log)
