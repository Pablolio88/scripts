$Servs= Get-Content -Path C:\Users\pavel.kuprin\Serv.txt
$cred=Get-Credential
foreach ($Serv in $Servs) {
    $sess = New-PSSession -Credential $cred -ComputerName $Serv
    Enter-PSSession $sess
    w32tm /config /manualpeerlist:wdc-adc-01.dc.syncplicity.com /syncfromflags:manual 
    Stop-Service w32time
    Start-Service w32time
    Exit-PSSession
    Remove-PSSession $sess
}
