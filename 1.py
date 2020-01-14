#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
import codecs
a=0
#b="KAV.20.0.14.1085g_01.14_20.26_9576.SRV.log"
b="KAV.20.0.14.1085g_01.14_21.08_7484.SRV.log"

print ("    Trace parcer 1.0")
#print ("---")
#print ("1 step - the script asks you to enter name of the trace file")
#print ("2 step - the script asks you to input the paramets of parsing:)
#print ("t - trafmon\ssl\http")
#print ("k - ksn")    
print ("---")
#file_name = input("please enter the filename:\n(the file must be placed to the same folder as the py script)\n")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
    #with codecs.open('KAV.20.0.14.1085g_01.13_17.59_9576.SRV.log','r') as opened_file:
        print ("file found!")
        print ("trace file pasring is in process!")
        print ("------")
        #print (opened_file) #show the system info about opene file - name, mode, encoding
                
        for line in opened_file:
            if "TraceFile:" in line:
                level_position=line.find('TraceFile: on ')
                level_value=line[level_position+14:level_position+17]
                #print(type(level_value))
                print('traces level equal',level_value)
                if level_value == '700':
                    print('traces were collected with RECOMMENDED level')
                elif level_value == '800':
                    print('traces were collected with ALL(DBG) level')
                else:
                    print('traces were collected not with ALL or RECOMMENDED level')
                break
            
        for line in opened_file:    
            if "ai.sm.loader	Loaded successfully" in line:
                #print(line)
                print("traces collected from the product start")
except OSError:
    # 'File not found' error message.
    print ("File not found")


print ("---ldr---")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
        for line in opened_file:
           if "ldr	Module" in line:
                print(line)
        for line in opened_file:    
            if "ai.sm.loader" in line:
                print (line)
except OSError:
    # 'File not found' error message.
    print ("File not found")


print ("---ai.sm.loader---")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
        for line in opened_file:
           if "ai.sm.loader" in line:
                print(line)
                #print('no ldr component in the trace file')
except OSError:
    # 'File not found' error message.
    print ("File not found")


print ("---Module---")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
        for line in opened_file:
           if "Module '" in line:
                print(line)
                #print('no ldr component in the trace file')
except OSError:
    # 'File not found' error message.
    print ("File not found")


print ("---esm	Parsing---")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
        for line in opened_file:
           if "esm	Parsing" in line:
                print(line)
                #print('no ldr component in the trace file')
except OSError:
    # 'File not found' error message.
    print ("File not found")

print ("---category---")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
        for line in opened_file:
           if ", category='" in line:
                print(line)
                #print('no ldr component in the trace file')
except OSError:
    # 'File not found' error message.
    print ("File not found")


print ("---drivers---")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
        for line in opened_file:
            if "system_interceptors::driver_log_manager::detail::DriverLogSession::DisplayVersion" in line:
                print(line)
            elif ", C:\WINDOWS\system32\drivers" in line:
                print(line)
            elif "CreateFileByName failed for file:"  in line:
                print(line)
                
except OSError:
    # 'File not found' error message.
    print ("File not found")

print ("---Profile names---")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
        for line in opened_file:
           if "Begin. Profile name - " in line:
                print(line)
except OSError:
    # 'File not found' error message.
    print ("File not found")    	

print ("---State changed---")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
        for line in opened_file:
            if "tm	State changed to " in line:
                 print(line)
            elif "' cannot be started because" in line:
                 print(line)
            
                
except OSError:
    # 'File not found' error message.
    print ("File not found")  

print ("---SSL Domain excludes---")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
        for line in opened_file:
           if "Domain excludes:" in line:
                print(line)
                
except OSError:
    # 'File not found' error message.
    print ("File not found")  


print ("---ClickEvents---")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
        for line in opened_file:
           if "ClickEvent :" in line:
                print(line)
                
except OSError:
    # 'File not found' error message.
    print ("File not found")

print ("---Trusted applications excludes---")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
        for line in opened_file:
            if "<path>" in line:
                print(line)
            elif "<controlTriggersMask>"  in line:
                print(line)
            elif "[ApplicationExclusionsManager]" in line:
                print(line)
            #elif "name='exclude.application_manager'" in line: 
            #    print(line)
            #elif "            <path" in line: 
            #    print(line)
                
except OSError:
    # 'File not found' error message.
    print ("File not found")

