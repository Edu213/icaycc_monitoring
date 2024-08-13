## Monitorio del estado de un servidor.

Por el momento el repositorio esta dedicado a pruebas de tecnologias como glances, Apptainer, Stress-ng, Victoria-Metrcis y Grafana.

## Autores ✒️

- **Alan Ortega** - _Trabajo Inicial_ - [Edu213](https://github.com/Edu213/)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto.

## Configuración e instalación

Para la configuración e instalación de Glances, Victoria-Metrics y Grafana se utiliza apptainer para tener cada aplicación en su propio contenedor.

### Apptainer

En este caso se hace uno de Debian como SO de trabajo, por lo que la siguiente guía de instalación es para dicho SO. Si tienes alguna distribución diferente sigue los pasos descritos en la [documentación](https://github.com/apptainer/apptainer/blob/main/INSTALL.md).

#### Instalar dependencias del sistema

Para sistemas basados en Debian:

> # Asegurate de tener los repositorios actualizados
>
> sudo apt-get install update
>
> # Instalación de los paquetes de Debian
>
> sudo apt-get install -y \
>  build-essential \
>  libseccomp-dev \
>  pkg-config \
>  uidmap \
>  squashfs-tools \
>  fakeroot \
>  cryptsetup \
>  tzdata \
>  dh-apparmor \
>  curl wget git

#### Instalar Go

Debido a que apptainer se encuentra desarrollado en Go, se puede requerir una versión más reciente de Go de la disponible en los repositorios de tu distribución. Por lo que es recomendable descargar la versión más reciente de Go.

**NOTA**: Si estas actualizando tu versión de Go, asegurate de remover /usr/local/go antes de reinstalarlo de nuevo.

```
export GOVERSION=1.20.10 OS=linux ARCH=amd64  # cambia esto segun la version que gustes
wget -O /tmp/go${GOVERSION}.${OS}-${ARCH}.tar.gz \
https://dl.google.com/go/go${GOVERSION}.${OS}-${ARCH}.tar.gz
sudo tar -C /usr/local -xzf /tmp/go${GOVERSION}.${OS}-${ARCH}.tar.gz
```

Finalmente agrega /usr/local/go/bin al la variable de entorno PATH.
