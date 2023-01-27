# Git

Aqui estão todas as minhas anotações sobre o uso da tecnologia Git

## O que é Git

[Git](https://git-scm.com) é basicamente um sistema de controle de versões, foi desenvolvido por Linus Torvalds, tendo como objetivo inicial o desenvolvimento do Kernel Linux, porém foi adotado para vários outros projetos.

## O que é versionamento

O Git é muito usado para o controle de versões de um códico, ou seja, toda vez onde há uma mudança significativa a ser feita no projeto, é criada uma **branch** do app, dessa forma, o código novo é adcionado a esse braço secundário criado, caso alguma coisa dê errado, a versão estável do app é mantida segura e sem alterações, caso o texto adicionado funcione sem erros, o braço secundário pode ser "fundido" com o principal.

## O que é repositório e branch

Repositório pode ser visto como uma pasta onde seu projeto é armazenado, o repositório é dividido em branchs, que são esses braços clonados e manipulados sem interferir no código principal.
![branch](https://blog.4linux.com.br/wp-content/uploads/2019/02/Screenshot-from-2019-02-13-11-22-06.png)

## Comandos básicos do Git

O Git normalmente é manipulado por um terminal, onde se faz necessário o uso de alguns comandos para realizar as ações dentro do seu repositório

```
git commit
```

O comando **git commit** basicamente salva as alterações feitas no seu repositório local.

```
git push
```

O comando **git push** envia as alterações anteriormente salvas no repositório local, para o repositório remoto, como o GitHub ou GitLab.

```
git add
```

O comando **git add** adiciona pastas ou arquivos para serem rastreados pelo git, assim, todas as alterações vão ser detectadas salvas ao serem comitadas.

```
git clone
```

O comando **git clone** baixa algum repositório remoto ja existente para sua máquina, assim podendo ser editado localmente.

```
git pull
```

O comando **git pull** traz todas as alterações feitas no repositório para os seus arquivos locais.

```
git status
```

O comando **git status** te indica quais são os arquivos que sofreram alterações e ainda não foram comitados, ou seja, ainda não estão salvos no repositório local e não estão prontos para serem enviados ao reposiório remoto