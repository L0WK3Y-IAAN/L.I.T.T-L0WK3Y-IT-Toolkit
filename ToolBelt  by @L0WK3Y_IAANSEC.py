#!/usr/bin/env python
from pyfiglet import Figlet
import subprocess
import random
import string
import time
import sys
import optparse
import sys, traceback
import termcolor
from sys import platform

def osCheck():
            if platform == "linux" or platform == "linux2":
                
                def linux():#Linux Commands
                    try:
                        nums = random.choice(string.digits)
                        randomString = 'a' + 'b' + 'c' + 'd' + 'e' + 'f'
                        numberList = '0', '2', '4', '6', '8'
                        randomNums = random.choice(numberList)
                        subprocess.call(["clear"])
                        print('[+] Toolbelt v1.0 by @L0WK3Y_IAANSEC [+]')
                        custom_fig = Figlet(font='isometric1')
                        print(custom_fig.renderText("IAAN"))
                        time.sleep(2)
                        subprocess.call(["clear"])
                        # modeSelection = raw_input ("1. Auto MAC Generator \n2. Manual MAC Entry\n3. IP Address Generator \nMode: ")
                        modeSelection = raw_input ("1. MAC Changer\n2. IP Address Generator \n3. Network Interface Modes \n4. System Updates & Upgrades \nMode: ")


                        if modeSelection == '1':
                            subprocess.call('clear')
                            def MACchanger():
                                macChanger = raw_input ("1. Auto MAC Generator \n2. Manual MAC Entry\nMode: ")
                                if macChanger == '1':
                                    subprocess.call(['clear'])
                                    def autoMacGenerator():
                                        print("[+] Mode 1. |Auto MAC Generator| selected.")
                                        time.sleep(1.5)
                                        subprocess.call(['clear'])
                                        subprocess.call(["ifconfig"])
                                        time.sleep(1)
                                        interface = raw_input("Enter name of wireless interface : ")

                                        zero = '0'
                                        a = random.choice(randomString)
                                        b = random.choice(randomString)
                                        c = random.choice(randomString)
                                        d = random.choice(randomString)
                                        e = random.choice(randomString)
                                        macArray = [zero + zero + ':' + randomNums + a + ':' + zero + b + ':' + randomNums + c + ':' + zero + d + ':' + randomNums + e]
                                        mac=''.join(macArray)
                                        #add and option for user to enter a mac address manually (if statement)
                                        # manualMac = raw_input("Enter your MAC address.")

                                        # interface = options.interface
                                        # manualMac = options.manualMac

                                        def generationAnimation():
                                            print("[+] Generating new MAC address.")
                                            animation = "|/-\\"

                                            for i in range(10):
                                                time.sleep(0.1)
                                                sys.stdout.write("\r" + animation[i % len(animation)])
                                                sys.stdout.flush()
                                        time.sleep(.5)
                                        generationAnimation()


                                        print('\n' + "[+] MAC generation complete.")
                                        time.sleep(.5)
                                        print("[+] Your new MAC address is " + mac)
                                        time.sleep(.5)

                                        # subprocess.call("sudo ifconfig " + interface + " down", shell=True) (Less secure way, subprocess.call() can be exploited and used to execute other linux commands using ";" after defining the interface input)

                                        #More secure usage of subprocess.call()
                                        subprocess.call(["sudo", "ifconfig", interface, "down"]) 
                                        print('[+] Shutting down ' + interface)
                                        time.sleep(.5)
                                        # subprocess.call("sudo ifconfig " + interface + " hw ether " + mac, shell=True)
                                        subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac])
                                        print('[+] Applying new MAC address to ' + interface)
                                        time.sleep(.5)
                                        # subprocess.call("sudo ifconfig " + interface + " up", shell=True) 
                                        subprocess.call(["sudo", "ifconfig", interface, "up"]) 
                                        print('[+] Bringing ' + interface + ' back online')
                                        time.sleep(.5)
                                        print('[+] Operation Complete')
                                    autoMacGenerator()
                            

                                if macChanger == '2':

                                    def manualEntry():
                                        print("[+] Mode 2. |Manual MAC Entry| selected.")
                                        time.sleep(1.5)
                                        subprocess.call(['clear'])
                                        subprocess.call(["ifconfig"])
                                        time.sleep(1)
                                        interface = raw_input("Enter name of wireless interface : ")
                                        #add and option for user to enter a mac address manually (if statement)
                                        # manualMac = raw_input("Enter your MAC address.")

                                        # interface = options.interface
                                        # manualMac = options.manualMac
                                        manualMac = raw_input("Enter your new MAC address: ")

                                        time.sleep(.5)
                                        print("[+] Your new MAC address is " + manualMac)
                                        time.sleep(.5)

                                        # subprocess.call("sudo ifconfig " + interface + " down", shell=True) (Less secure way, subprocess.call() can be exploited and used to execute other linux commands using ";" after defining the interface input)

                                        #More secure usage of subprocess.call()
                                        subprocess.call(["sudo", "ifconfig", interface, "down"]) 
                                        print('[+] Shutting down ' + interface)
                                        time.sleep(.5)
                                        # subprocess.call("sudo ifconfig " + interface + " hw ether " + mac, shell=True)
                                        subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", manualMac])
                                        print('[+] Applying new MAC address to ' + interface)
                                        time.sleep(.5)
                                        # subprocess.call("sudo ifconfig " + interface + " up", shell=True) 
                                        subprocess.call(["sudo", "ifconfig", interface, "up"]) 
                                        print('[+] Bringing ' + interface + ' back online')
                                        time.sleep(.5)
                                        print('[+] Operation Complete')
                                    manualEntry()
                            MACchanger()

                        if modeSelection == '2':
                            subprocess.call('clear')
                            print("[+] Mode 2. |IP Address Generator| selected.")
                            time.sleep(1.5)
                            def ipGenerator():
                                def generationAnimation():
                                    print("[+] Generating IP addresses.")
                                    animation = "|/-\\"

                                    for i in range(10):
                                        time.sleep(0.1)
                                        sys.stdout.write("\r" + animation[i % len(animation)])
                                        sys.stdout.flush()
                                time.sleep(.5)
                                generationAnimation()
                                print('\n' + "[+] IP generation complete.")
                                time.sleep(.5)
                                subprocess.call(['clear'])
                                def ipList():
                                    ipArray = [1,'.', 2,'.',3,'.',4]
                                    ipArray[0] = random.randint(0, 255)
                                    ipArray[2] = random.randint(0, 255)
                                    ipArray[4] = random.randint(0, 255)
                                    ipArray[6] = random.randint(0, 255)
                                    ipString = ''.join(str(e) for e in ipArray)
                                    print('\n' + ipString)
                                for i in range(10):
                                    ipList()
                            
                            ipGenerator()

                        #add a monitor mode function
                        if modeSelection == '3':
                            subprocess.call(['clear'])
                            interfaceModeSelection = raw_input("1. Monitor Mode\n2. Managed Mode\nMode: ")
                            if interfaceModeSelection == '1':
                                subprocess.call(['clear'])
                                def monitorMode():
                                    print("[+] Mode 1. |Monitor Mode| selected.")
                                    time.sleep(.5)

                                    def autoMacGenerator():
                                        subprocess.call(['clear'])
                                        subprocess.call(["ifconfig"])
                                        time.sleep(1)
                                        interface = raw_input("Enter name of wireless interface : ")

                                        zero = '0'
                                        a = random.choice(randomString)
                                        b = random.choice(randomString)
                                        c = random.choice(randomString)
                                        d = random.choice(randomString)
                                        e = random.choice(randomString)
                                        macArray = [zero + zero + ':' + randomNums + a + ':' + zero + b + ':' + randomNums + c + ':' + zero + d + ':' + randomNums + e]
                                        mac=''.join(macArray)
                                        #add and option for user to enter a mac address manually (if statement)
                                        # manualMac = raw_input("Enter your MAC address.")

                                        # interface = options.interface
                                        # manualMac = options.manualMac

                                        def generationAnimation():
                                            print("[+] Generating new MAC address.")
                                            animation = "|/-\\"

                                            for i in range(10):
                                                time.sleep(0.1)
                                                sys.stdout.write("\r" + animation[i % len(animation)])
                                                sys.stdout.flush()
                                        time.sleep(.5)
                                        generationAnimation()


                                        print('\n' + "[+] MAC generation complete.")
                                        time.sleep(.5)
                                        print("[+] Your new MAC address is " + mac)
                                        time.sleep(.5)

                                        # subprocess.call("sudo ifconfig " + interface + " down", shell=True) (Less secure way, subprocess.call() can be exploited and used to execute other linux commands using ";" after defining the interface input)

                                        #More secure usage of subprocess.call()
                                        subprocess.call(["sudo", "ifconfig", interface, "down"]) 
                                        print('[+] Shutting down ' + interface)
                                        time.sleep(.5)
                                        # subprocess.call("sudo ifconfig " + interface + " hw ether " + mac, shell=True)
                                        subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac])
                                        print('[+] Applying new MAC address to ' + interface)
                                        time.sleep(.5)

                                        subprocess.call(['sudo', 'iwconfig', interface, 'mode', 'monitor'])
                                        print('[+] Monitor mode now active on ' + interface)
                                        time.sleep(.5)
                                        # subprocess.call("sudo ifconfig " + interface + " up", shell=True) 
                                        subprocess.call(["sudo", "ifconfig", interface, "up"]) 
                                        print('[+] Bringing ' + interface + ' back online')
                                        time.sleep(.5)
                                        print('[+] Operation Complete')
                                    autoMacGenerator()
                                monitorMode()
                            if interfaceModeSelection == '2':
                                subprocess.call(['clear'])
                                def managedMode():
                                    print("[+] Mode 2. |Managed Mode| selected.")
                                    time.sleep(.5)
                                    subprocess.call(['clear'])
                                    subprocess.call(["ifconfig"])
                                    time.sleep(1)
                                    interface = raw_input("Enter name of wireless interface : ")
                                    subprocess.call(["sudo", "ifconfig", interface, "down"]) 
                                    print('[+] Shutting down ' + interface)
                                    time.sleep(.5)
                                    subprocess.call(["sudo", "ifconfig", interface, "up"]) 
                                    print('[+] Bringing ' + interface + ' back online')
                                    time.sleep(.5)
                                    print('[+] Managed mode now active on ' + interface)
                                    time.sleep(.5)
                                    print('[+] Operation Complete')
                                managedMode()
                        if modeSelection == '4':
                            subprocess.call(['clear'], shell=True)
                            print("[+] Mode 4. |System Updates & Upgrades| selected.")
                            subprocess.call("sudo apt-get update && sudo apt-get upgrade", shell=True)
                    except KeyboardInterrupt:
                        termcolor.cprint(text="\nShutdown requested...exiting\n", color="red") 
                    except Exception:
                        traceback.print_exc(file=sys.stdout)
                    sys.exit(0)

                if __name__ == "__main__":
                    linux()
               
            elif platform == "darwin":
                print('os x')
            elif platform == "win32":
                print('windows')
osCheck()

#Adds command options such as "--help" or "-i" 
# parser = optparse.OptionParser()

# parser.add_option("-i", "--interface", dest="interface", help="Set interface to change MAC address.")
# parser.add_option("-m", "--mac", dest="manualMac", help="Manually set a MAC address.")

# (options, arguments) = parser.parse_args()
