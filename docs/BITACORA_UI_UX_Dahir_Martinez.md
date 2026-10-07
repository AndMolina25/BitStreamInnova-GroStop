# Bitácora Individual de Trabajo - GroStop
**Integrante:** Dahir Miguel Martinez Ortiz [cite:1,3]  
**Rol:** Diseñador de Interfaces y Experiencia (UI/UX)[cite:3,4]  
**Célula:** BitStream Innova[cite:1]  

### Justificación de Incorporación
A causa de la baja de la integrante originalmente asignada a este rol, asumí la responsabilidad de la evaluación heurística de interfaz y experiencia de usuario a partir del corte de los Días 6-8 para evitar vacíos en la entrega final del equipo[cite:3,4].

### Registro de Actividades por Fases

#### Días 6 - 8: Auditoría Heurística y Diagnóstico Visual[cite:3,4]
* **Actividad realizada:** Recorrido e inspección técnica de las plantillas Jinja2 dentro del paquete `market/templates/` y estilos CSS en `market/static/`[cite:3,15].
* **Hallazgos:**
    - Uso consistente del sistema de rejilla (*grid*) de Bootstrap para presentar el catálogo y consistencia en los componentes de botones y tablas[cite:3,15].
    - En el perfil de Cliente: ausencia de retroalimentación inmediata (*toast/alert*) al agregar productos al carrito y falta de jerarquía visual en los precios del catálogo[cite:15].
    - En el perfil de Administrador: formularios de alta extensos sin validación visual diferenciada y tablas de pedidos sin paginación ni filtros por estado[cite:2,15].
* **Dificultades:** Rastrear el flujo de datos dinámicos de los formularios únicamente a través de la sintaxis Jinja2 antes del despliegue completo del entorno local[cite:3].
* **Entregable:** Archivo formal `docs/EVALUACION_UI_UX.md` integrado en el repositorio del equipo (`BitStreamInnova-GroStop`)[cite:4,15].

#### Días 9 - 11: Coordinación de Flujos y Documentación Visual del Sistema[cite:4]
* **Actividad realizada:** Organización y revisión de la experiencia de usuario dentro del documento consolidado del sistema, garantizando la correcta integración gráfica de los diagramas de casos de uso y datos en Markdown[cite:4,12,13].
* **Hallazgos:**
    - Se comprobó que el flujo del usuario cliente requería clarificar visualmente las dependencias de compra (validación de existencias antes del procesamiento de la orden)[cite:12,13].
    - Se organizó la estructura del repositorio ubicando los diagramas en la ruta `docs/img/` para una lectura clara y profesional en GitHub[cite:12,13].
* **Entregable:** Sección de modelado e interfaces integrada en `docs/DESCRIPCION_DEL_SISTEMA.md`[cite:4,12,13].

#### Días 13 - 14: Diagnóstico de Viabilidad e Intento de Implementación Visual[cite:3,4]
* **Actividad realizada:** Intento de traslación e integración de las mejoras visuales planificadas (rediseño de tarjetas de catálogo con badges de disponibilidad y microinteracciones) sobre las plantillas HTML/Bootstrap del repositorio[cite:3,15].
* **Dificultades:**
    - No fue viable consolidar la implementación en código dentro de la rama activa debido a desfases en la estructura de plantillas y a que los esfuerzos inmediatos se concentraron en garantizar la estabilidad del arranque local del backend[cite:2,4].
* **Entregable:** Especificación heurística y propuesta de mejora visual documentadas formalmente para ser retomadas en siguientes iteraciones[cite:4,15].