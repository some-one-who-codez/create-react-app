import os # needed to run terminals

# get details of app
appName = input("What is your React app name? ")
directory = input("Which directory do you wish to place it in? ") # eg 'C:\Users\YOUR_USERNAME\Documents\react'

directoryOfApp = directory + '/' + appName 
use_vite = str(input("Do you want to use vite? (y/N) ")).lower()
use_tailwind = str(input("Do you want to use tailwind? (y/N) ")).lower()
use_typescript = str(input("Do you want to use typescript? (y/N) ")).lower()

createApp = ""
start = ""

if use_vite == "yes" or use_vite == 'y':
    if(use_typescript == "yes" or use_typescript == 'y'):
       createApp = "npm create vite@latest " + appName + " -- --template react-ts"  # creates app
       start = "npm run dev" # start react app 
    else:
        createApp = "npm create vite@latest " + appName + " -- --template react"  # creates app
        start = "npm run dev" # start react app
else:
    if(use_typescript == "yes" or use_typescript == 'y'):
        reateApp = "npx create-react-app " + appName + " --template typescript" # creates app
        start = "npm start" # start react app
    else: 
        createApp = "npx create-react-app " + appName # creates app
        start = "npm start" # start react app

vsc = "code ." # opens VSC

os.chdir(directory)

# create app
os.system(createApp)

# navigate to app dir
os.chdir(directoryOfApp)

# use tailwind
if use_tailwind == 'yes' or use_tailwind == 'y':
    install = 'npm install -D tailwindcss postcss autoprefixer'
    init = 'npx tailwindcss init -p'
    os.system(install)
    os.system(init)

# open VSC and start react app
os.system(vsc)
os.system(start)

exit(0)
