"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
    '''this takes value and limit and returns difference, percent and status'''
    difference = limit - value
    percent = (value/limit)*100
    status = "OVERLIMIT" if value>limit else "OK"
    return difference,percent,status

def print_report(label,value,limit,difference,percent,status):
    '''this prints the whole report'''
    return {"label":label,"value":value,"limit":limit,"difference":difference,"percent":percent,"status":status}
# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

def load_records(path):
    record = []
    try:
        with open(path) as f:
            new = f.readlines()
            for n in new:
                label,value,limit = n.strip().split(",")
                value,limit = float(value),float(limit)
                new1 = {"label":label,"value":value,"limit":limit}
                record.append(new1)
            
        return record
    except FileNotFoundError:
        print("fine not found, check the name of the file or directory")
        record = []
        return record

records = load_records("/home/siddhantdoshi21/Downloads/CST1510_Week4/Week 04 - Lists, Dictionaries and Files/LAB/datasets.txt")

    

# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here


with open("results.txt","w") as f:
    overlimit = 0
    for record in records:
        label = record["label"]
        value = record["value"]
        limit = record["limit"]
        difference,percent,status = check_record(value,limit)
        if status == "OVERLIMIT":
            overlimit += 1
        print(print_report(label,value,limit,difference,percent,status))
        f.write(f"{label}, {status}\n")
    f.write(f"\ntotal overlimits: {overlimit}")
# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
