# Bitácora de Pruebas Funcionales e Integración — GroStop

## Proyecto
**BitStreamInnova - GroStop**

## Objetivo

Instalar, configurar, ejecutar y explorar el funcionamiento del sistema GroStop,
documentando las pruebas realizadas, los resultados obtenidos, los errores
encontrados y las posibles mejoras identificadas durante el proceso.

---

# 1. Preparación del proyecto

Se clonó el repositorio del proyecto mediante Git:

git clone https://github.com/AndMolina25/BitStreamInnova-GroStop.git

Posteriormente se ingresó a la carpeta del proyecto y se verificó el estado
del repositorio mediante Git.

Se abrió el proyecto utilizando Visual Studio Code.

---

# 2. Configuración de Python

Durante la instalación se detectaron problemas de compatibilidad entre algunas
dependencias del proyecto y las versiones más recientes de Python.

Inicialmente se realizaron pruebas con Python 3.12 y Python 3.13, pero algunas
dependencias presentaron errores durante su instalación.

Para solucionar el problema se instaló:

**Python 3.10.11**

Posteriormente se creó un entorno virtual:

py -3.10 -m venv venv

Se activó mediante:

.\venv\Scripts\Activate.ps1

Se actualizaron las herramientas necesarias:

python -m pip install --upgrade pip setuptools wheel

Finalmente se instalaron correctamente las dependencias:

pip install -r requirements.txt

### Resultado
Entorno virtual configurado correctamente y dependencias del proyecto instaladas.

**Estado: EXITOSO**

---

# 3. Configuración de MySQL

Se instaló MySQL Community Server junto con MySQL Workbench.

Se configuró el servidor utilizando:

- MySQL Server 8.0
- Puerto: 3306
- Usuario administrador: root
- Servicio de Windows: MySQL80

Por seguridad, la contraseña utilizada para la conexión no se documenta en
esta bitácora.

---

# 4. Restauración de la base de datos

Al revisar el archivo `Dump.sql` se identificó que la base utilizada por el
proyecto es:

online_store

Se creó manualmente mediante:

CREATE DATABASE online_store;
USE online_store;

Posteriormente se ejecutó el archivo `Dump.sql`.

La importación permitió recuperar las tablas utilizadas por el sistema,
incluyendo, entre otras:

- admin
- cart
- category
- customer
- delivery_boy
- offer
- orders
- product
- product_feedback
- rates_order_delivery
- seller
- sells

### Resultado
Base de datos restaurada correctamente.

**Estado: EXITOSO**

---

# 5. Configuración de la conexión

Se revisó el archivo:

database.yaml

Se configuraron los datos correspondientes al servidor MySQL local.

La contraseña utilizada no se incluye en esta documentación por razones
de seguridad.

---

# 6. Ejecución de GroStop

Con el entorno virtual activo se ejecutó:

python run.py

Flask inició correctamente mostrando:

Running on http://127.0.0.1:5000

Se ingresó desde el navegador y se comprobó que la aplicación cargara.

### Resultado
GroStop se ejecuta correctamente de manera local.

**Estado: EXITOSO**

---

# 7. Corrección de interfaz de página principal

Durante la primera ejecución se detectó que los botones de la página principal
aparecían desalineados y parcialmente cortados.

Se revisó la ruta principal en `routes.py`:

@app.route('/HomePage')
@app.route('/')

Se identificó que la página inicial utiliza:

homepage.html

Se revisó y ajustó la distribución visual de esta plantilla para mejorar
el centrado y visualización de los botones.

### Resultado
La página principal quedó funcional y con una mejor distribución visual.

**Estado: CORREGIDO**

---

# 8. Pruebas funcionales — Cliente

## 8.1 Acceso al módulo Cliente

Desde la página principal se seleccionó:

**Enter as User**

El sistema mostró correctamente las opciones:

- Acceso
- Registro

**Resultado: EXITOSO**

---

# 9. Registro de cliente

Se ingresó al formulario de registro.

El sistema solicita:

- Nombre
- Apellido
- Correo electrónico
- Contraseña
- Número telefónico

Se utilizaron datos ficticios exclusivamente para las pruebas.

Después de enviar el formulario, el sistema mostró:

