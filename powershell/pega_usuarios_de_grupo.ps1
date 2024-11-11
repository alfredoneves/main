# coloque o nome do GR para encontrar todos os usuários do AD que estão inclusos nele
Get-ADGroupMember -Identity "GR_AQUI" -Recursive | Where-Object { $_.objectClass -eq 'user' } | Get-ADUser | Select-Object Name, SamAccountName
