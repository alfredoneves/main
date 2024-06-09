# varre host

param($net)

if(!$net){
    echo "Uso: $($myInvocation.InvocationName) [NETWORK]"
    echo "Exp: $($myInvocation.InvocationName) 192.168.0"
    exit
}

foreach($f in 1..254){
    $resp = ping -w 1 -n 1 "$net.$f" | Select-String "bytes=32"

    try{
        echo $($resp.Line.split(' ')[2] -replace ":","") 
    }catch{}
    
}
