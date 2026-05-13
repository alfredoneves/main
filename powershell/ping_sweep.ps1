param($ip_range)

if(!$ip_range){
    echo "Uso: $($myInvocation.InvocationName) [IP_RANGE]"
    echo "Exp: $($myInvocation.InvocationName) 192.168.0.0/24"
    exit
}

$network, $cidr = $ip_range.Split('/')

$ipBytes = [System.Net.IPAddress]::Parse($network).GetAddressBytes()
[array]::Reverse($ipBytes)

$ipInt = [BitConverter]::ToUInt32($ipBytes, 0)

$mask = ([uint32]4294967295) -shl (32 - [int]$cidr)

$networkInt = $ipInt -band $mask
$broadcastInt = $networkInt -bor (-bnot $mask)

$ips = @()

for($i = $networkInt + 1; $i -lt $broadcastInt; $i++){

    $bytes = [BitConverter]::GetBytes([uint32]$i)
    [array]::Reverse($bytes)

    $ip = ([System.Net.IPAddress]::new($bytes)).ToString()

    $ips += $ip
}

# Número máximo de jobs simultâneos
$maxJobs = 20

foreach($ip in $ips){

    # Limita quantidade de jobs simultâneos
    while((Get-Job -State Running).Count -ge $maxJobs){
        Start-Sleep -Milliseconds 100
    }

    Start-Job -ArgumentList $ip -ScriptBlock {

        param($ip)

        $result = Test-Connection -ComputerName $ip -Count 1 -Quiet -ErrorAction SilentlyContinue

        if($result){
            echo $ip
        }

    } | Out-Null
}

# Aguarda todos os jobs finalizarem
Get-Job | Wait-Job | Out-Null

# Exibe resultados
Get-Job | Receive-Job

# Remove jobs da memória
Get-Job | Remove-Job
