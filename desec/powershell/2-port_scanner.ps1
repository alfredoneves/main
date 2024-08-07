param($ip)

if(!$ip){
    echo "Uso: $($myInvocation.InvocationName) [IP]"
    echo "Exp: $($myInvocation.InvocationName) 192.168.0.1"
    exit
}

$top_ports = 21,22,25,80,139,445,3306,3369,4444,8080

foreach($port in $top_ports){
    if(Test-NetConnection $ip -Port $port -WarningAction SilentlyContinue -InformationLevel Quiet){
        echo "Porta $port aberta"
    }
}
