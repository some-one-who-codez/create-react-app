import os

appName = input("What is your React app name ")
cmd = "npx create-react-app " + appName
cd = "cd " + appName
start = "npm start"
vsc = "code ."

os.system('cmd /c ' + cmd)
os.system('cmd /c ' + cd)
os.chdir(appName)
os.system('cmd /c ' + vsc)
os.system('cmd /c ' + start)

exit(0)
