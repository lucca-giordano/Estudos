# Docker

## O que é Docker?

Docker é uma plataforma de código aberto que facilita a criação, implantação e execução de aplicativos em contêineres. Os contêineres permitem que um desenvolvedor empacote um aplicativo com todas as partes necessárias, como bibliotecas e outras dependências, e envie como um único pacote. Ao fazer isso, o desenvolvedor garante que o aplicativo será executado em qualquer outra máquina, independentemente de quaisquer configurações personalizadas que a máquina possa ter que possam diferir da máquina usada para escrever e testar o código.

## O que é um contêiner?

Um contêiner é uma unidade padrão de software que empacota o código e todas as suas dependências para que o aplicativo seja executado de forma rápida e confiável de um ambiente de computação para outro. Um contêiner inclui tudo o que é necessário para executar um aplicativo - o código, um tempo de execução, bibliotecas, variáveis de ambiente e arquivos de configuração.

## Qual a diferença entre uma máquina virtual e um contêiner?

Uma máquina virtual (VM) é um ambiente de computação em software que emula um computador físico. As máquinas virtuais são baseadas em computadores físicos e fornecem funcionalidades de computação de um computador físico. Um contêiner é uma unidade padrão de software que empacota o código e todas as suas dependências para que o aplicativo seja executado de forma rápida e confiável de um ambiente de computação para outro.

## O que é Docker Hub?

Docker Hub é um serviço baseado em nuvem que permite a você compartilhar imagens de contêineres publicamente ou privadamente e usar imagens compartilhadas por outras pessoas. Ele fornece uma maneira centralizada para armazenar e gerenciar imagens de contêineres.

## Comandos Docker

- `docker run`: Executa um comando em um novo contêiner, caso o contêiner não exista, ele é baixado do Docker Hub.

- `docker pull`: Baixa uma imagem do Docker Hub.

- `docker images`: Lista as imagens disponíveis no host.

- `docker ps`: Lista os contêineres em execução.

- `docker ps -a`: Lista todos os contêineres, inclusive os que estão parados.

- `docker stop`: Para um contêiner em execução.

- `docker start`: Inicia um contêiner parado.

- `docker rm`: Remove um contêiner.

- `docker rmi`: Remove uma imagem.
