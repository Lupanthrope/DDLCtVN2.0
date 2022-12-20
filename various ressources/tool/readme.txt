Rpatool is a great tool to repack your rpyc into a single rpa archive. Link of the tool : https://github.com/Shizmob/rpatool

The ps1 script allows to repack all the files of a folder into a single archive of the name of your liking. Put both "rpatool" and "repackAll.ps1" into the target folder and use this command in a admin powershell prompt :

PowerShell -ExecutionPolicy RemoteSigned -file .\repackAll.ps1 -output name_of_your_archive.rpa