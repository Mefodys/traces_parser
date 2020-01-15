import codecs
b="KAV.20.0.14.1085g_01.15_20.01_4728.SRV.log"
#incorrect=-1
#print (incorrect)
#print (type(incorrect))

print ("    Trace parcer 1.0")
print ("---")

proxy_sessions_list=[]
print ("---traffic ERR---")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
        for line in opened_file:
            if  "ERR	trafmon	ProxySession" in line:
                a=line.find ("Session(")
                b=line.find ("): ")
                #print ("a=",a)
                #print ("b=",b)
                #print(type(a))
                #print(type(b))
                #if a == incorrect:
                #    print ("a or b = -1")
                proxy_session_number=(line[a+8:b])
                #print ("proxy_session_number",proxy_session_number)
                proxy_sessions_list.append(int(proxy_session_number))
                proxy_sessions_counter=len(proxy_sessions_list)
            elif "ERR	ssl	ProxySession("  in line:
                c=line.find ("Session(")
                d=line.find ("): ")
                proxy_session_number=(line[c+8:d])
                proxy_sessions_list.append(int(proxy_session_number))
                proxy_sessions_counter=len(proxy_sessions_list)
            elif "ERR	http	ProxySession("  in line:
                e=line.find ("Session(")
                f=line.find ("): ")
                proxy_session_number=(line[e+8:f])
                proxy_sessions_list.append(int(proxy_session_number))
        proxy_sessions_list.sort()
        proxy_sessions_counter=len(proxy_sessions_list)
        print("proxy_sessions_counter",proxy_sessions_counter)
        print("proxy_sessions_list",proxy_sessions_list)
        #print("proxy_sessions_list_sorted",proxy_sessions_list_sorted)
        #print (type(proxy_sessions_list))
        print ("===")
                    #    print(line)
            #elif "ERR	ssl"  in line:
            #    print(line)
            #elif "ERR	http"  in line:
            #    print(line)

                
                
                                       
except OSError:
    # 'File not found' error message.
    print ("File not found")


print ("---traffic ERR sessions---")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
        for line in opened_file:
            if  "ProxySession" in line:
                for i in range(proxy_sessions_list):
                    if "ProxySession("+proxy_sessions_list[i] in line:
                        print(line.strip())

                
                
                                       
except OSError:
    # 'File not found' error message.
    print ("File not found")
