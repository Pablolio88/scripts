#!/bin/bash
echo -e "\e[1;31m This script will gather network stats based on traceroute, ping and iperf stats \e[0m"
echo Type host ip or URL
read pinghost
echo -e "\e[1;33mTest will run automaticly and put the output to the screen\e[0m"
echo -e "\e[1;33mDoing ping\e[0m"
ping -i 0.1 $pinghost -c 100 > ~/pingresult
tail -n 4 ~/pingresult
rm ~/pingresult
echo -e "\e[1;33mDoing traceroute. Using traceroute command.\e[0m"
trcpth=$(rpm -qa | grep iputils)
if [ -z "$trcpth" ]
then
echo You should install iputils
else
tracepath -n $pinghost
fi
echo -e "\e[1;33mPerforming network throughput tests. Using iperf3 command.\e[0m"
echo -e "\e[1;31mIperf3 package should be installed on the server and the client.\e[0m"
echo -e "\e[1;31mCommand 'iperf3 -s' should be entered on the server.\e[0m"
echo -e "\e[1;33mSkip this step if you do not have this package installed. Type yes or no\e[0m"

read yesno2
         if [ $yesno2 = "yes" ]
         then iperf3 -c $pinghost -w 65k
         else
         echo -e "\e[1;33m Network throughput tests will be skipped\e[0m"
         fi

echo -e "\e[32mAll tests are done\e[0m"
