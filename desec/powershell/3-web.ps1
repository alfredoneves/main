$r = Invoke-WebRequest -uri "http://www.businesscorp.com.br"
echo "r.statuscode = $($r.statuscode)"
echo "--------------------------"
echo "r.headers:"
echo $r.headers
echo "--------------------------"
echo "r.links.href:"
echo $r.links.href