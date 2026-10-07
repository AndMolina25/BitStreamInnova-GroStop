# Bitácora Conjunta de Trabajo - GroStop

**Integrantes:** Dahir Miguel Martinez Ortiz & Yahir Obed Martinez Ortiz  
**Roles:** Desarrollo de Módulos (Backend) / Refactorización Integral de Interfaz y Experiencia de Usuario (UI/UX)  
**Célula:** BitStream Innova  

---

### Justificación de Intervención y Cobertura de Rol

Ante la ausencia de la integrante asignada originalmente a las tareas de interfaz y experiencia de usuario, asumimos de manera conjunta la responsabilidad de la auditoría heurística, el rediseño visual y la implementación técnica del sistema (UI/UX), combinando esfuerzos en el desarrollo y la modernización estética para garantizar la entrega profesional del proyecto.

---

### Registro de Actividades por Fases

#### Días 6 - 8: Auditoría Heurística y Diagnóstico Visual
* **Actividad realizada:** Recorrido conjunto e inspección técnica de las plantillas Jinja2 dentro del paquete `market/templates/` y estilos CSS en `market/static/`.
* **Hallazgos:**
  * Uso de una estructura base obsoleta y componentes de Bootstrap que requerían actualización urgente hacia un estándar profesional.
  * Identificación de carencias en la retroalimentación al usuario y formularios administrativos saturados.
* **Entregable:** Diagnóstico y estructuración del plan de modernización visual para el sistema.

#### Días 9 - 11: Coordinación de Flujos y Documentación del Sistema
* **Actividad realizada:** Organización, revisión de flujos de experiencia de usuario y validación de la integración entre las vistas de cliente/administrador y las consultas al backend.
* **Hallazgos:**
  * Necesidad imperativa de unificar la identidad gráfica en todas las plantillas y accesos.
* **Entregable:** Consolidación de flujos de navegación integrados en la documentación del equipo.

#### Días 12 - 14: Modernización Integral y Refactorización a Flat Design (Fase Final)
* **Actividad realizada:** Rediseño, codificación colaborativa y migración total de las vistas de la aplicación (`home.html`, `base.html`, `UserLogin.html`, `AdminLogin.html`, registros y paneles) hacia un sistema visual unificado de **Flat Design** minimalista.
* **Implementación técnica:**
  * Establecimiento de variables CSS globales (`--fd-accent`: `#0d7a6f`, `--fd-page`: `#f4f6f8`, `--fd-surface`: `#ffffff`).
  * Reestructuración de layouts a un formato moderno de dos columnas tipo *split-screen* y tarjetas limpias con bordes sutiles de 1px.
  * Sincronización de formularios y variables de Jinja2 asegurando estabilidad absoluta con Flask y MySQL.
* **Entregable:** Interfaces de usuario modernizadas, responsivas y operando en el entorno local de pruebas (`http://127.0.0.1:5000`).

#### Días 15: Sincronización y Despliegue en la Rama Principal
* **Actividad realizada:** Consolidación de los cambios de código, control de versiones mediante Git y sincronización final en la rama `main` del repositorio remoto.
