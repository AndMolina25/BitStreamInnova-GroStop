# Documento Técnico de Consolidación — Sistema GroStop (Días 9-11)

**Célula de Trabajo:** BitStream Innova[cite:1]  
**Integrantes:**
- Martinez Martinez Eidy Elizabeth (Líder Técnico / Arquitecto de Software)[cite:3]
- Martinez Ortiz Dahir Miguel (Analista de Requisitos SRS y Diseñador UI/UX)[cite:1, 3]
- Martinez Ortiz Yahir Obed (Desarrollador de Módulos Asociados)[cite:3]
- Molina Espinoza Andres (Tester y Control de Plazos)[cite:3]

**Repositorio Base:** `vibhorag101/ECommerce-Grocery-Store`[cite:2,4]  
**Stack de Desarrollo:** Python (Flask), MySQL, Jinja2, HTML5, CSS3, Bootstrap[cite:2,4]  

## 1. Descripción General del Sistema
GroStop es una solución web de comercio electrónico enfocada en la comercialización y distribución de abarrotes[cite:2,4]. Desarrollada sobre el framework Flask con persistencia relacional en MySQL (`online_store`)[cite:2,4], la plataforma desacopla la interacción operativa de cuatro actores clave: el consumidor final (**Cliente**), el proveedor de existencias (**Vendedor**), el operador logístico de última milla (**Repartidor**) y el gestor de la plataforma (**Administrador**)[cite: 2,12,13].

## 2. Matriz de Usuarios y Control de Acceso (Permisos)
El sistema no utiliza un campo unificado de roles dentro de una tabla genérica; la autenticación e interfaces están segmentadas a nivel de esquema en entidades independientes[cite:2]:

| Actor / Perfil | Entidad BD | Permisos y Operaciones en el Sistema |
| :--- | :--- | :--- |
| **Cliente (Customer)** | `customer`[cite:2] | Registro público, autenticación de sesión, navegación del catálogo con filtrado, gestión de carrito activo único (`cart`), aplicación de cupones de descuento, confirmación de pedidos (*checkout*), historial de compras y calificación de artículos y repartidores[cite: 2,12,13]. |
| **Administrador (Admin)** | `admin`[cite:2] | Acceso restringido al panel de control, alta y mantenimiento de categorías (`category`), creación del catálogo maestro de productos (`product`), registro operativo de vendedores y repartidores, y auditoría general de pedidos emitidos[cite: 2,12,13]. |
| **Vendedor (Seller)** | `seller`[cite:2] | Acceso a panel de existencias; no crea artículos nuevos en el catálogo maestro, sino que actualiza el stock disponible de productos asociados y audita el volumen de ventas de su inventario[cite:2,12,13]. |
| **Repartidor (Delivery Boy)** | `delivery_boy`[cite:2] | Acceso operativo para consultar pedidos asignados para despacho y recepción del puntaje/retroalimentación asignado por el comprador al concretar la entrega[cite:2,12,13]. |

## 3. Modelado UML del Sistema

### 3.1 Diagrama de Casos de Uso
El modelo de casos de uso refleja las interacciones de los cuatro actores con las fronteras del sistema, delimitando las validaciones críticas mediante relaciones `<<include>>` (como validación de credenciales, control de existencias antes de agregar al carrito y procesamiento de pagos)[cite:2,13]:

![Diagrama de Casos de Uso - GroStop](img/diagrama_casos_uso.jpg)

**Análisis de Interacciones por Actor:**
* **Cliente:** Dispone del flujo principal de compra que abarca consultar, buscar/filtrar, ver detalles y agregar productos al carrito con validación de existencias[cite:13]. Su proceso de formalización del pedido (`Realizar pedido`) incluye de manera obligatoria el procesamiento de pago y la validación opcional de cupones de descuento[cite:2,13].
* **Vendedor:** Gestiona su interacción operativa a través de la actualización de stock/existencias de sus productos, la visualización de pedidos asociados y la consulta de reportes de ventas[cite:2,13].
* **Administrador:** Centraliza el gobierno del sistema mediante el alta y administración de usuarios (clientes, vendedores y repartidores) sujeta a validación de permisos[cite:13]. Administra el catálogo maestro de productos, gestiona cupones de descuento y supervisa los reportes globales de pedidos[cite:2,13].
* **Repartidor (Delivery Boy):** Gestiona la fase logística consultando pedidos asignados mediante validación de estado de pedido, actualizando el progreso de entrega y consultando el historial de sus despachos[cite:2,13].

### 3.2 Diagrama de Clases y Entidades
El diagrama de clases modela el dominio del sistema manteniendo fidelidad con las relaciones foráneas y la persistencia relacional del script `Dump.sql`[cite:2,12]:

![Diagrama de Clases - GroStop](img/diagrama_datos.jpg)

**Estructura y Reglas del Dominio:**
* **Desacoplamiento de Usuarios:** Las clases `Customer`, `Admin`, `Seller` y `DeliveryBoy` modelan entidades separadas, alineándose con las tablas aisladas de la base de datos MySQL[cite:2,12].
* **Ciclo de Compra (`Carrito` vs. `Pedido`):** 
  * Un `Customer` posee una relación estricta (1 a 1) con su `Carrito` activo[cite:2,12].
  * El `Carrito` se compone de múltiples instancias de `ItemCarrito` (1 a 0..*), donde cada ítem referencia un `Producto` del catálogo[cite:12].
  * Al consolidar la compra, se genera una entidad `Pedido` vinculada al `Customer`, la cual contiene instancias de `ItemPedido`, se asigna a un `DeliveryBoy` y puede aplicar de forma opcional (0..1) una entidad `Cupon`[cite:2,12].
* **Gestión de Catálogo e Inventario:** Cada `Producto` pertenece a una `Categoria` específica (0..* a 1) y recibe abastecimiento por parte de uno o varios vendedores (`Seller`) mediante la relación de publicación de existencias[cite:2,12].

## 4. Metodología de Deducción y Hallazgos Técnicos (Bitácora Grupal)
Para llegar a este modelado formal, la célula desarrolló un proceso deductivo estructurado[cite:4]:

1. **Inspección de Persistencia:** A través del análisis del script `Dump.sql`, se identificaron las relaciones foráneas que gobiernan las compras, confirmando que cada cliente opera un único carrito activo antes de generar una orden[cite:2].
2. **Auditoría de Rutas y Controladores:** Se rastrearon los decoradores `@app.route` en el código Flask para aislar el flujo de inicio de sesión (`/login`), identificando que la validación se distribuye hacia tablas independientes según la tarjeta seleccionada en la vista raíz[cite:2].
3. **Inspección de Plantillas Jinja2:** En `market/templates/` se detectó la estructura visual de las vistas operativas, validando los componentes de interacción de clientes y formularios administrativos[cite:1].
4. **Rectificación de Roles en el Modelado:** La inspección del código permitió corregir dos discrepancias críticas respecto a los análisis iniciales[cite:2]:
   - Se integró formalmente al **Repartidor** (`delivery_boy`), actor ausente en bocetos preliminares pero clave en la asignación de pedidos[cite:2,12,13].
   - Se delimitó el alcance del **Vendedor**, clarificando que su función técnica en el backend es actualizar existencias y cantidades vendidas, mientras que la creación maestro del artículo reside en el perfil de Administrador[cite:2,12,13].
