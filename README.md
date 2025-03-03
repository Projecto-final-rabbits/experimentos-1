# Proyecto de Experimentos - CCP

## 1. Estructura de Carpetas

El proyecto sigue la siguiente estructura de carpetas:

```
experimento/
│-- .gitignore
│-- docker-compose.yml
│-- cloud-key.json  # Archivo de credenciales necesario
│-- bodega_experimento/  # Microservicio de Bodega
│-- ventas_experimento/  # Microservicio de Ventas
```

## 2. Instrucciones para Montar Docker Compose

Para levantar los servicios requeridos (`bodega_experimento` y `ventas_experimento`), sigue estos pasos:

1. Asegúrate de tener Docker y Docker Compose instalados en tu sistema.
2. Configura las variables de entorno necesarias en cada microservicio (`bodega_experimento` y `ventas_experimento`).
3. Coloca el archivo `cloud-key.json` en la raíz del proyecto, ya que es requerido para la autenticación.
4. Ejecuta el siguiente comando desde la raíz del proyecto:

   ```sh
   docker-compose up -d
   ```

Esto iniciará los contenedores en segundo plano.

## 3. Endpoints para Realizar los Experimentos

A continuación, se listan los endpoints principales de los servicios involucrados en los experimentos:

### 📦 Servicio de Bodega

- **Crear Producto:**
  ```http
  POST /product/
  ```
  *Descripción:* Crea un nuevo producto en el sistema.

- **Consultar producto desde bodega:**
  ```http
  GET /products/{id}
  ```
  *Descripción:* Permite consultar un producto en bodega por id.

### 🛒 Servicio de Ventas

- **Crear una venta:**
  ```http
  POST /sell_product/
  ```
  *Descripción:* Registra una nueva venta en el sistema.

- **Consultar ventas:**
  ```http
  GET /products/{id}
  ```
  *Descripción:* Permite consultar un producto en bodega por id desde el modulo de ventas.

## Consideraciones Adicionales

- Es obligatorio configurar las **variables de entorno** de cada microservicio antes de ejecutarlos.
- Se requiere el archivo `cloud-key.json` en la raíz del proyecto para la autenticación.
- El microservicio `compras_experimento` **no** se utilizará en estos experimentos y no se incluye en `docker-compose.yml`.
