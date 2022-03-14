import os # needed to run terminals

# get details of app
appName = input("What is your React app name? ")
directory = input("Which directory do you wish to place it in? ") # eg 'C:\Users\YOUR_USERNAME\Documents\react'

directoryOfApp = directory + '\\' + appName # eg 'C:\Users\YOUR_USERNAME\Documents\react\YOUR_APP_NAME'
createApp = "npx create-react-app " + appName # creates app
start = "npm start" # start react app
vsc = "code ." # opens VSX

os.chdir(directory)

# create app
os.system('cmd /c ' + createApp)

# navigate to app dir
os.chdir(directoryOfApp)

# open VSC and start react app
os.system('cmd /c ' + vsc)
os.system('cmd /c ' + start)

exit(0)
