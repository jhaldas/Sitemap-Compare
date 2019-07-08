import requests
import sys
import glob, os
import datetime, time
import xml.etree.ElementTree as ET
import itertools


FILE_PATH = "/Users/jhaldas/Documents/Python/Logs/" # Set this to the path that you want your XML files to be saved in
MAX_SITEMAPS = 5 # Set this to the maximum number of sitemaps you want saved at once
URL = "https://www.cctvcamerapros.com/sitemap.xml" # Set this to the URL of the sitemap
SEND_EMAIL = True # Set True if you want to be emailed, False if not.


# Downloads the sitemap given a URL, a path to save the
#sitemaps to, and the maximum amount of sitemaps at a time.
def downloadXML(URL, location, maxFiles):

    currentDT = datetime.datetime.now()
    filename = currentDT.strftime("%Y-%m-%d_%H-%M-%S%p")
    
    response = requests.get(URL)
    with open(location + filename + ".xml", "wb") as file:
        file.write(response.content)

    os.chdir(location)

    list_of_files = os.listdir()
    
    if len(glob.glob("*.xml")) > maxFiles:
        files = []

        # Returns list of file paths and adds them to the files list
        for r, d, f in os.walk(location):
            for file in f:
                if '.xml' in file:
                    files.append(os.path.join(r, file))
        for path in files:
            print(path)
            # Gets the creation time of each file
            print(os.path.getctime(path))

        oldest_file = min(files, key=os.path.getctime)

        os.remove(oldest_file)

    
def compareXML(path, sendEmail):
    
    os.chdir(path)

    list_of_files = os.listdir()

    files = []

    for r, d, f in os.walk(path):
        for file in f:
            if '.xml' in file:
                files.append(os.path.join(r, file))

    # Sorts the list in order of oldest to newest based on time created
    files.sort(key=os.path.getctime)

    # Sets newest and second newest file based on sorted list
    newestFile = files[len(files)-1]
    secondNewestFile = files[len(files)-2]

    # Turns newest files into Lists
    list1 = XMLtoList(newestFile)
    list2 = XMLtoList(secondNewestFile)

    print("Comparing", newestFile, "with", secondNewestFile)

    newLinks = ""
    missingLinks = ""

    for i in list1:
        if i in list2:
            pass
        else:
            print("Found new link:", i)
            newLinks += i + '\n'
            
    for j in list2:
        if j in list1:
            pass
        else:
            print("Missing Link!", i)
            missingLinks += j + '\n'
            
    print("New Links:", newLinks)
    print("Missing Links:", missingLinks)

    if sendEmail == True:
        email_alert(newLinks, missingLinks)
            
# Takes an sitemap xml and converts into a list of URL strings.
def XMLtoList(xml):
    children = []
    tree = ET.parse(xml)
    root = tree.getroot()
       
    for child in root:
        children.append(child[0].text)

    return children

# Emails you the differences of the 
def email_alert(first, second):
    print("sending email")
    report = {}
    report["value1"] = first
    report["value2"] = second
    requests.post("https://maker.ifttt.com/trigger/XML_Notification/with/key/iyZRNsw8-r29Ro3xjaoMwcLxb-v2J4VxH08z_zO8NvD", data=report)  


downloadXML(URL, FILE_PATH, MAX_SITEMAPS)
compareXML(FILE_PATH, SEND_EMAIL)    




