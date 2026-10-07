# Bitácora Individual de Trabajo - GroStop
**Integrante:** Dahir Miguel Martinez Ortiz[cite:1]  
**Rol:** Analista de Requisitos y Modelado SRS[cite:1]  
**Célula:** BitStream Innova[cite:1]  

### Registro de Actividades por Fases

#### Días 1 - 2: Recepción del Proyecto y Análisis del Repositorio[cite:3,4]
* **Actividad:** Clonación e inspección preliminar de la estructura de archivos del repositorio base (`vibhorag101/ECommerce-Grocery-Store`)[cite:2].
* **Hallazgos:**
    - El proyecto está desarrollado en Flask (Python) con plantillas Jinja2 y soporte de interfaz mediante Bootstrap[cite:2,3].
    - La persistencia se define en el script `Dump.sql` sobre la base de datos `online_store`[cite:2].
    - La configuración de credenciales del servidor de base de datos se desacopla en `database.yaml`[cite:2].
* **Dificultades:** Identificar inicialmente cómo el sistema valida los roles al ingresar, ya que no existe una columna `rol` unificada en una sola tabla de usuarios[cite:2].

#### Días 3 - 5: Exploración de Modelos y Rutas de la Aplicación[cite:3,4]
* **Actividad realizada:** Rastreo de endpoints en los archivos de rutas de Flask y análisis de las plantillas HTML asociadas[cite:3].
* **Hallazgos:**
    - El flujo de arranque en `run.py` conduce a una pantalla inicial de segmentación de tres roles: Administrador, Vendedor y Cliente[cite:2].
    - La autenticación se segmenta en tablas independientes (`customer`, `admin`, `seller`)[cite:2].
    - El sistema maneja un esquema de carrito único por cliente autenticado (`cart`) antes de consolidar el pedido en una orden final[cite:2].
* **Dificultades:** Comprender las restricciones de llaves foráneas en el carrito al interactuar con el módulo de cupones de descuento[cite:2].

#### Días 6 - 8: Redacción de la Especificación de Requisitos (SRS)[cite:3,4]
* **Actividad realizada:** Elaboración de la matriz de actores, catálogo de requisitos funcionales (RF), requisitos no funcionales (RNF) y descripción detallada de interfaces[cite:2].
* **Hallazgos:**
    - Se mapearon 16 requisitos funcionales divididos en 5 módulos operativos[cite:3].
    - Se documentaron las 9 interfaces principales del sistema desglosando datos de entrada, acciones y perfiles autorizados[cite:2].
* **Entregable:** Archivo formal `DOCUMENTACION_SRS.md` integrado en el repositorio del equipo (`BitStreamInnova-GroStop`)[cite:2].

#### Días 9 - 11: Consolidación Documental y Soporte al Modelado UML[cite:4]
* **Actividad realizada:** Integración, análisis técnico y consolidación formal del documento del sistema incorporando los diagramas generados por la arquitectura de software (`diagrama_casos_uso.jpg` y `diagrama_datos.jpg`)[cite:12,13].
* **Hallazgos:**
    - Se constató en el diagrama de casos de uso la correcta inclusión del actor Repartidor (`delivery_boy`) y las relaciones `<<include>>` críticas para autenticación, validación de stock y checkout[cite:2,13].
    - Se verificó en el diagrama de clases la separación desacoplada de perfiles y la relación estructural entre `Carrito`, `ItemCarrito`, `Pedido` e `ItemPedido` según el script `Dump.sql`[cite:2,12].
* **Entregable:** Coautoría y publicación del documento técnico consolidado `docs/DESCRIPCION_DEL_SISTEMA.md` con recursos gráficos enlazados en `docs/img/`[cite:4,12,13].

#### Días 13 - 14: Verificación Funcional y Preparación de Checkpoint[cite:3,4]
* **Actividad realizada:** Auditoría final de la coherencia entre el catálogo de requisitos funcionales (SRS), los casos de uso modelados y el comportamiento del backend documentado[cite:2,4].
* **Hallazgos:**
    - Se estructuró la argumentación técnica para defender cómo el sistema desacopla los perfiles de usuario y cómo opera la persistencia del carrito hacia la orden final[cite:2,4].
* **Dificultades:** Alinear los tiempos de cierre de los diagramas del equipo para sincronizar el documento general con las especificaciones del SRS[cite:3,4].
* **Entregable:** Matriz completa de requerimientos y documento consolidado del sistema listos para el checkpoint con el docente[cite:2,4].