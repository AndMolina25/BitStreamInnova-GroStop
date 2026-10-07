# Bitácora Individual de Trabajo - GroStop
**Integrante:** Dahir Miguel Martinez Ortiz[cite:1]
**Rol:** Analista de Requisitos y Modelado SRS[cite:1]
**Célula:** BitStream Innova[cite:1]

### Registro de Actividades por Fases

#### Días 1 - 2: Recepciónb del Proyecto y Análisis del Repositorio
* **Actividad:** Clonación e inspección preliminar de la estructura de archivos del repositorio base (`vibhorag101/ECommerce-Grocery-Store`).
* **Hallazgos:**
    - El proyecto está desarrollado en Flask (Python) con plantillas Jinja2 y soporte de intefaz mediante Bootstrap[cite:3,7].
    - La persistencia se define en el script `Dump.sql` sobre la base de datos `online_store`[cite:7].
    - La configuración de credenciales del servidor de base de datos se desacopla en `database.yaml`[cite:7].
* **Dificultades:** Identificar inicialmente cómo el sistema valida los roles al ingresar, ya que no existe una columna `rol` unificada en una sola tabla de usuarios[cite:7].

#### Días 3 - 5: Exploración de Modelos y Rutas de la Aplicación[cite:3]
* **Actividad realizada:** Rastreo de endpoints en los archivos de rutas de Flask y análisis de las plantillas HTML asociadas[cite:3].
* **Hallazgos:**
    -El flujo de arranque en `run.py` conduce a una pantalla inicial de segmentación de tres roles: Administrador, Vendedor y Cliente[cite:7].
    -La autenticación se segmenta en tablas independientes(`customer`,`admin`,`seller`)[cite:7].
    -El sistema maneja un esquema de carrito único por cliente autenticado (`cart`) antes de consolidar el pedido en una orden final[cite:7].
* **Dificultades:** Comprender las restrucciones de llaves foráneas en el carrito al interactuar con el módulo de cupones de descuento[cite:7].

#### Días 6-8: Redacción de la especificación de Requisitos (SRS)[cite:3]
* **Actividad realizada:** Elaboración de la matríz de actores, catálogo de requisitos funcionales (RF), requisitos no funcionales (RNF) y descripción detallada de interfaces[cite:2,7].
* **Hallazgos:**
    - Se mapearon 16 requisitos funcionales divididos en 5 módulos operativos [cite:3].
    - Se documentaron las 9 interfaces principales del sistema desglosando datos de entrada, acciones y perfiles autorizados [cite:7].

* **Entregable:** Archivo formal `DOCUMENTACION_SRS.md` integrado en el repositorio del equipo (`BitStreamInnova-GroStop`)[cite:7].