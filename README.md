# Sitemap-Compare
A Python script with methods to compare XML sitemaps.

# Description
The purpose for this script is to detect discrepancies between sitemaps.  This script has the capability to download and store sitemaps as XML files, convert sitemaps to lists of URL's, compare most recent files given a file location, and email you any changes between most recent sitemaps using IFTTT.

# Usage
This script was made using:
 - <a href="https://docs.python.org/3/library/idle.html">Idle</a>, and Version 3.7.3 of Python, which can both be downloaded <a href="https://www.python.org/downloads/">here</a>. Other versions of Python may work, but Python 3.7.3 is the only version I've tested with.
 - I recommend downloading <a href="https://docs.conda.io/en/latest/miniconda.html">Miniconda</a>, as it comes with many useful libraries, and includes all the libraries used in this script.  Otherwise, you'll have to download the imported libraries included in the script on your own.
 - A <a href="https://ifttt.com/discover">IFTTT</a> account is required if you want to be emailed the list of discrepancies between sitemaps.  
 
## Setting up the IFTTT script
If you want to recieve emails on any sitemap discrepancies, this section is a quick guide on how to make your own IFTTT applet.  This will be a less in depth version of another guide, found <a href="https://anthscomputercave.com/tutorials/ifttt/using_ifttt_web_request_email.html">here</a>.
### Setting up the event on IFTTT
These steps will show you how to create your own event on IFTTT:
1. In the drop down menu under your username, click "New Applet".
2. Click the blue "+this".
3. In the search field, type "Webhooks", and then click the result "Receive a web request".
4. Name your web event, I named mine "Sitemap_Notification".
5. Click "Create Trigger" and then click the blue "+that".
6. In the search field, type and select "Email", then click the result "Send me an email".
7. Name the subject for your email, I used "XML Sitemap Notification".
8. You can choose to create your own body, or you can copy and paste the format I have here: 
'''
Sitemap Discrepancies:<br>
New Links:<br>
{{Value1}}<br><br>
Missing Links:<br>
{{Value2}}<br>
'''
9. Click "Finish"
### Terminal commands
You will need to run these commands in your terminal in order to make sure everything is up to date and installed.
'''
sudo pip install requests
sudo apt-get install python-dev libffi-dev libssl-dev
sudo pip install --upgrade ndg-httpsclient
'''
### Editing the code
This section will explain what you need to change in your code in order to run your IFTTT event through the Python script.
