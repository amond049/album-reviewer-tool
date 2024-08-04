echo off 
python detector.py > temp.txt
set /p output=<temp.txt

if not %output% == false (
    :: Could not figure out how to accept multiple inputs because this does not seem to be working, instead delegating the input to the python file
    python uploadToTable.py %output%
) else (
    echo An album was not listened to!
)