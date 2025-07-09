# Python em docker 
Instruções para executar com segurança o container Docker com acesso ao servidor X do host hospedeiro.

## Permitindo qualquer container Doker acessar o X
~~~shell
$ xhost +local:docker
~~~

## Permitindo apenas usuário local acessar o X
No host, permita acesso ao servidor X apenas para o usuário local 'alexander':
~~~shell
$ xhost +SI:localuser:alexander 
~~~

## Construindo a imagem
Construa a imagem Docker:
~~~Shell
   docker build -t python-app-cursor .
~~~

## Rodando container
Execute o container com acesso ao servidor X:
~~~Shell
$ docker run -it --rm \
-e DISPLAY=$DISPLAY \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-v $HOME/.Xauthority:/root/.Xauthority \
--device /dev/uinput \
--privileged \
python-app-cursor
~~~

## Removendo permissões
Após o uso, remova a permissão concedida:
~~~shell
$ xhost -local:docker
$ xhost -SI:localuser:alexander
~~~