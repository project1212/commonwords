#commonwords

To start server run file webservice.py. This will start on local port 8080. The sentences.json file contains
the sentences which will be compared for similarities. Input1 and Input2 are the ones which are used by the script, input3 is just a place holder for testing. Key 'removeSpecialChar' takes a value of true or false, it gives the user the ability to remove special characters or not from the comparison. After starting the server you can test with curl -d "@sentences.json" -H "Content-Type: application/json" -X POST http://localhost:8080/process