@ECHO OFF

REM Start copy Anaconda config to all current and future users
REM -------------------------------------------------

IF EXIST "C:\Users\" PUSHD "C:\Users\"

FOR /F "tokens=*" %%G in ('dir /a:d-s-h /b') do (
	XCOPY "%~dp0config_anaconda\*" "%%G\AppData\Roaming\" /Y /R /Q /S
)
POPD

XCOPY "%~dp0config_anaconda\*" "C:\Users\default\Appdata\Roaming\" /Y /R /Q /S

REM Start copy Spyder config to all current and future users
REM -------------------------------------------------

IF EXIST "C:\Users\" PUSHD "C:\Users\"

FOR /F "tokens=*" %%G in ('dir /a:d-s-h /b') do (
	XCOPY "%~dp0config_spyder\*" "%%G\" /Y /R /Q /S
)
POPD

XCOPY "%~dp0config_spyder\*" "C:\Users\default\" /Y /R /Q /S

REM Start copy Juputer config to all current and future users
REM -------------------------------------------------

IF EXIST "C:\Users\" PUSHD "C:\Users\"

FOR /F "tokens=*" %%G in ('dir /a:d-s-h /b') do (
	XCOPY "%~dp0config_jupyter\*" "%%G\" /Y /R /Q /S
)
POPD

XCOPY "%~dp0config_jupyter\*" "C:\Users\default\" /Y /R /Q /S