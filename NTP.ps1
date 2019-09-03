$Servs=Get-Content -Path C:\Users\pavel.kuprin\Serv.txt
$cred=Get-Credential
foreach($Serv in $Servs){
    Invoke-Command -ComputerName $Serv -ScriptBlock { w32tm /config /manualpeerlist:wdc-adc-01.dc.syncplicity.com /syncfromflags:manual } -credential $cred
    Invoke-Command -ComputerName $Serv -ScriptBlock { Stop-Service w32time } -credential $cred
    Invoke-Command -ComputerName $Serv -ScriptBlock { Start-Service w32time } -credential $cred 
}
