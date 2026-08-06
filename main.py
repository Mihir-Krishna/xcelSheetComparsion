import pandas as pd

def compareExcel(file1Path, file2Path):
    sheet1 = pd.read_excel(file1Path, sheet_name="Sheet1")
    sheet2 = pd.read_excel(file2Path,sheet_name="Sheet1")
    
# print(sheet1)
# print(sheet2)

# print("which rows you want to exclude?")
# rowExcludedValues = [int(x) for x in input("enter values: ").split(
# )]
# print("which columns you want to exclude?")
# columnExcludedValues = input("enter values: ").split()

# sheet1 = sheet1.drop(columns=columnExcludedValues)
# sheet2 = sheet2.drop(columns=columnExcludedValues)
# sheet1 = sheet1.drop(index=rowExcludedValues)
# sheet2 = sheet2.drop(index=rowExcludedValues)


    rows1, columns1 = sheet1.shape   
    rows2, columns2 = sheet2.shape

    print(rows1, columns1)
    print(rows2, columns2)




    def compareShape(rows1, rows2, columns1, columns2):
        if rows1 == rows2 and columns1 == columns2: 
            return True
        else:
            return False
        
    value = compareShape(rows1, rows2, columns1, columns2)
    # print(value)

    sheet1Columns = sheet1.columns.tolist()
    sheet2Columns = sheet2.columns.tolist()

    print(sheet1Columns, sheet2Columns)

    len1 = len(sheet1Columns)
    len2 = len(sheet2Columns)

    for i in range(max(len1,len2)):
        if i < len1 and i < len2:
            if sheet1Columns[i] == sheet2Columns[i]:
                print(f"{i}th attributes match")
            else: 
                print(f"column{i}:{sheet1Columns[i]} != {sheet2Columns[i]}")
        elif i < len1: 
            print(f"column{i}: {sheet1Columns[i]} exists only in sheet 1")
        else: 
            print(f"column{i}:{sheet2Columns[i]} exists only in sheet2")
            
    def presence():
        # Check columns of sheet1 in sheet2
        for column1 in sheet1Columns:
            found = False
            
            for column2 in sheet2Columns:
                if column1 == column2:
                    found = True
                    break
            
            if found == False:
                print(f"{column1} doesn't exist in sheet2")


        # Check columns of sheet2 in sheet1
        for column2 in sheet2Columns:
            found = False
            
            for column1 in sheet1Columns:
                if column2 == column1:
                    found = True
                    break
            
            if found == False:
                print(f"{column2} doesn't exist in sheet1")
                    
                
                    
    print(presence())

    difference = sheet1.compare(sheet2)
    print(difference)
        
    

