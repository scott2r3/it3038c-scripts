function getIP{(Get-NetIPAddress).IPv4Address | Select-String "192*"}
$IP = getIP
function userGet{get-localuser | select-string "admin"}
$USERCURRENT = userGet
$HOSTNAME = hostname
$VERSION = $HOST.Version.Major
$DATE = Get-Date

function bodyy{
"This machines IP is $IP. User is $USERCURRENT. Hostname is $HOSTNAME. Powershell Version $VERSION. Today's Date is $DATE"
}
$BODY = bodyy

Send-MailMessage -To "reedws@ucmail.uc.edu" -From "scotttester2307@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)