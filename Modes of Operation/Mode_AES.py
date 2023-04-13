import CBC_AES
import ECB_AES
import OFB_AES


mode = input("Please input your mode\n")

if mode == "ECB":
    inputFileName = input("Please input your inputFile\n")
    outputFileName = input("Please input your outputFile\n")
    key = input("Please input your key\n")
    operation = input("Please input encode(e) or decode(d)\n")
    inputFILE = open(inputFileName, "r")
    s = inputFILE.read()
    outputFILE = open(outputFileName, "w")
    if(operation == 'e'):
        outputFILE.write(ECB_AES.encryptECB_AES(s, key))
    elif(operation == 'd'):
        outputFILE.write(ECB_AES.decryptECB_AES(s, key))
    else:
        print("Error: Wrong operation\n")
elif mode == "CBC":
    inputFileName = input("Please input your inputFile\n")
    outputFileName = input("Please input your outputFile\n")
    key = input("Please input your key\n")
    IV = input("Please input your IV\n")
    operation = input("Please input encode(e) or decode(d)\n")
    inputFILE = open(inputFileName, "r")
    s = inputFILE.read()
    outputFILE = open(outputFileName, "w")
    if(operation == 'e'):
        outputFILE.write(CBC_AES.encryptCBC_AES(s, key, IV))
    elif(operation == 'd'):
        outputFILE.write(CBC_AES.decryptCBC_AES(s, key, IV))
    else:
        print("Error: Wrong operation\n")
elif mode == "OFB":
    inputFileName = input("Please input your inputFile\n")
    outputFileName = input("Please input your outputFile\n")
    key = input("Please input your key\n")
    IV = input("Please input your IV\n")
    operation = input("Please input encode(e) or decode(d)\n")
    inputFILE = open(inputFileName, "r")
    s = inputFILE.read()
    outputFILE = open(outputFileName, "w")
    if(operation == 'e'):
        outputFILE.write(OFB_AES.encryptOFB_AES(s, key, IV))
    elif(operation == 'd'):
        outputFILE.write(OFB_AES.decryptOFB_AES(s, key, IV))
    else:
        print("Error: Wrong operation\n")
