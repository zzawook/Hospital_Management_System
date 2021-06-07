import pickle

def run():
    fileName="patientDatabase.txt"
    #infile=open(fileName,"rb")
    #prevData=pickle.load(infile)
    #infile.close()
    outfile=open(fileName, 'wb')
    prevData=[] #[{'name': 'Jae Hyeok', 'phone number': '6380837438', 'date of birth': (2002, 1, 25), 'gender': 0, "id" : '0', "address":""}]
    pickle.dump(prevData, outfile)
    outfile.close()
if __name__=="__main__":
    run()