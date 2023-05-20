## Pasos que utilizamos para configurar nuestro sistema (windows 10/11)
Revisar si los puertos:  3306, 3308, 5000, 5001, 5100, 5200, 5201, 5202, 5672, 8088, 15672  estan desocupados, de lo contrario se deberan cerrar las aplicaciones que utilicen esos puertos, o 
cambiar los puertos utilizados para ejecutar cada aplicacion.   
  1 Puerto 3306, 3308 Base de datos     
  2 Puerto 5000 Frontend     
  3 Puerto 5001 Collect     
  4 Puerto 5100 Publisher-Backend     
  5 Puerto 5200, 5201, 5202 Slaves    
  6 Puerto 5672, 15672 RabbitMQ     
  7 Puerto 8088 Nginx   
  
En caso de querer modificar configuraciones de la aplicacion, se debe acceder a los siguientes archivos:  
   1 Para cambiar la configuración de la conexión a la base de datos "boletería", se debe cambiar en el archivo Cluster1/Backend/config/config.json  
   2 Para cambiar la configuración de la conexión a la base de datos "token", se deben cambiar los archivos:  
      - Cluster1/Backend/config/config.json  
      - Cluster2/Suscription-Backend/config/config.json  
      - Cluster3/GarbageCollector/config/config.json  
      - Cluster3/token_backend/config/config.json  por cada Slave añadido.  
   3 Para añadir nuevas colas primero se debe añadir el concierto a la base de dato con su respectiva cola. Luego se debe modificar:  
      - Cluster2/Publisher-Backend/config/config.json  
      - Cluster2/Suscription-Backend/config/config.json  
   4 Para añadir réplicas del componente token_backend:
      4.1 Añadir el archivo de configuración correspondiente (ejemplo: config3.json).  
      4.2 Modificar el archivo Cluster3/nginx.conf, añadiendo la ruta del slave en la sección "upstream backend".  
      4.3 Añadir la información del slave a Cluster3/.env para que se ejecute al levantar con el "docker compose up".  
   5 Para cambiar las credenciales de rabbitMQ:
      5.1 Cambiar las variables de entorno en Cluster2/rabbit/Dockerfile  
      5.2 Cambiar Cluster1/Backend/model/__init__.py, donde se establece la conexión a la cola.  
      5.3 Cambiar Cluster2/Publisher-Backend/app.py, donde se establece la conexión a la cola.  
      5.4 Cambiar Cluster2/Suscription-Backend/reciber.py, donde se establece la conexión a la cola.  
      5.5 Cambiar Cluster3/GarbageCollector/garbage.py, donde se establece la conexión a la cola.  
   6 Para cambiar la cantidad de clientes simultáneos en conciertos con la misma cola, se debe cambiar en  Cluster2/Suscription-Backend/config/config.json
