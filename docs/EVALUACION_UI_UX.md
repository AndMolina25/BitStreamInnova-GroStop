# Evaluación Heurística y Diagnóstico de Interfaz (UI/UX) — GroStop
**Evaluador:** Dahir Miguel Martinez Ortiz (Asumiendo responsabilidades UI/UX)[cite:1,10]  
**Célula:** BitStream Innova[cite:1]  
**Ruta de Vistas Evaluadas:** `market/templates/` y `market/static/`[cite:3]  
**Stack de Interfaz:** Jinja2 Templates, HTML5, CSS3, Bootstrap 4/5[cite:3]

## 1. Alcance y Objetivos de la Evaluación
Este documento recoge el análisis visual y funcional de la experiencia de usuario (UX) y el diseño de interfaces (UI) de GroStop, recorriendo el flujo de interacción de los perfiles principales: **Cliente** y **Administrador**[cite: 11]. El objetivo es identificar aciertos de maquetación, fricciones operativas y formular una propuesta de mejora para los Días 13 y 14.

## 2. Diagnóstico Heurístico por Perfil de Usuario

### 2.1 Perfil: Cliente (Customer)[cite:11]

#### Acceso y Navegación Inicial (`home.html` / `login.html`)
* **Aspectos Positivos:**
  - El sistema de rejilla (*grid*) de Bootstrap organiza de manera clara las categorías y la distribución básica de los productos en pantalla[cite:3].
  - La barra de navegación superior proporciona accesos directos al carrito y al cierre de sesión[cite:7].
* **Áreas de Oportunidad (Fricción UX):**
  - **Sobrecarga en la decisión inicial:** Al ingresar al sistema, la pantalla de inicio prioriza la selección de rol en lugar de ofrecer una vitrina directa de productos destacados o promociones de abarrotes[cite:7].
  - **Jerarquía tipográfica:** Los precios y nombres de artículos presentan pesos visuales similares, dificultando que el usuario identifique ofertas rápidamente.

#### Catálogo y Fichas de Producto
* **Aspectos Positivos:**
  - Inclusión de imágenes referenciales y detalle de la unidad de medida (kilogramos, piezas, paquetes)[cite:7].
* **Áreas de Oportunidad (Fricción UX):**
  - **Falta de retroalimentación inmediata:** Al pulsar "Agregar al carrito", no existe una alerta dinámica (*toast* o notificación emergente de Bootstrap); la confirmación requiere refrescar la vista o depender del contador superior[cite:11].
  - **Indicadores de disponibilidad:** No se visualiza con suficiente contraste si un producto tiene pocas existencias disponibles antes de intentar agregarlo.

#### Carrito y Confirmación de Pedido (`cart.html` / `checkout.html`)
* **Aspectos Positivos:**
  - La disposición tabular del carrito desglosa claramente cantidades, precios unitarios y el subtotal calculado[cite:7].
* **Áreas de Oportunidad (Fricción UX):**
  - El campo de texto para aplicar cupones promocionales se encuentra visualmente aislado del bloque de total a pagar, generando dudas sobre si el descuento se aplicó con éxito o no cumplió con el monto mínimo[cite:7].

### 2.2 Perfil: Administrador (Admin)[cite: 11]

#### Panel de Control y Formularios de Registro (`admin.html`)
* **Aspectos Positivos:**
  - Agrupación funcional para registrar productos, categorías, repartidores y vendedores en un único tablero operativo[cite:7].
* **Áreas de Oportunidad (Fricción UX):**
  - **Densidad de datos:** Las tablas de supervisión general de pedidos carecen de paginación o filtros dinámicos por estado (entregado, pendiente, cancelado)[cite:7].
  - **Validación visual de formularios:** Los mensajes de error en campos obligatorios no cuentan con colores diferenciados o íconos de advertencia estándar que guíen al administrador ante capturas inválidas.

## 3. Matriz Resumen de Usabilidad

| Criterio Evaluado | Estado Actual | Observación Técnica Principal |
| :--- | :--- | :--- |
| **Visibilidad del estado del sistema** | Regular | Se requiere retroalimentación visual inmediata tras interactuar con el carrito[cite:11]. |
| **Consistencia y estándares** | Bueno | Uso adecuado de la paleta de componentes base y botones provistos por Bootstrap[cite:3]. |
| **Prevención y manejo de errores** | Regular | Falta contraste y especificidad en los mensajes al fallar cupones o credenciales[cite:7]. |
| **Jerarquía visual** | Aceptable | Las tarjetas de producto requieren mayor prominencia en precio y llamadas a la acción (*CTA*). |

## 4. Propuesta de Mejora Visual (Para Días 13 y 14)
* **Módulo seleccionado:** Catálogo de Productos y Tarjetas de Abarrotes (`market/templates/`)[cite:3].
* **Mejora concreta:** Rediseñar la tarjeta de producto (*Product Card*) para:
  1. Agregar una insignia visual (*badge* de Bootstrap) con el estado de stock (ej. "En Existencia" / "Agotado")[cite:3].
  2. Mejorar el contraste cromático del botón de adición al carrito.
  3. Integrar un aviso temporal de confirmación visual (*alert/toast*) al completar la acción de compra sin pérdida de contexto[cite:11].