# caminho do arquivo
$filePath = "C:\Users\CPF168456527\Desktop\matriculas.txt"

# verificar se o arquivo existe
if(Test-Path $filePath){
	$usernames = Get-Content $filePath
	
	foreach($username in $usernames){	# iterar no loop para cada usuário (um por linha)
		try{
			$userPrincipalName = (Get-ADUser -Identity $username.Trim() -Properties UserPrincipalName).UserPrincipalName
			Write-Output "$userPrincipalName" >> emails.txt
		} catch{
			Write-Output "VERIFICAR XXXXXXXXXXXXX" >> emails.txt
		}
	}
} else {
	Write-Output "Arquivo $filePath inexistente"
}
