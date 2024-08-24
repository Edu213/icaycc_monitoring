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

#### Asegurate de tener los repositorios actualizados

```bash
sudo apt-get install update
```

#### Instalación de los paquetes de Debian

```bash
sudo apt-get install -y \
build-essential \
libseccomp-dev \
pkg-config \
uidmap \
squashfs-tools \
fakeroot \
cryptsetup \
tzdata \
dh-apparmor \
curl wget git
```

#### Instalar Go

Debido a que apptainer se encuentra desarrollado en Go, se puede requerir una versión más reciente de Go de la disponible en los repositorios de tu distribución. Por lo que es recomendable descargar la versión más reciente de Go.

**NOTA**: Si estas actualizando tu versión de Go, asegurate de remover /usr/local/go antes de reinstalarlo de nuevo.

```bash
export GOVERSION=1.20.10 OS=linux ARCH=amd64  # cambia esto según la version que gustes
wget -O /tmp/go${GOVERSION}.${OS}-${ARCH}.tar.gz \
https://dl.google.com/go/go${GOVERSION}.${OS}-${ARCH}.tar.gz
sudo tar -C /usr/local -xzf /tmp/go${GOVERSION}.${OS}-${ARCH}.tar.gz
```

Finalmente agrega /usr/local/go/bin al la variable de entorno PATH.

```bash
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc
```

#### Clona el repositorio

Clona el repositorio con ayuda de git, en la dirección que tu quieras:

```bash
git clone https://github.com/apptainer/apptainer.git
cd apptainer
```

De forma predeterminada, su repositorio clon estará en la rama principal, que es donde ocurre el desarrollo de Apptainer. Para crear una versión específica de Apptainer, consulte una [etiqueta de lanzamiento](https://github.com/apptainer/apptainer/tags) antes de compilar, por ejemplo:

```bash
git checkout v1.3.3
```

#### Compilar apptainer

Como paso final solo queda compilar apptainer para que la instalación quedé finalizada:

```bash
./mconfig
cd $(/bin/pwd)/builddir
make
sudo make install
```

Para verificar que apptainer se ha instalado correctamente ejecuta el comando:

```bash
apptainer --version
```

## Contenedores en Apptainer

Una vez instalado apptainer debemos generar nuestros contenedores para nuestros servicios. Si se quiere entender de mejor manera el funcionamiento de Apptainer, así como sus comandos y opciones disponibles se recomienda leer la [documentación](https://apptainer.org/docs/user/latest/)

### Glances

Para crear el contendor que correrá glances, descarga el [archivo de definición](https://github.com/Edu213/icaycc_monitoring/tree/main/definitionFiles) de glances o puedes clonar el repositorio completo si gustas:

```bash
git clone https://github.com/Edu213/icaycc_monitoring.git
cd icaycc_monitoring
```

Una vez que tengas el archivn de definición, para crear nuestro contenedor en un directorio, ejecuta el siguiente comando:

```bash
apptainer build --sandbox GLANCES/ [Definition_file_path]
```

**NOTA**: El contenedor en directorio lo puedes generar en caulquier directorio que gustes, en el comando de arriba se crea en el directorio de trabajo. Si quisieras mandarlo al home de tu usuario podríeas usar /home/usuario/GLANCES/

Para ejecutar el contenedor se ejecuta el siguiente comando:

```bash
apptainer run GLANCES/ --export prometheus
```

**NOTA**: La banadera --export prometheus, nos permite exportar las métricas en un formato de prometheus.

### Victoria metrics

Puedes obtener el archivo de [defición de ejemplo]() para crear el contenedor en directorio:

```bash
apptainer build --sandbox VICTORIA/ [Definition_file_path]
```

Para ejecutar el contenedor y levantar nuestro servicio de Victoria metrics ejecuta el comando:

```bash
apptainer run -w VICTORIA/ -promscrape.config=victoria.yaml -httpListenAddr=":17002
```

**NOTA**: En este caso es necesario que tengas el archivo de [configuración yaml](https://github.com/Edu213/icaycc_monitoring/tree/main/configFiles). Además de colocar el puerto al que nuestro servicio se encontrará escuchando.

### Grafana

Obten el archivo de configuración. Una vez que ya tienes el archivo de configuración ejecuta el siguiente comando para construir nuestro contenedor en directorio:

```bash
apptianer buil --sandbox GRAFANA/ [Definition_file_path]
```

Para levantar el contenedor de grafana, ejecuta el comando:

```bash
apptainer instance run -w GRAFANA/ grafana
```

## Links de utilidad

[Documentación Victoria Metrics](https://docs.victoriametrics.com/)
[Documentación Glances](https://glances.readthedocs.io/en/develop/#)
[Documentación Grafana](https://grafana.com/docs/grafana/latest/)

[Configuración Victoria-Grafana](https://docs.victoriametrics.com/#prometheus-setup)
[Congifuracíon data source de Grafana](https://grafana.com/docs/grafana/latest/datasources/prometheus/configure-prometheus-data-source/)
[Creación de un dashboard en Grafana](https://grafana.com/docs/grafana/latest/getting-started/build-first-dashboard/)
[Lenguaje PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/)
