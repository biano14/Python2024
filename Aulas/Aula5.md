# Aula sobre Git e Github

## Codigos adicionais

- codigo para mudar de Branch
  - `git checkout "nome-da-branch"`
- codigo para deletar Branch
  - `git branch -d "nome-da-branch"`
- codigo para ver log de Commit
  - `git log`
- codigo para configurar seu email e usuario
  - `git config --global user.name "nome-de-usuario"`
- codigo para configurar email
  - `git config --global user.email "nome-de-email"`
- codigo para dar merge
  - `git merge "nome-da-fonte"`
- codigo para log em arvore
  - `git log --graph`
- codigo para log em arvore resumido
  - `git log --pretty=format:"%h %s" --graph`

### Atualizações para Git lfs (Arquivos Grandes)

- codigo para a instalação do git lfs
  - `git lfs install`
- codigo para trackear extensões grandes
  - `git lfs track "*.extension"`
- codigo para add arquivo com configurações do git lfs
  - `git add .gitattributes`
