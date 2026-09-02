# Implementación de una API REST en Banca

El equipo de desarrollo de una institución financiera necesita implementar una API REST para gestionar cuentas bancarias. La API debe permitir la creación, lectura, actualización y eliminación de cuentas. Además, debe garantizar la consistencia de los datos y manejar adecuadamente los errores y casos límite del dominio. Los actores involucrados son el 'originador de cuentas', el'motor de validación' y el'sistema de persistencia'. La API debe ser idempotente para las operaciones de creación y actualización de cuentas, con un umbral de 5 segundos para la idempotencia. Los modos de falla incluyen timeouts del motor de validación y errores de consistencia en el sistema de persistencia.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | api-rest-con-fastapi-y-sqlalchemy |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición del Modelo de Datos

**Objetivo:** Definir el modelo de datos para las cuentas bancarias, incluyendo atributos y restricciones.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identificar los atributos necesarios para una cuenta bancaria (número de cuenta, saldo, titular, fecha de creación, etc.).
- Establecer las restricciones y validaciones necesarias (saldo positivo, titular válido, etc.).

**Entregable:** Modelo de datos para cuentas bancarias con atributos y restricciones definidas.

<details>
<summary>Pistas de conocimiento</summary>

- Considera las propiedades operativas necesarias para la consistencia y la idempotencia.
- Piensa en los posibles edge cases y cómo manejarlos.

</details>

### Fase 2: Implementación de la API REST

**Objetivo:** Implementar la API REST para gestionar las cuentas bancarias, garantizando la idempotencia y manejando los errores.

**Tiempo estimado:** 4 horas

**Instrucciones:**

- Crear los endpoints para las operaciones CRUD de cuentas bancarias.
- Implementar la lógica para garantizar la idempotencia en las operaciones de creación y actualización.
- Manejar adecuadamente los errores y casos límite del dominio.

**Entregable:** API REST funcional para gestionar cuentas bancarias, con idempotencia garantizada y manejo de errores.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo implementar la idempotencia utilizando claves de operación.
- Piensa en los posibles modos de falla y cómo recuperarte de ellos.

</details>

### Fase 3: Pruebas y Validación

**Objetivo:** Realizar pruebas unitarias y de integración para validar el funcionamiento de la API REST.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Escribir pruebas unitarias para los endpoints de la API.
- Realizar pruebas de integración para validar la idempotencia y el manejo de errores.
- Asegurar que la API cumple con las propiedades operativas y los criterios de aceptación.

**Entregable:** Pruebas unitarias y de integración que validan el funcionamiento de la API REST.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo simular diferentes modos de falla para probar la idempotencia y el manejo de errores.
- Piensa en los criterios de aceptación y cómo validarlos en las pruebas.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una API REST y cuáles son sus componentes principales?
- **paraQueSirve**: ¿Para qué sirve la idempotencia en una API REST y cómo se implementa?
- **comoSeUsa**: ¿Cómo se manejan los errores y casos límite en una API REST?
- **erroresComunes**: ¿Cuáles son los errores comunes al implementar una API REST y cómo se evitan?
- **queDecisionesImplica**: ¿Qué decisiones de diseño implica la implementación de una API REST idempotente?

## Criterios de Evaluacion

- Definición del modelo de datos para cuentas bancarias con atributos y restricciones.
- Implementación de la API REST con idempotencia garantizada y manejo de errores.
- Realización de pruebas unitarias y de integración que validan el funcionamiento de la API REST.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
