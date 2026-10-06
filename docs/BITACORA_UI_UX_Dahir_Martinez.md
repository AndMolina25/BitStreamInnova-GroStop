# Bitácora Individual de Trabajo - GroStop
**Integrante:** Dahir Miguel Martinez Ortiz (Asignado tras reestructuración de la célula)[cite:1,10]
**Rol:** Diseñador de Interfaces y Experiencia (UI/UX)[cite:10,11]
**Célula:** BitStream Innova[cite:1]

### Justificación de Incorporación
A causa de la baja de la integrante originalmente asignada a este rol, asumí la responsabilidad de la evaluación heurística de interfaz y experiencia de usuario a partir del corte de los Días 6-8 para evitar vacíos en la entrega final del equipo[cite:3,10,11].

### Registro de Actividades por Fases

#### Días 6 - 8: Auditoría Heurística y Diagnóstico Visual
* **Actividad realizada:** Recorrido e inspección técnica de las plantillas Jinja2 dentro del paquete `market/templates/` y estilos CSS en `market/static/`[cite:3,12].
* **Hallazgos:**
    - Uso consistente del sistema de rejilla (*grid*) de Bootstrap para presentar el catálogo y consistencia en los componentes de botones y tablas[cite:3,12].
    - En el perfil de Cliente: ausencia de retroalimentación inmediata (*toast/alert*) al agregar productos al carrito y falta de jerarquía visual en los precios del catálogo[cite:12].
    - En el perfil de Administrador: formularios de alta extensos sin validación visual diferenciada y tablas de pedidos sin paginación ni filtros por estado[cite:7,12].
* **Dificultades:** Rastrear el flujo de datos dinámicos de los formularios únicamente a través de la sintaxis Jinja2 antes del despliegue completo del entorno local[cite:3].
* **Entregable:** Archivo formal `docs/EVALUACION_UI_UX.md` integrado en el repositorio del equipo (`BitStreamInnova-GroStop`)[cite:11,12].

#### Días 9 - 11: Coordinación de Flujos y Mockups de Mejora[cite:3]
* **Actividad realizada:** Enlace con la arquitectura del sistema para asegurar que las pantallas evaluadas coincidan con los diagramas de casos de uso y definición de la propuesta visual para las tarjetas de producto[cite:3,12].
* **Hallazgos:**
    - Se delimitó la necesidad de modernizar la tarjeta de producto integrando insignias de stock visible para evitar intentos de compra de artículos sin existencias[cite:3,12].
* **Dificultades:** Coordinar los tiempos de revisión de los wireframes/mockups con el avance del modelado UML del equipo[cite:3].

#### Días 13 - 14: Implementación de la Propuesta Visual (Proyección)[cite:3,11]
* **Actividad planificada:** Colaborar con el desarrollador backend para integrar insignias (*badges*) de disponibilidad de inventario y alertas visuales en la tarjeta de producto dentro del catálogo[cite:11,12].
* **Entregable:** Plantilla HTML/Bootstrap actualizada y lista para pruebas funcionales con el equipo[cite:3,11].