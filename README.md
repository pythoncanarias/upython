# upython
## Instalación

Para poder instalar MicroPython, descargaremos el firmware de la [Página oficial](http://micropython.org/download#esp8266) (Descargar el firmware para el chip correspondiente al ESP8266). Una vez descargado vamos a instalar las herramientas necesarias para flashear el chip con el firmware de MicroPython.


### Linux

Utilizando la herramienta _pip_ instalamos la herramienta _esptool_.

```bash
$ pip install esptool
```

Una vez instalado vamos a borrar la memoria flash del chip.

```bash

$ esptool.py --port /dev/ttyUSB0 erase_flash
```

Donde _/dev/ttyUSB0_ es el puerto serie donde se encuentre conectada la placa.

Una vez hecho esto vamos a pasar a flashear el firmware en la placa.

```bash
$ esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.9.2.bin
```

Donde tenemos que poner el puerto donde esta conectado la velocidad en baudios (en algunas placas puede haber problemas de comunicación si la velocidad es muy alta; recomendamos poner 115200 baudios). Además de poner el nombre del fichero del firmware.

### MacOs

En MacOs la operación es la misma; sin embargo es necesario instalar los drivers del chip de comunicación USB CH340/CH341. Los cuales podemos descargar [aquí](http://www.mblock.cc/docs/run-makeblock-ch340-ch341-on-mac-os-sierra/).

Una vez instalado ya podremos ver el puerto serie en nuestro sistema.

El resto de pasos, se realizan de igual forma que para Linux.

### Windows

Para windows también debemos instalar los drivers CH340/CH341; que podemos encontrar en la web del [fabricante](http://www.wch.cn/download/CH341SER_EXE.html).

## Herramientas de terminal

### Linux

* picocom
* minicom

#### Usando *picocom*

```bash
picocom /dev/ttyUSB0 -b 115200
```
* <kbd>Control</kbd>-<kbd>a</kbd> <kbd>Control</kbd>-<kbd>x</kbd> SALIR
* <kbd>Control</kbd>-<kbd>a</kbd> <kbd>Control</kbd>-<kbd>c</kbd> LOCAL ECHO
* <kbd>Control</kbd>-<kbd>d</kbd> NODEMCU SOFT REBOOT



### MacOS

Para conectarnos a la placa, usaremos _coolTerm_.

### CoolTerm

Para descargar CoolTerm Puede hacerse desde el siguiente [enlace](http://freeware.the-meiers.org/CoolTermMac.zip)

Una vez descargado e instalado, se configurará el puerto a utilizar; pulsando en el botón _Options_.

![opcionesCoolTerm](imagenes/optioncoolTerm.png)

Una vez configurado el puerto (con el que nos aparece en nuestro MAC) y configurado el baudrate a _115200_. Pulsaremos OK y al botón _connect_. Apareciendo el promt de Python.

![coolTerm](imagenes/coolTerm.png)
### Windows


## Pinout del NodeMCU

![alt text](https://docs.bsfrance.fr/documentation/10663_NODEMCU_V3_CH340/Pinout.png "Esquema de pines para la NodeMCU")