**"¡Te has registrado correctamente!"**

### Resultado
El registro de clientes funciona correctamente.

**Estado: EXITOSO**

---

# 10. Inicio de sesión como cliente

Después del registro se realizó el inicio de sesión utilizando la cuenta
de prueba.

El sistema permitió el acceso y mostró el catálogo de productos.

Cada producto presenta información como:

- Nombre
- Marca
- Precio
- Opción para añadir a la cesta

### Resultado
El inicio de sesión y la visualización del catálogo funcionan.

**Estado: EXITOSO**

---

# 11. Prueba del carrito

Se seleccionaron productos del catálogo mediante la opción:

**"añadir a la cesta"**

El sistema mostró el mensaje:

**"¡El producto se ha añadido correctamente al carrito!"**

Posteriormente se ingresó al carrito y se comprobó que los productos
seleccionados aparecieran correctamente.

### Resultado
La función de agregar productos al carrito funciona.

**Estado: EXITOSO**

---

# 12. Generación del pedido

Durante la prueba se seleccionaron dos productos:

- Producto 1: 25 rupias
- Producto 2: 26 rupias

El sistema calculó correctamente:

25 + 26 = 51 rupias

En la pantalla del pedido apareció:

**"Su importe total es: 51 rupias"**

Posteriormente se solicitaron:

- Número de casa
- Ciudad
- Estado
- Código postal
- Forma de pago

Se utilizaron datos ficticios para completar la prueba.

Al finalizar, el sistema mostró:

**"¡Su pedido se ha realizado correctamente!"**

### Resultado
El flujo de creación del pedido se completó correctamente desde la interfaz.

**Estado: EXITOSO**

---

# 13. Comprobación del pedido en MySQL

Para comprobar la integración entre Flask y MySQL se ejecutó:

USE online_store;

SELECT * FROM orders;

En ese momento se encontró un nuevo registro correspondiente al pedido
realizado durante las pruebas.

El pedido apareció inicialmente con:

- Order_ID: 11
- Amount: 51
- Mode: efectivo

Esto permitió comprobar inicialmente que la información enviada desde la
interfaz llegó a la base de datos.

### Resultado inicial
Integración entre interfaz, backend y base de datos comprobada.

**Estado INICIAL: EXITOSO**

---

# 14. Pruebas funcionales — Administrador

Se ingresó al módulo:

**Enter as Admin**

Inicialmente se obtuvo un mensaje indicando:

**"Correo electrónico o contraseña incorrectos"**

Al revisar `AdminLogin.html` se descubrió que el formulario realmente solicita:

- First_Name
- Last_Name
- Password

Por lo tanto, el mensaje de error hace referencia a un correo electrónico
aunque el formulario no utiliza correo.

### Hallazgo UX-01

Existe una inconsistencia entre los campos solicitados y el mensaje mostrado
cuando las credenciales son incorrectas.

### Mejora propuesta

Cambiar el mensaje por:

**"Nombre, apellido o contraseña incorrectos."**

---

# 15. Comprobación de administradores

Se revisó la tabla:

admin

mediante MySQL Workbench.

Se confirmó que existen cuentas de administrador almacenadas en la base
de datos.

Utilizando un registro existente se consiguió iniciar sesión correctamente.

### Resultado
Inicio de sesión del administrador funcional.

**Estado: EXITOSO**

---

# 16. Funciones disponibles para Administrador

Después del inicio de sesión se identificaron las siguientes funciones:

- Ver pedidos
- Agregar repartidor
- Agregar nuevas ofertas
- Agregar nuevo producto
- Agregar vendedor

Esto confirma que el administrador tiene funciones de gestión sobre distintos
elementos del sistema.

---

# 17. Prueba de "Ver pedidos"

Se seleccionó:

**Ver pedidos**

El sistema mostró diferentes pedidos registrados incluyendo:

- Forma de pago
- ID del pedido
- Precio
- Fecha

Sin embargo, durante la revisión no se encontró visualmente el pedido
de prueba con ID 11 e importe de 51 rupias.

Esto inició una investigación del comportamiento del sistema.

---

# 18. Revisión de routes.py

Se encontró la función encargada de consultar los pedidos del administrador.

La consulta utilizada es:

