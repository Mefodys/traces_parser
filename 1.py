#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
a=0

print ("    Trace parcer 1.0")
#print ("---")
#print ("1 step - the script asks you to enter name of the trace file")
#print ("2 step - the script asks you to input the paramets of parsing:)
#print ("t - trafmon\ssl\http")
#print ("k - ksn")    
print ("---")
#file_name = input("please enter the filename:\n(the file must be placed to the same folder as the py script)\n")
try:
    with open('KAV.20.0.14.1085g_01.13_17.59_9576.SRV.log','r',encoding='utf-8') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
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
            if "IMP	ldr	" in line:
                print(line)
                
        for line in opened_file:    
            if "ai.sm.loader" in line:
                print (line)
                
                
           








except OSError:
    # 'File not found' error message.
    print ("File not found")

