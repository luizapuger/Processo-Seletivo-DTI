# Processo-Seletivo-DTI
 
Este projeto consiste em testes automatizados utilizando Python com Selenium pelo VSCode para verificar o comportamento do sistema de login em um site específico.

## Cenários de Teste

É recomendável executar os testes na ordem em que foram apresentados nos cenários de teste.

### Cenário 1: Login com Credenciais Inválidas (loginincorreto.py)

- **Dado que** o usuário esteja na página de login.
- **Quando** o usuário inserir um e-mail inválido ou uma senha inválida.
- **Então** a página exibirá uma mensagem de erro indicando que as credenciais fornecidas estão incorretas.

### Cenário 2: Login sem Informações (loginseminfo.py)

- **Dado que** o usuário esteja na página de login.
- **Quando** o usuário não inserir nada e apertar para logar.
- **Então** a página exibirá uma mensagem de erro indicando que é necessário inserir e-mail e senha.

### Cenário 3: Limite de Tentativas de Login (block.py)

- **Dado que** o usuário esteja na página de login.
- **Quando** o usuário tentar fazer login várias vezes com credenciais inválidas. (3x)
- **Então** o usuário será bloqueado e aparecerá uma mensagem falando para ele tentar novamente mais tarde.

### Cenário 4: Recuperação de Senha (forgot.py)

- **Dado que** o usuário esteja na página de login.
- **Quando** o usuário clicar no link "Esqueceu a senha?"/"Forgot your password?".
- **Então** o usuário será redirecionado para a página de recuperação de senha, onde poderá fornecer informações para redefinir sua senha.

## Contribuindo

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.
