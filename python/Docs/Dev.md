# Como desenvolver código para esse projeto

Pelo *docker-compose.yml* que usamos para criar a aplicação, está configurado um Volumes como *volumes: ./python:/app*. Isto significa que o diretório ./python que está rodando na sua máquina (aka. **HOST**) está mapeado bidirecionalmente no diretório *./app* do container - que é onde a aplicação está rodando. Isso significa que o seu ambiente de desenvolvimento e o container estão sincronizados, e você pode editar os arquivos pelo VSCode na sua máquina - por exemplo - e o Docker atualiza dentro do container automaticamente. 

Isso permite que você desenvolva como se estivesse rodando localmente, **mas note, a aplicação está rodando no container e portanto você tem que executar pelo JupyterLab no seu navegador.**

## Sugestão para Devs

Como sugestão, leia e crie arquivos/diretórios pelo VSCode, e edite somente pelo JupyterLab. Nada ~~quebra~~ se você fizer toda edição pelo VSCode ou JupyterLab, mas as vezes o Jupyter vai lançar uns warnings de *"arquivo editado, deseja salvar conteudo"* se você editar pelo VSCode algo que estiver aberto lá e eles são bem chatos. Dou a sugestão pois é o jeito mais ágil que achei de desenvolver. 

Editar arquivos pelo **HOST** que *NÃO* estejam abertos no Jupyter não lança nenhum warning.