SELECT * FROM orders

Posteriormente el sistema ejecuta:

cur.fetchall()

y construye una lista con información de los pedidos.

Finalmente utiliza:

viewOrder.html

para mostrar los resultados.

No se encontró inicialmente una limitación explícita en la consulta que
explicara la ausencia del pedido 11.

---

# 19. Revisión de viewOrder.html

Se revisó la plantilla:

viewOrder.html

La plantilla utiliza un ciclo:

{% for dict in list %}

Por lo tanto, en principio recorre todos los pedidos recibidos desde
`routes.py`.

No se encontró una condición dentro de la plantilla que excluyera
específicamente el pedido 11.

---

# 20. Investigación del pedido ID 11

Se ejecutó posteriormente:

SELECT *
FROM orders
WHERE Order_ID = 11;

La consulta no devolvió ningún registro.

Esto confirmó que el pedido ID 11, que anteriormente había sido observado
en la tabla `orders`, ya no se encontraba almacenado en la base de datos
al momento de realizar esta segunda comprobación.

### Hallazgo técnico

El pedido ID 11 fue observado inicialmente en la tabla `orders`, pero en una
consulta posterior dejó de estar disponible.

Todavía no se ha determinado qué operación provocó este comportamiento.

---

# 21. Búsqueda de eliminación de pedidos

Para investigar la causa se realizó una búsqueda en el código fuente de:

DELETE FROM orders

No se encontraron coincidencias.

Posteriormente se inició una búsqueda más general utilizando:

DELETE

con el objetivo de determinar si existe alguna operación que elimine
registros mediante otra parte de la aplicación.

### Estado

**INVESTIGACIÓN EN PROCESO**

No se modificará el comportamiento del sistema hasta identificar la causa.

---

# 22. Hallazgos y posibles mejoras hasta el momento

Durante las pruebas se identificaron los siguientes puntos:

1. El proyecto requiere una versión compatible de Python para instalar
   correctamente sus dependencias.

2. La interfaz original presenta algunos problemas de distribución visual.

3. El sistema utiliza rupias como moneda, a pesar de que GroStop puede
   adaptarse al contexto local.

4. El mensaje de error del administrador menciona correo electrónico,
   aunque el formulario utiliza nombre, apellido y contraseña.

5. Se detectó un comportamiento pendiente de investigación relacionado
   con la persistencia del pedido ID 11.

6. Es necesario continuar probando las funciones del administrador.

7. Falta realizar pruebas funcionales del módulo Vendedor.

8. Falta comprobar completamente el módulo Repartidor.

---

# 23. Estado actual del proyecto

| Elemento | Estado |
|---|---|
| Clonación del repositorio | Completado |
| Entorno virtual | Completado |
| Dependencias | Completado |
| MySQL | Completado |
| Restauración de base de datos | Completado |
| Ejecución de Flask | Completado |
| Registro de cliente | Funcional |
| Login de cliente | Funcional |
| Catálogo | Funcional |
| Carrito | Funcional |
| Generación de pedido | Funcional |
| Login de administrador | Funcional |
| Visualización de pedidos | En revisión |
| Agregar repartidor | Pendiente de prueba |
| Agregar ofertas | Pendiente de prueba |
| Agregar productos | Pendiente de prueba |
| Agregar vendedor | Pendiente de prueba |
| Módulo vendedor | Pendiente |
| Módulo repartidor | Pendiente |
| Contenerización/Docker | Pendiente |
| Mejora final | Pendiente |

---

# Conclusión parcial

Se consiguió instalar y ejecutar correctamente GroStop utilizando Flask y
MySQL. Se comprobó gran parte del flujo correspondiente al Cliente y se inició
la exploración del módulo Administrador.

Las pruebas no se limitaron a verificar la interfaz, sino que también se
utilizó MySQL Workbench para comprobar la persistencia de información.

Durante este proceso se identificaron problemas de interfaz, inconsistencias
en mensajes y un comportamiento relacionado con la desaparición del pedido
ID 11 que continúa bajo investigación.

Las siguientes pruebas estarán enfocadas en completar las funciones del
Administrador, Vendedor y Repartidor, documentar los resultados y determinar
las mejoras que se implementarán en el sistema.
