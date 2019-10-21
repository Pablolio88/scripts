$cred=Get-Credential| 
$Servs = Get-ADComputer -Filter '*' -Properties IPv4Address | FT DNSHostName -A
foreach($Serv in $Servs){
    Get-Service -DisplayName *snmp*  | Where-Object {$_.Status -EQ "Running"} 
}

$cred=Get-Credential
Get-ADComputer -Filter '*' -Properties IPv4Address |  DNSHostName -A | Write-Host "Polling server $_" Get-Service -DisplayName *snmp*  | Where-Object {$_.Status -EQ "Running"} 


$cred=Get-Credential
Get-ADComputer -Filter '*' -Properties Created | FT DNSHostName, Created #| Measure-Object -Line


$Computers = Get-ADComputer -SearchBase 'dc=syncplicity,dc=local' -Filter '*'
Foreach ($Computer in $Computers)
{
$Hostname = $Computer.Name
$ComputerInfo = (Get-Service -DisplayName *snmp* -ComputerName $Hostname)
Write-Host "Name: $Hostname"
Write-Host "$ComputerInfo"
#Write-Host "Model: $Model"
#Write-Host " "
#$Content = "$Hostname;$Manufacturer;$Model"
#Add-Content -Value $Content -Path "C:\PS\ServersInfo.txt"
}


$Computers = Get-ADComputer -SearchBase 'dc=syncplicity,dc=local' -Filter '*'
Foreach ($Computer in $Computers)
{
$Hostname = $Computer.Name
Write-Host "Name: $Hostname"
$snmp = Get-Service -DisplayName *snmp* -ComputerName $Hostname
if ($snmp) {
    Write-Host "SNMP service is running"
if (!$snmp) {
    Write-Host "SNMP service is not running"
    }
#Write-Host "$ComputerInfo"
#Write-Host "Model: $Model"
#Write-Host " "
#$Content = "$Hostname;$Manufacturer;$Model"
#Add-Content -Value $Content -Path "C:\PS\ServersInfo.txt"
}
Uninstall-WindowsFeature -Name $snmp -ComputerName $Hostname -Confirm -Credential $cred -IncludeManagementTools

##################################  WORKING ONE  ##############################################
$cred=Get-Credential -Credential pavel.kuprin
$Computers = Get-ADComputer -SearchBase 'dc=dc,dc=syncplicity,dc=com' -Filter * -Properties lastlogondate | ? {$_.lastlogondate -gt (Get-Date).AddDays(-365)}
Foreach ($Computer in $Computers)
{
$Hostname = $Computer.Name
$snmp = Get-Service -DisplayName 'SNMP Service'
if ($snmp.Status -eq 'Running') {
    Write-Host "Name: $Hostname"
    Write-Host "SNMP service is running"
    Uninstall-WindowsFeature -Name SNMP-Service -ComputerName $Hostname -Credential $cred -IncludeManagementTools -Remove
    }
else {
    Write-Host "Name: $Hostname"
    Write-Host "SNMP service is not running"
    }
}

Get-ADComputer -Identity "UNV-WEB-my-01" -Properties *