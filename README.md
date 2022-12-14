# StringsAPK

## Introduction

StringsAPK is a cross-platform tool that aids a penetration tester to find intresting strings inside of an APK file, thus aiding the static code analysis process during android app penetration testing.
  
## Pre-requisites
  
  StringsAPK requires `apktool` to decompile the application. So, `apktool` being installed is crucial. You can find guide on how to install apktool on your specific platform at [How to install APKTOOL](https://ibotpeaches.github.io/Apktool/install/).
  
  StringsAPK requires the python module termcolor.
  To install this module run:
  
  `pip install termcolor`
  
  #### or
  
  `pip install -r requirements.txt`
  
### Operation

  To find intresting strings inside of a APK file, create a wordlist that contains all the keywords. This wordlist will aid StringsAPK to look for specific keywords inside the decompiled APK. Upon running StringsAPK a directory named `decompiledFiles` that will be created which contains the decompiled APK along with a `report.txt` file that will contain the output of the script.
  
  To run StringsAPK on a APK file enter the following command:
  
  `python3 stringsapk.py <path to apk> <path to wordlist>`
