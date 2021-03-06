# Sitemap-Compare
A Python script with methods to compare XML sitemaps.

# Description
The purpose for this script is to detect discrepancies between sitemaps.  This script has the capability to download and store sitemaps as XML files, convert sitemaps to lists of URL's, compare most recent files given a file location, and email you any changes between most recent sitemaps using IFTTT.

# Usage
This script was made using:
 - <a href="https://docs.python.org/3/library/idle.html">Idle</a>, and Version 3.7.3 of Python, which can both be downloaded <a href="https://www.python.org/downloads/">here</a>. Other versions of Python may work, but Python 3.7.3 is the only version I've tested with.  I prefer Idle, but any Python IDE you're comfortable with should work.
 - I recommend downloading <a href="https://docs.conda.io/en/latest/miniconda.html">Miniconda</a>, as it comes with many useful libraries, and includes all the libraries used in this script.  Otherwise, you'll have to download the imported libraries included in the script on your own.
 - An <a href="https://ifttt.com/discover">IFTTT</a> account is required if you want to be emailed the list of discrepancies between sitemaps.  
 
## Email Notifications
If you want to recieve emails on any sitemap discrepancies, this section is a quick guide on how to make your own IFTTT applet.  This is based off of another guide, found <a href="https://anthscomputercave.com/tutorials/ifttt/using_ifttt_web_request_email.html">here</a>.

### Setting up event on IFTTT
These steps will show you how to create your own event on IFTTT:
1. In the drop down menu under your username, click "New Applet".
2. Click the blue "+this".
3. In the search field, type "Webhooks", and then click the result "Receive a web request".
4. Name your web event, I named mine "Sitemap_Notification".
5. Click "Create Trigger" and then click the blue "+that".
6. In the search field, type and select "Email", then click the result "Send me an email".
7. Name the subject for your email, I used "XML Sitemap Notification".
8. You can choose to create your own body, or you can copy and paste the format I have here: 
```
Sitemap Discrepancies:<br>
New Links:<br>
{{Value1}}<br><br>
Missing Links:<br>
{{Value2}}<br>
```
If choosing to create your own body, still use {{Value1}} and {{Value2}} as your variables.

9. Click "Finish"
10. Go to "Settings" under your username and make sure you have URL Shortening toggled off.

### Terminal commands
You should run these commands in your terminal in order to make sure everything is up to date and installed.  However, everything should be installed if you installed Miniconda.
```
sudo pip install requests
```
```
sudo apt-get install python-dev libffi-dev libssl-dev
```
```
sudo pip install --upgrade ndg-httpsclient
```

### Editing the code
You will need to go into the config.py file and change the variables.  All of the variables have comments next to them explaining what they are used for.

#### For the key variable:
In order to get your key, on IFTTT, you will need to go to My Applets -> Services -> Webhooks -> Settings -> URL: https://maker.ifttt.com/use/ThisIsYourKey

Only copy the area where I have labled ThisIsYourKey and paste it into the KEY variable in config.py
