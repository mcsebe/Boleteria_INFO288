## Pasos que utilizamos para configurar nuestro sistema (windows 10/11)
1. Revisar si los puertos:  3306, 5001, 5100, 5200, 5201, 5202, 5672, 8088  estan desocupados, de lo contrario se deberan cerrar las aplicaciones que utilicen esos puertos, o 
cambiar los puertos utilizados para ejecutar cada aplicacion.   
  1.1 Puerto 3306 MariaDB   
  1.2 Puerto 5001 Collect   
  1.3 Puerto 5100 Publisher-Backend   
  1.4 Puerto 5200, 5201, 5202 Slaves  
  1.5 Puerto 5672 RabbitMQ   
  1.5 Puerto 8088 Nginx   
2. Deben crearse credenciales en RabbitMQ para poder 
