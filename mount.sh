clear
Local=`hostname | awk -F\- '{ print $2 }'`

case $Local in
    'sp')
        Dest=("mr" "b8:27:eb:b5:92:d8" "A_MR")	;;
    'mr')
        Dest=("sp" "dc:a6:32:1c:7e:8b" "A_SP")	;;
    *)
        Dest=""	;;
esac
Gw=`ip route | grep default | awk '{ print $3 }' | uniq | awk -F\. '{ print $1"."$2"."$3".0/24"}'`
IP=`arp-scan $Gw | grep ${Dest[1]} | grep DUP -v | awk '{ print $1 }'`
Live=`ping $IP -c2 | grep ^2 | awk -F\, '{ print $2 }' | awk '{ print $1}'`
Mount=`df -h | grep "${Dest[2]}" | awk -F\: '{ print $1 }'`

#-------------------------------------------------------------------------------------------------------
echo "
Local:	$Local
Dest:	${Dest[0]} - ${Dest[1]}
GW:	$Gw
IP:	$IP
Live:	$Live
Mount:	$Mount
"
if [ "$Live" == "2" ] && [ "$Mount" != "$IP" ]
then
    mount -t nfs $IP:/ /${Dest[2]}/
else
    echo -e "\n\nJa montado"
fi


