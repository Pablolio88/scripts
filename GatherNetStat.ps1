Write "This script will gather network stats based on traceroute, ping and iperf stats"
$pinghost = Read-Host -Prompt "Enter host ip or URL: "
Write "Doing ping"
ping -n 10 -w 100 $pinghost
Write "Doing traceroute"
tracert -d $pinghost
