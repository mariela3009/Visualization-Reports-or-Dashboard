# De los datos a la nube: un dashboard de ventas con Streamlit y despliegue automático

**Autor:** [nombre del integrante]  
**Repositorio público:** https://github.com/mariela3009/Visualization-Reports-or-Dashboard  
**Dashboard público:** [pegar URL real]  
**Video:** [pegar URL real]

> Borrador listo para editar. Publicar después de ejecutar el despliegue, verificar el dashboard y reemplazar los campos pendientes. Cada integrante debe identificar su contribución real y publicar su artículo si así lo exige la asignatura.

## El problema

Una tabla de ventas permite consultar pedidos, pero dificulta detectar tendencias o comparar productos. Este proyecto convierte esa tabla en un dashboard interactivo que responde tres preguntas: ¿cuánto se vendió?, ¿cómo evolucionaron las ventas durante el año? y ¿qué productos aportaron más ingresos?

La aplicación se llama **Ventas 360**. Incluye filtros de periodo, ciudad y categoría; indicadores de ventas, pedidos, unidades y ticket promedio; gráficos y una descarga de los datos filtrados.

## Herramientas y datos

Streamlit construye la interfaz en Python. Pandas transforma y agrupa los registros, mientras Plotly genera gráficos interactivos. Docker describe el entorno de ejecución y GitHub Actions conecta las verificaciones con la publicación en Hugging Face Spaces.

Para que el ejemplo sea reproducible y no dependa de información privada, `data.py` genera 1.200 pedidos ficticios de 2025. Cada registro tiene fecha, producto, categoría, ciudad, unidades e importe en pesos colombianos. La semilla 42 mantiene constantes los datos entre ejecuciones. Las conclusiones del dashboard describen esta simulación, no un negocio real.

## Construcción del dashboard

El primer paso es instalar las dependencias y ejecutar la aplicación:

```bash
pip install -r requirements.txt
streamlit run app.py
```

La barra lateral permite seleccionar categorías, ciudades y fechas. Los filtros se combinan y se aplican antes de calcular los indicadores, de modo que los gráficos y la tabla representan el mismo conjunto de pedidos.

Las ventas totales son la suma de los importes; los pedidos corresponden al número de registros, porque cada fila representa un pedido único; las unidades son la suma de cantidades. El ticket promedio se calcula dividiendo las ventas entre los pedidos.

```python
ventas_totales = vista.venta.sum()
pedidos = len(vista)
ticket_promedio = ventas_totales / pedidos
```

La aplicación comprueba primero que haya resultados. Cuando una selección no contiene pedidos, muestra un mensaje para ajustar los filtros en lugar de calcular indicadores vacíos.

El gráfico de líneas agrupa las ventas por mes para mostrar la evolución. Las barras comparan los ingresos por producto y el gráfico de dona presenta la participación por categoría. Una tabla permite inspeccionar los pedidos; el botón de descarga exporta exactamente la selección visible.

**[Insertar captura del dashboard completo y otra con filtros activos.]**

## Repositorio público

El repositorio incluye `app.py`, `data.py`, `requirements.txt`, `Dockerfile`, las pruebas y el workflow. El README explica cómo instalar, ejecutar y desplegar. Las credenciales no forman parte del código: el token del proveedor se configura como un secreto de GitHub.

**Repositorio:** https://github.com/mariela3009/Visualization-Reports-or-Dashboard.

## Despliegue mediante automatización

El workflow se activa al actualizar `main`, al abrir un pull request o mediante ejecución manual. Primero instala las dependencias y ejecuta pruebas de reproducibilidad de los datos, arranque de la aplicación, selección de categoría y filtros sin resultados.

Si las pruebas pasan y el evento corresponde a la rama principal, el script de despliegue publica los archivos del dashboard en un Space Docker. Se configuran dos valores en GitHub: el secreto `HF_TOKEN`, con permiso de escritura, y la variable `HF_SPACE_ID`, con el formato `usuario/ventas-360`.

Hugging Face construye la imagen a partir del Dockerfile y ejecuta Streamlit en el puerto 7860, configurado también en los metadatos del Space. Para validar el proceso hay que comprobar tanto el workflow como el estado Running y el funcionamiento de la aplicación remota.

**[Insertar captura del workflow exitoso y del Space ejecutándose.]**

Una demostración de la automatización consiste en modificar el título, subir el cambio a `main` y observar su aparición en la aplicación pública después del despliegue. Esa evidencia permite comprobar que las actualizaciones no requieren copiar archivos manualmente al proveedor.

## Resultado del conjunto de datos

Sin aplicar filtros, los datos generados contienen 1.200 pedidos, 3.656 unidades y ventas por **$1.980.275.000 COP**. El ticket promedio es **$1.650.229,17 COP**. Estos valores sirven para comprobar que el dashboard reproduce los cálculos del conjunto simulado; no representan resultados comerciales reales.

## Publicación y resultado

**Aplicación:** [pegar URL pública real].  
**Video del proceso:** [pegar URL pública real].

**[Después de probar: describir qué verificaste en la URL pública, la fecha de verificación y el cambio usado para demostrar el despliegue automático.]**

El proyecto ofrece una ruta reproducible desde una tabla hasta una aplicación de visualización. Como mejoras futuras se pueden incorporar archivos propios, comparaciones entre periodos y validaciones de calidad de datos. Cualquier uso con datos reales exigiría adaptar el modelo y revisar quién puede acceder a la información.

## Mi contribución

**[Cada integrante: explicar su trabajo real en datos, visualización, pruebas, despliegue o documentación; añadir un ejemplo o una decisión propia.]**

## Documentación consultada

- [Streamlit](https://docs.streamlit.io/)
- [Docker Spaces](https://huggingface.co/docs/hub/spaces-sdks-docker)
- [Publicación de archivos con huggingface_hub](https://huggingface.co/docs/huggingface_hub/guides/upload)
- [GitHub Actions](https://docs.github.com/en/actions)
