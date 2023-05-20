## Pasos que utilizamos para configurar nuestro sistema (windows 10/11)
1. Revisar si los puertos:  3306, 3308, 5000, 5001, 5100, 5200, 5201, 5202, 5672, 8088, 15672  estan desocupados, de lo contrario se deberan cerrar las aplicaciones que utilicen esos puertos, o 
cambiar los puertos utilizados para ejecutar cada aplicacion.   
  1.1 Puerto 3306, 3308 Base de datos   
  1.2 Puerto 5000 Frontend   
  1.3 Puerto 5001 Collect   
  1.4 Puerto 5100 Publisher-Backend   
  1.5 Puerto 5200, 5201, 5202 Slaves  
  1.6 Puerto 5672, 15672 RabbitMQ   
  1.7 Puerto 8088 Nginx   
2. En caso de querer modificar aspectos de la aplicacion, en cada carpeta se encuentra un archivo de configuracion.   
3. Para modificar la cantidad de clientes a soportar con colas, se debe modificar la configuracion del archivo config de la carpeta Suscription-backend

