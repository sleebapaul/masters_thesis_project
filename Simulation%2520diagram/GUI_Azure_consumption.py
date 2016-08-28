from Tkinter import *
import urllib2 # If you are using Python 3+, import urllib instead of urllib2
import json 

fields = 'Loading (MW)','SD4', 'SD3', 'E4', 'E3'

def fetch(entries):
   text=[]
   for entry in entries:
      text.append(entry[1].get())
   text.append('1')
   data =  {"Inputs":{"input1":{"ColumnNames":["Loading", "SD4", "SD3", "E4", "E3", "Label"],"Values":[text]}},"GlobalParameters":{}}
   body = str.encode(json.dumps(data))
   url = 'https://ussouthcentral.services.azureml.net/workspaces/8e3a01b9b5a94cd8be8f69c85bfd1215/services/923ca965d52a46788d91c32cd9cdc9fd/execute?api-version=2.0&details=true'
   api_key = 'zogVJpUKUmTEEh3auMuVYZ1q1tBKBWA+tHeZWIyzuG2sYUfxHKJ7F4IpXhGALe5IiVpunzMHjDF8i0gTImfqfA==' # Replace this with the API key for the web service
   headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
   req = urllib2.Request(url, body, headers)
   try:
      response = urllib2.urlopen(req)
      # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
      # req = urllib.request.Request(url, body, headers) 
      # response = urllib.request.urlopen(req)
      result = response.read()
      out=json.loads(result)
      score=out['Results']['output1']['value']['Values'][0][12]
      if score=='1':
         status=" No Events"
      elif score =='2':
         status="Islanding"
      elif score=='3':
         status="L-G Fault"
      elif score =='4':
         status=" L-L Fault"
      elif score=='5':
         status="Non-Linear Load Switch"
      w4.configure(text="STATUS : "+status)
   except urllib2.HTTPError, error:
      print("The request failed with status code: " + str(error.code))
      # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
      print(error.info())
      print(json.loads(error.read()))

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append([field, ent])
   return entries
def quit():
    root.destroy()
if __name__ == '__main__':
   root = Tk()
   root.title('Disturbance Predictor ')
   root.geometry('530x350')
   new=Frame(root)
   w2=Label(new,text='1.75 MW HYBRID SYSTEM',anchor='w')
   w3=Label(new,text='PV (Rated) - 0.25 MW  ',anchor='w')
   w5=Label(new,text='Wind Plant (Rated) - 1.5 MW  ',anchor='w')
   w6=Label(new,text='Grid Voltage - 25 kV  ',anchor='w')
   new.pack(side=TOP, fill=X, padx=5, pady=10)
   w2.pack()
   w3.pack(side=LEFT)
   w5.pack(side=LEFT)
   w6.pack(side=LEFT)
   ents = makeform(root, fields)
   win=Frame(root)
   w4=Label(win,text='',anchor='w')
   win.pack(side=TOP, fill=X, padx=5, pady=5)
   w4.pack()
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   b1 = Button(root, text='Show',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT,padx=50,pady=5)
   b2 = Button(root, text='Quit', command=quit)
   b2.pack(side=RIGHT,padx=50,pady=5)
   root.mainloop()
