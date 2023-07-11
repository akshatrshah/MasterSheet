@echo off
echo Starting the ping command...
start cmd /c "java -classpath D:\hackk\feed-play-1.0.jar hackathon.player.Main D:\hackk\dataset.csv 8080"

REM Wait for 20 seconds
timeout /t 20

REM Terminate the command (in this case, we are terminating the 'ping' command)
taskkill /f /im ping.exe

echo Command terminated after 20 seconds.
pause