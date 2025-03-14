@echo off
echo Requesting Administrator Privileges...
powershell -Command "Start-Process cmd -ArgumentList '/c %~f0' -Verb RunAs" && exit

echo Installing Veronica AI...
python Veronica_Setup.py

echo Adding Veronica AI to Startup...
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v VeronicaAI /t REG_SZ /d "%CD%\veronica_online.bat" /f

echo Creating Desktop Shortcut...
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%USERPROFILE%\Desktop\Veronica_AI.lnk'); $s.TargetPath='%CD%\veronica_online.bat'; $s.Save()"

echo Installation Complete. Run 'veronica_online.bat' to start Veronica AI.
pause
