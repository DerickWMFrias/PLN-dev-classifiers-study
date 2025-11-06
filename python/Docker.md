# Tutorial: Como rodar esta aplicação

Aqui você encontra um guia de **como rodar os modelos desta aplicação utilizando o Docker e JupyterLab**. 

Para explicações/orientações de como essa *stack* funciona e como você pode desenvolver código para ela, referencie-se pelas instruções neste [*README*](../README.md).


## Como editar a Dockerfile.example

Neste diretório você vai encontrar um arquivo chamado Dockerfile.example. Você deve renomear o arquivo para Dockerfile, antes de rodar *docker compose up*. Se você deseja rodar scripts geradores de embeddings (como Jiina, BAAI, Gemma), você ainda precisará de editar o conteúdo da Dockerfile - descomentando alguns pacotes python p/ fazer com que sejam instalados. Você pode ler mais sobre em comentários dentro da própria Dockerfile.


## Como rodar pela Docker CLI

Esta aplicação utiliza Docker para criar o ambiente de processamento. 

Podemos usar a Docker CLI - que nada mais são que os comandos Docker que podem rodar na linha de comando - para rodar a aplicação.

Primeiro você precisa criar as imagens e containers do Docker. *Não se esqueça primeiro de instalar o Docker e de rodar o Docker Deamon* (Basta abrir o Docker Desktop que ele já inicia).

Abra sua CLI de preferência, e use *cd* até o diretório "/python" desta aplicação. Para assegurar-se, dê *ls* e procure pelo arquivo *docker-compose-example.yml* que está no diretório.

Então, renomeie *docker-compose-example.yml* para *docker-compose.yml*. Aproveite também para renomear *.gitignore.example* para *.gitignore* se pretende desenvolver.

Agora você está pronto para gerar a imagens e containeres e rodar sua aplicação. Aqui temos duas maneiras:

1. Rode *docker compose up*. Esse comando é usado para criar e rodar o container da aplicação. Se a imagem não estiver criada ainda, o Docker a cria automaticamente pois o container depende dela. 
2. Rode *docker compose build* e depois *docker compose up*. Build serve para criar a imagem, e Up para subir o container.

Os *devopeiros* dizem que o método 2 é boa prática.

Por fim, depois que o container subir, procure na sua CLI por um trecho como:

```
- pythonapp-1  | [I 2025-10-04 08:39:25.548 ServerApp] Jupyter Server 2.17.0 is running at:

- pythonapp-1  | [I 2025-10-04 08:39:25.548 ServerApp]     http://127.0.0.1:8888/lab?token=68ffe11baa5bc7e98bbcfbecbc8509fe0c64a783d206eb17

- pythonapp-1  | [I 2025-10-04 08:39:25.548 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
``` 

Esse endereço - *http://127.0.0.1:8888/lab?token=68ffe11baa5bc7e98bbcfbecbc8509fe0c64a783d206eb17* - é por onde você acessa o JupyterLab. **O token é recriado cada vez que você faz compose down/up**, então você tem que sempre copiar o endereço quando subir o container. Basta por fim acessar pelo seu navegador e a interface do JupyerLab abrirá, e você pode rodar os notebooks como um ambiente Jupyter comum.


## Dicas Docker

- *docker compose up -d* não funciona para essa aplicação, porque rodar no modo detached não vai permitir que você pegue o link do JupyterLab. Você precisa lockar um terminal para rodar a aplicação. 
- Para verificar se o container esta rodando, dê *docker ps* e procure por algum container com nome como *pythonapp-1*.
- Não esqueça de dar *docker compose down* no container ao terminar de usar.
