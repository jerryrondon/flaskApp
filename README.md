# flaskApp
AntonPutra-DockerComposeTutorial


## App

Para ejecutar la aplicación:
```bash
cd flask
flask --app app run
```

Luego ir a un navegador web e ir a `localhost:5000` o ejecutar:
```bash
curl 127.0.0.1:5000/about
```

# Docker
Para crear la imagen:
```bash
cd flask
docker build --tag jerryrondon/flaskapp:0.1.0 .
```

Para crear el contenedor:
```bash
docker container run --name flaskApp --publish 8080:8080 -e APP_VERSION=0.2.1 jerryrondon/flaskapp:0.1.0
```
Para verificar la ejecución:
```bash
curl 127.0.0.1:8080/about
```
Respuesta:
```bash
$ curl 127.0.0.1:8080/about
{"version":"0.2.1"}
```
