# UF-API
Powered by Adal

![Build Status](https://d31dn7nfpuwjnm.cloudfront.net/images/valoraciones/0023/7113/UF.png?1463732419)

Esta api permite obtener la unidad de fomento registrada por el SII para una fecha específica, además permite listar el valor de unidades de fomento registradas por fechas para un año.

## Características

- Desarrollada con Python 3.9 y FastAPI
- Uso de Docker
- Testing con Pytest

## Correr el proyecto localmente
Debes tener docker y docker compose instalados en tu máquina. Abre tu consola de preferencia en el directorio que quieras tener el proyecto, en este ejemplo será el directorio Downloads.

```sh
cd Downloads
git clone https://github.com/Adal1013/uf-api
cd uf-api
```

Una vez dentro de la carpeta del proyecto, ejecutamos lo siguientes comandos para correr el proyecto:

```sh
docker-compose build
docker-compose up
```

Ya con esto tendrás el proyecto corriendo en tu máquina local en el puerto :8000. Puedes ingresar a la ruta http://localhost:8000/docs donde tendrás acceso a la documentación del proyecto a través de Swagger UI, en esta interfaz también puedes probar los endpoints de la API . Si deseas ejecutar las pruebas con pytest lo puedes hacer desde la consola en el directorio raíz del proyecto (uf-api) con el siguiente comando:

```sh
docker-compose exec -it uf-api python -m pytest
```

## Nota

Debes verificar que el archivo .env esté creado y con el valor de la URL que corresponde, sino está creado el archivo debes crearlo en la carpeta app con el valor de la URL para la variable SII_UF_URL.
