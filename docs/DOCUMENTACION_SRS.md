# ESPECIFICACIÓN DE REQUISITOS DE SOFTWARE (SRS) — GroStop
**Analista de Requisitos:** Dahir Miguel Martinez Ortiz  
**Célula:** BitStream Innova  
**Proyecto Base:** GroStop (Flask / MySQL)

---

## 1. Introducción y Alcance del Sistema
A partir del análisis del código fuente y el script de base de datos (`Dump.sql`) del repositorio base, GroStop es una plataforma web de comercio electrónico de abarrotes desarrollada sobre Flask, Jinja2 y MySQL. El sistema centraliza la intermediación comercial entre clientes finales, proveedores de inventario (sellers), personal de entrega física (delivery boys) y la administración central del negocio.

---

## 2. Matriz de Actores y Control de Acceso
El sistema no utiliza un esquema de roles unificado en una sola tabla, sino entidades separadas en la base de datos para cada perfil:

| Actor / Rol | Tabla Base de Datos | Responsabilidad y Acceso en la Plataforma |
| :--- | :--- | :--- |
| **Customer (Cliente)** | `customer` | Usuario final comprador. Puede registrarse desde la web, navegar el catálogo general o por categoría, gestionar su carrito activo, aplicar cupones de descuento, confirmar órdenes y calificar tanto productos como al repartidor asignado. |
| **Admin (Administrador)** | `admin` | Administrador general de la tienda. Da de alta categorías, crea el catálogo maestro de productos, registra vendedores, da de alta a repartidores y monitorea el historial global de pedidos. |
| **Seller (Vendedor)** | `seller` | Proveedor asociado. No da de alta productos nuevos, sino que ingresa al panel para actualizar existencias (stock) de los productos del catálogo y auditar el volumen de ventas de sus artículos. |
| **Delivery Boy (Repartidor)** | `delivery_boy` | Personal logístico. Consulta pedidos asignados para despacho y recibe la retroalimentación/calificación del comprador al concretar la entrega. |

---

## 3. Requisitos Funcionales del Sistema (RF)

### 3.1 Módulo de Acceso y Sesión
* **RF-01 (Selección de Perfil):** Al acceder a la raíz del sistema, la interfaz debe obligar a seleccionar el tipo de acceso: *Admin*, *Seller* o *Customer*.
* **RF-02 (Registro de Clientes):** Formulario exclusivo para clientes que valida nombre, apellidos, teléfono, correo electrónico y contraseña en la tabla `customer`.
* **RF-03 (Autenticación por Perfil):** El login debe contrastar credenciales contra la tabla respectiva del actor seleccionado y mantener la sesión mediante cookies seguras en Flask.
* **RF-04 (Cierre de Sesión):** Destrucción de la sesión activa en el servidor y redirección a la pantalla de selección de rol.

### 3.2 Módulo de Catálogo y Productos
* **RF-05 (Catálogo General y Filtrado):** Visualización de productos con nombre, marca, precio de lista (MRP), unidad de medida y disponibilidad. Permite filtrado por el identificador de categoría (`category_id`).
* **RF-06 (Gestión de Categorías - Admin):** Alta y mantenimiento de categorías en la tabla `category`. Ninguna categoría debe quedar huérfana de productos según las restricciones del esquema.
* **RF-07 (Catálogo Maestro de Productos - Admin):** Alta de productos asociándolos al `Admin_ID` que los crea y a una categoría válida.

### 3.3 Módulo de Carrito, Cupones y Checkout
* **RF-08 (Gestión de Carrito Único):** Cada cliente autenticado mantiene únicamente un carrito activo (`cart`). Permite sumar unidades, restar o remover artículos.
* **RF-09 (Validación de Ofertas y Cupones):** Permite ingresar códigos promocionales que validan:
  1. Monto mínimo de compra en el carrito.
  2. Aplicación de porcentaje de descuento con un tope máximo fijado por la administración.
* **RF-10 (Checkout y Generación de Orden):** Conversión del carrito activo en una orden de compra, registrando dirección de entrega y asignando un estado inicial.
* **RF-11 (Historial y Seguimiento):** Consulta de órdenes pasadas asociadas únicamente al `Customer_ID` de la sesión activa.

### 3.4 Módulo de Inventario y Operación
* **RF-12 (Gestión de Stock - Seller):** El vendedor consulta la lista de productos y actualiza las existencias disponibles para venta.
* **RF-13 (Alta de Proveedores y Repartidores - Admin):** Registro de credenciales y datos operativos de nuevos vendedores y repartidores por parte del administrador.
* **RF-14 (Auditoría Global de Pedidos - Admin):** Vista centralizada de todas las órdenes emitidas en la tienda para control logístico.

### 3.5 Módulo de Feedback
* **RF-15 (Calificación de Productos):** Formulario para que el cliente califique y comente los productos adquiridos.
* **RF-16 (Calificación del Repartidor):** Evaluación del desempeño del repartidor asignado a la entrega de una orden específica.

---

## 4. Requisitos No Funcionales (RNF)

* **RNF-01 (Persistencia Relacional):** Integridad referencial mandatoria con motor MySQL (`online_store`), gestionada mediante claves foráneas entre usuarios, carritos, productos y órdenes.
* **RNF-02 (Configuración Desacoplada):** Los parámetros de conexión (`mysql_host`, `mysql_user`, `mysql_password`, `mysql_db`) deben mantenerse aislados en el archivo `database.yaml` para facilitar despliegues locales y en contenedores.
* **RNF-03 (Interfaz y Usabilidad):** Vistas web renderizadas mediante Jinja2 y maquetadas con Bootstrap 5, garantizando tiempos de carga locales inferiores a 1 segundo.
* **RNF-04 (Despliegue y Ejecución):** Ejecución nativa mediante script de arranque `run.py` bajo entornos Python 3.8+ y compatibilidad con Dockerfile para contenerización.

---

## 5. Descripción y Flujo de Pantallas

* **Pantalla de Inicio / Acceso General (`/`):** Vista inicial que no muestra mercancía; despliega tres tarjetas de acceso para direccionar al usuario según su rol (*Customer*, *Seller*, *Admin*).
* **Login de Cliente / Admin / Seller (`/login`):** Formulario de validación de correo y contraseña. Incluye el switch hacia el formulario de registro si el rol es cliente.
* **Registro de Cliente (`/register`):** Formulario de captura de datos personales (nombre, teléfono, correo y contraseña).
* **Catálogo y Vista de Productos (`/home`):** Muro principal de abarrotes con cuadrícula de productos, precio, opción de agregar al carrito y selector de categorías.
* **Carrito de Compras (`/cart`):** Tabla de artículos acumulados, cálculo de subtotal, campo de texto para código de cupón y botón de proceder a pagar.
* **Confirmación de Orden (`/checkout`):** Pantalla de confirmación donde se ingresa la dirección de entrega y se resume el costo final con descuento aplicado.
* **Panel de Control del Vendedor (`/seller`):** Interfaz para consultar unidades vendidas y actualizar cantidades disponibles por producto.
* **Panel Administrativo (`/admin`):** Dashboard central para crear categorías, dar de alta productos, enrolar vendedores/repartidores y auditar pedidos globales.