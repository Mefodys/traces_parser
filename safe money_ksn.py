import codecs
b="KAV.20.0.14.1085g_01.15_20.01_4728.SRV.log"

print ("    Trace parcer 1.0")
print ("---")

print ("---Safe money---")
try:
    with codecs.open(b,'r',encoding='utf-8',errors='ignore') as opened_file:  # OR the file can be opened liek the following ## trace_file=open(opened_file,'r')
        for line in opened_file:
            if "sbank	Settings is :" in line:
                print(line)
            elif "sbank.safe_browser_controller"  in line:
                print(line)
            elif "sbank.browser_environment_state_controller"  in line:
                print(line)
            elif "Protected domain detected:"  in line:
                print(line)
            elif ". Set BankClient container"  in line:
                print(line)
            elif "sbank.ui_host_session_manager" in line:
                print(line)
            elif "Hypervisor status for SafeBrowser" in line:
                print(line)
            elif "OnSafeBrowserTreeExit " in line:
                print(line)
                           
except OSError:
    # 'File not found' error message.
    print ("File not found")


##ksn search
#dnsclnt	Received 	
#GetCurrentRoute for service 
#ksnclnt	Service 
#OnPingTimeout
#Network status 
#Service CERTINFO
