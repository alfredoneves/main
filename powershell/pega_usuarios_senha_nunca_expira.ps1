# lista os usuários do AD cuja senha nunca expira
Get-ADUser -Filter * -Property Name, PasswordNeverExpires | Where-Object { $_.PasswordNeverExpires -eq $true } | Select-Object Name
