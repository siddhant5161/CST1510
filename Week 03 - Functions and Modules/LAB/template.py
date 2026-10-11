def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
    
def check(value, limit):
    difference = limit - value
    percent = (value/limit)*100
    return difference, percent

label = input("Enter the hostname /press 'q' to exit:")        
value = float(input("Enter the value: "))    
limit = float(input("enter the limit: "))    

difference,percent =  check(value, limit)              
status = status_of(percent)        

def print_report(label,value,limit,difference,percent,status):
    return {"label":label,"value":value,"limit":limit,"difference":difference,"percent":percent,"status":status}

report = print_report(label,value,limit,difference,percent,status)

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

def final_report(**report):
    for ky,val in report.items():
        if ky == "q":
            break
        elif ky == "percent":
            print(f"\n{ky.title()}\t:\t{val:>+10.2f}%")
        elif ky == "label" or "status":
            print(f"\n{ky.title()}\t:\t{val:>10}")
        else:
            print(f"\n{ky.title()}\t:\t{val:>+10.2f}")
            
final_report(**report)
