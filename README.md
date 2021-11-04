# devops-netologyfirst modification
# Игнорируються каталоги .terraform  и их содержимое
**/.terraform/*

# все файлы с именами содержащие  .tfstate 
*.tfstate
*.tfstate.*

# Лог файлы
crash.log

# Файлы с именами содержашие: 
#
*.tfvars 
override.tf 
override.tf.json
*_override.tf
*_override.tf.json

# кроме файлов  !example_override.tf

# Игнорирують файлы
.terraformrc
terraform.rc
#
add new line
