
def HeaderConvert(toProcess):

    Step1 = toProcess.split("\n" or "\r")



    DataList = []

    TotalCount = len(Step1)
    CurrentCount = 0
    for data in Step1:

        # Split raw headers by title and data        
        CurrentCount+=1 
        Step2 = data.split(': ')
        output = "".join(["'",Step2[0]+"': '",Step2[1].strip(),"'"])
        if CurrentCount < TotalCount:
            output +=','
        
        DataList.append(output)


    TotalCount = len(DataList)
    CurrentCount = 0

    # Output raw data as a dictionary string
    OutputStr = '{'
    for i in DataList:
        CurrentCount +=1
        
        OutputStr += i

        if CurrentCount < TotalCount:
            OutputStr += "\n"


    OutputStr += '}'
    
    return str(OutputStr)




