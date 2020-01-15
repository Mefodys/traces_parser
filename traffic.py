import codecs
b="KAV.20.0.14.1085g_01.15_20.01_4728.SRV.log"

print ("    Trace parcer 1.0")
print ("---")

print ("---traffic---")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
        for line in opened_file:
            if "OUTBOUND connection from PID=" in line:
                print(line)
            elif ": REMOTE NAME set to"  in line:
                print(line)
            #elif ": Protocol detected"  in line:
            #    print(line)
            elif ": SSL decode mode is"  in line:
                print(line)
            elif "    () DECODE"  in line:
                print(line)
            elif ": Connecting to server"  in line:
                print(line)
            elif "ProcessData() for filter"  in line:
                print(line)
            elif "ERR	trafmon" in line:
                print(line)
            elif "ERR	ssl"  in line:
                print(line)
            elif "ERR	http"  in line:
                print(line)

                
                
                                       
except OSError:
    # 'File not found' error message.
    print ("File not found")


##
proxy_sessions_list=[]
print ("---traffic ERR---")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
        for line in opened_file:
            if  "ERR	trafmon" in line:
                a=line.find ("Session(")
                b=line.find ("): ")
                print ("a=",a)
                print ("b=",b)
                #print(type(a))
                #print(type(b))
                if a or b == "-1":
                    break
                
                proxy_session_number=(line[a+8:b])
                print ("proxy_session_number",proxy_session_number)
                proxy_sessions_list.append(proxy_session_number)
                print("proxy_sessions_list",proxy_sessions_list)
                proxy_sessions_counter=len(proxy_sessions_list)
                print("proxy_sessions_counter",proxy_sessions_counter)
                
            #    print(line)
            #elif "ERR	ssl"  in line:
            #    print(line)
            #elif "ERR	http"  in line:
            #    print(line)

                
                
                                       
except OSError:
    # 'File not found' error message.
    print ("File not found")


