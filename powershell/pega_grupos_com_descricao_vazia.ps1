# mostra na tela todos os grupos do AD que estão com o campo de descrição vazio
Get-ADGroup -Filter {-not (description -like "*")} | Select-Object -Property Name
