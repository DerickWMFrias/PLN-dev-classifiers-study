Para informações de desenvolvimento e implementação deste projeto, leia o README que está no diretório /python. (Esta por escrever ainda)


# Tutorial: Como rodar esta aplicação

## Pela Docker CLI
Esta aplicação utiliza Docker para criar o ambiente de processamento. Podemos usar a Docker CLI - que nada mais são que os comandos Docker que podem rodar na linha de comando - para iniciar Imagens e Containeres e rodar a aplicação.

Primeiro você precisa criar as Imagens e Containers. Para isso, não se esqueça de instalar o Docker e de rodar o Docker Deamon (Basta abrir o Docker Desktop que ele já inicia).

Abra sua CLI de preferência, e use *cd* até o diretório "/python" desta aplicação. Para assegurar-se, dê *ls* e procure pelo arquivo *docker-compose-example.yml* que está no diretório.

Então, renomeie *docker-compose-example.yml* para *docker-compose.yml*. Neste momento, aproveite também para renomear *.gitignore.example* para *.gitignore*.

Agora você está pronto para gerar a Imagem e o Container que irá rodar sua aplicação. Tem duas maneiras:

1. Rode *docker compose up*. Esse comando é usado para criar e rodar o container da aplicação. Se a Imagem não estiver criada ainda, o Docker a cria automaticamente pois o container depende dela.
2. Rode *docker compose build* e depois *docker compose up*. Build serve para criar a Imagem, e Up para subir o container.

Os devopeiros dizem que o método 2 é boa prática.

Por fim, depois que o container subir, procure na sua CLI por um trecho como:

- pythonapp-1  | [I 2025-10-04 08:39:25.548 ServerApp] Jupyter Server 2.17.0 is running at:

- pythonapp-1  | [I 2025-10-04 08:39:25.548 ServerApp]     http://127.0.0.1:8888/lab?token=68ffe11baa5bc7e98bbcfbecbc8509fe0c64a783d206eb17

- pythonapp-1  | [I 2025-10-04 08:39:25.548 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation). 

Esse endereço *http://127.0.0.1:8888/lab?token=68ffe11baa5bc7e98bbcfbecbc8509fe0c64a783d206eb17* é por onde você acessa o JupyterLab. O token é recriado cada vez que você faz compose down/up, então você tem que sempre copiar o endereço quando subir o container. Basta por fim acessar pelo seu navegador e a interface do JupyerLab abrirá, e você pode rodar os notebooks como um ambiente Jupyter comum.

### Como desenvolver código/rodar os modelos

Pelo *docker-compose.yml* que usamos para criar a aplicação, está configurado um Volumes como *volumes: ./python:/app*. Isto significa que o diretório ./python que está rodando na sua máquina (aka. HOST) está mapeado bidirecionalmente no diretório ./app do container, que é onde a aplicação está rodando. Isso significa que o seu ambiente de desenvolvimento e o container estão sincronizados, e você pode editar os arquivos pelo VSCode na sua máquina - por exemplo - e o Docker atualiza dentro do container automaticamente. 

Isso permite que você desenvolva como se estivesse rodando localmente, mas lembre, a aplicação está rodando no container e portanto você tem que executar pelo JupyterLab no seu navegador.

Como sugestão, leia e crie arquivos/diretórios pelo VSCode, e edite somente pelo JupyterLab. Nada ~~quebra~~ se você fizer toda edição pelo VSCode ou JupyterLab, mas as vezes o Jupyter vai lançar uns warnings de "arquivo editado, deseja salvar conteudo" se você editar pelo VSCode algo que estiver aberto lá e eles são chatos. Dou a sugestão pois é o jeito mais ágil que achei de desenvolver.

### Dicas

- *docker compose up -d* não funciona para essa aplicação, porque rodar no modo detached não vai permitir que você pegue o link do JupyterLab. Você precisa lockar um terminal para rodar a aplicação. 
- Para verificar se o container esta rodando, dê *docker ps* e procure por algum container com nome como *pythonapp-1*.
- Não esqueça de dar *docker compose down* no container ao terminar de usar.

  
## Pelo Docker Desktop
É possível fazer todos esses processos pela GUI do Docker Desktop, mas não é algo que estou acostumado a fazer, então não sou capaz de orientar nisso.
