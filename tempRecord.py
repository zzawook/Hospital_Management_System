import pickle

def run():
    fileName = "serviceDatabase.txt"
    outfile = open(fileName, 'wb')
    prevData = [{"recordId": "0", "patientId": "0", "date": (2020, 5, 1), "symptom": "Slight fever and cold", "diagnose": "Simple allergy", "prescription": "Take some rest"}]
    pickle.dump(prevData, outfile)
    outfile.close()

    infile = open(fileName, "rb")
    nowData = pickle.load(infile)
    print(nowData)
    print("hello")

if __name__=="__main__":
    run()