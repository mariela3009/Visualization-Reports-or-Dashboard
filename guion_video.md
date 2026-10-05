# Guion de video — Ventas 360

**Duración objetivo: 4 minutos y 30 segundos.** Grabar pantalla a 1080p y narración. Ensayar una vez; cortar esperas para mantener el límite de 5 minutos. Mostrar evidencias reales del despliegue. Ocultar tokens y no abrir el contenido de los secretos.

## 0:00–0:25 — Presentación

**Pantalla:** dashboard público y título del proyecto.

**Narración:** «Hola, soy [nombre]. En este video muestro cómo construir un dashboard de ventas con Streamlit, publicar su código en GitHub y automatizar el despliegue en Streamlit Community Cloud. El proyecto se llama Ventas 360 y permite explorar ventas por fecha, ciudad y categoría».

## 0:25–0:55 — Datos y estructura

**Pantalla:** repositorio, archivos `data.py`, `app.py` y `requirements.txt`.

**Narración:** «Usamos mil doscientos pedidos simulados de 2025. Son datos educativos y no pertenecen a una empresa real. Cada pedido contiene producto, categoría, ciudad, fecha, unidades y valor en pesos colombianos. Una semilla fija permite reproducir el conjunto de datos. Pandas prepara la información, Streamlit construye la interfaz y Plotly genera los gráficos».

## 0:55–1:35 — Construcción

**Pantalla:** fragmento de filtros y métricas; terminal con `streamlit run app.py`; aplicación local.

**Narración:** «Instalamos las dependencias y ejecutamos Streamlit. En el código, primero cargamos los datos y creamos los filtros de la barra lateral. Aplicamos todas las selecciones antes de calcular las métricas. Las ventas son la suma de los importes; los pedidos se cuentan por registro; las unidades se suman; y el ticket promedio divide las ventas entre los pedidos. Si no hay resultados, la aplicación muestra un mensaje para ajustar los filtros».

## 1:35–2:15 — Visualizaciones y filtros

**Pantalla:** seleccionar Tecnología y Bogotá, cambiar periodo, recorrer gráficos y descargar CSV.

**Narración:** «El gráfico de líneas muestra la evolución mensual. Las barras comparan las ventas por producto y la dona muestra la participación de cada categoría. Al elegir Tecnología y Bogotá, los indicadores y los gráficos cambian juntos. La tabla permite inspeccionar los registros. También podemos descargar un CSV con los pedidos filtrados, útil para continuar el análisis en otra herramienta».

## 2:15–3:00 — Repositorio y automatización

**Pantalla:** URL pública de GitHub; workflow de pruebas; configuración de repositorio, rama y archivo en Community Cloud.

**Narración:** «El repositorio es público e incluye instrucciones para ejecutar el proyecto. GitHub Actions verifica la aplicación en cada cambio. Las pruebas revisan los datos, el arranque y el comportamiento de los filtros. Streamlit Community Cloud observa main y actualiza el dashboard automáticamente. Las pruebas y el despliegue son independientes; una protección de rama puede exigir que las pruebas pasen antes de integrar cambios».

## 3:00–3:45 — Publicación y evidencia

**Pantalla:** Configuración de Community Cloud, dashboard activo, URL pública y evidencia de un cambio de título publicado automáticamente.

**Narración, después de verificarlo:** «Configuramos el repositorio, la rama main y el archivo app.py. Community Cloud instala las dependencias y ejecuta Streamlit. Aquí se ve la aplicación activa y el dashboard accesible desde su dirección pública. Para demostrar la automatización, cambié el título y actualicé main. Esta ejecución corresponde al cambio y aquí podemos ver el resultado publicado».

**Nota:** preparar esta evidencia antes de grabar; usar un corte de edición para omitir la espera de construcción.

## 3:45–4:15 — Artículo y entrega

**Pantalla:** artículo publicado y sus enlaces; archivo `enlaces.txt` con URLs reales.

**Narración, después de publicar:** «El artículo explica la preparación de datos, la construcción del dashboard y la configuración del despliegue. Incluye el repositorio, la aplicación y este video. Los enlaces se reúnen en un archivo dentro del ZIP de entrega. Después compartimos el artículo y el video en el grupo de Telegram indicado para la actividad».

## 4:15–4:30 — Cierre

**Pantalla:** dashboard y enlaces del proyecto.

**Narración:** «Con este proyecto convertimos datos en una aplicación interactiva y reproducible, con actualizaciones automáticas. Los enlaces están en la descripción del video y en el archivo de entrega. Gracias por ver la demostración».

## Publicación del video

Título: **Dashboard de ventas con Streamlit y despliegue automático | Ventas 360**.

Descripción editable:

«Construcción de un dashboard educativo con Streamlit, Pandas y Plotly, repositorio público en GitHub y despliegue automático en Streamlit Community Cloud con verificaciones en GitHub Actions.

Repositorio: [URL real]
Dashboard: [URL real]
Artículo: [URL real]
Integrante(s): [nombres]
Datos: simulados, 1.200 pedidos de 2025».

Publicar con visibilidad **Pública** y confirmar una duración de máximo 5 minutos. Si cada integrante necesita video propio, adaptar su presentación y contribución.
