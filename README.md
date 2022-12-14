# StringsAPK

## Introduction

StringsAPK is a cross-platform tool that aids a penetration tester to find intresting strings inside an APK file, thus aiding the static code analysis process during android app penetration testing.

## Installation
  
### Pre-requisites
  
  StringsAPK requires `apktool` to decompile the application. So, `apktool` being installed is crucial. You can find guide on how to install apktool on your specific platform at [How to install APKTOOL](https://ibotpeaches.github.io/Apktool/install/).
  
  StringsAPK requires the python module termcolor.
  To install this module run:
  
  `pip install termcolor`
  
  #### or
  
  `pip install -r requirements.txt`
  
### Operation

  To find intresting strings inside of a APK file, first create a wordlist that contains all the intresting keywords. This wordlist will aid StringsAPK to look for specific keywords inside the decompiled APK. Upon running StringsAPK a directory named decompiledFiles will be created along with a report.txt file that will contain the result output of our script.
  
  To run StringsAPK on a APK file enter the following command:
  
  `python3 stringsapk.py <path to apk> <path to wordlist>`
