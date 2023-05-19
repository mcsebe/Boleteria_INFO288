## Como ejecutar el codigo:
1. Tener instalado subsistema de linux.
  1.1 Abrir powershell, apretando la tecla "windows" del teclado y escribiendo powershell.
  1.2 Dar click derecho a powershell y ejecutar como administrador.
  1.3 Escribir el siguiente comando "wsl --install" y dar enter.
  1.4 Si existe algún problema en la instalacion seguir instrucciones que windows le entregará.
2. Instalar Docker dando click en el boton "Download Docker Desktop" que se encuentra al abrir https://www.docker.com/products/docker-desktop/.
3. Ejecutar Docker Desktop.
4. Abrir 3 terminales en la carpeta Boleteria_INFO288. 
5. En la primera terminal ingresar a la carpeta Cluster2 con el comando "cd Cluster2"
6. Ejecutar el comando "docker-compose up"
7. En la segunda terminal ingresar a la carpeta Cluster1 con el comando "cd Cluster1"
8. Ejecutar el comando "docker-compose up"
9. En la tercera terminal ingresar a la carpeta Cluster3 con el comando "cd Cluster3"
10. Ejecutar el comando "docker-compose up"
11. Dirigirse a http://localhost:5000/ para utilizar la pagina.
