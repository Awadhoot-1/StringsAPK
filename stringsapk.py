import os
import re
import sys
from termcolor import colored
import argparse

def decompile_apk(path):
    # Decompiling using apktool
    os.system("apktool d " + path + " -o decompiledfiles -f")
    return 0 

def word_list(wpath):
    with open(wpath, "r") as file:
        text = file.read()
    word_list = text.split()
    array = []
    for word in word_list:
        array.append(word)
    return array    
    
def string_finder(words): # Finds strings in the decompiled files 
    path = os.getcwd() + "\decompiledfiles"
    filelist = []
    for (root, dirs, files) in os.walk(path):
	    for file in files:
            #append the file name to the list
		    filelist.append(os.path.join(root,file))
    text = ''    
    for fpath in filelist:
        # Reading Decompiled files
        with open(fpath, 'r', errors="ignore") as f:        
            lines = f.readlines()
            for line in lines:
                for word in words:
                    # Searching for keywords
                    if re.search(word, line, re.IGNORECASE):
                        print(colored("Found! | " + line + "\nPath   | " + fpath + "\n", 'green' ) )
                        text+="".join (["Found! | ", line, "\nPath   | ", fpath, "\n"])
                        continue
                    else:
                        continue
    with open('report.txt', 'w') as report:
        report.write(text)

def main():
    print("\n")
    print(colored(r"███████╗████████╗██████╗ ██╗███╗   ██╗ ██████╗ ███████╗ █████╗ ██████╗ ██╗  ██╗", 'red'))
    print(colored(r"██╔════╝╚══██╔══╝██╔══██╗██║████╗  ██║██╔════╝ ██╔════╝██╔══██╗██╔══██╗██║ ██╔╝", 'red'))
    print(colored(r"███████╗   ██║   ██████╔╝██║██╔██╗ ██║██║  ███╗███████╗███████║██████╔╝█████╔╝ ", 'red'))
    print(colored(r"╚════██║   ██║   ██╔══██╗██║██║╚██╗██║██║   ██║╚════██║██╔══██║██╔═══╝ ██╔═██╗ ", 'red'))
    print(colored(r"███████║   ██║   ██║  ██║██║██║ ╚████║╚██████╔╝███████║██║  ██║██║     ██║  ██╗", 'red'))
    print(colored(r"╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝", 'red'))
    print("\n")
                                                                               
    parser = argparse.ArgumentParser()
    parser.add_argument("APKPath", help="Path to the APK file", type=str)
    parser.add_argument("Wordlist", help="Path to wordlist", type=str)
    args = parser.parse_args()
    decompile_apk(args.APKPath)
    w=word_list(args.Wordlist)
    string_finder(w)
if __name__ == "__main__":
    main()

