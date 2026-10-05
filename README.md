# Ventas 360

Repositorio: https://github.com/mariela3009/Visualization-Reports-or-Dashboard

Dashboard educativo de ventas con Streamlit, Pandas y Plotly. Incluye indicadores, filtros, tres gráficos, tabla y exportación CSV. Utiliza 1.200 pedidos ficticios de 2025, reproducibles con semilla 42; no contiene datos de clientes reales.

## Ejecutar

Requiere Python 3.11 o posterior.

```bash
python -m venv .venv
```

En Windows activa el entorno con `.venv\Scripts\Activate.ps1`; en Linux/macOS usa `source .venv/bin/activate`.

```bash
pip install -r requirements.txt
streamlit run app.py
python -m unittest discover -s tests -v
```

## Repositorio público y automatización

1. Crea un repositorio público en GitHub y sube este proyecto a la rama `main` (incluye `.github/workflows/deploy.yml`). No subas tokens.
2. Crea una cuenta de Hugging Face y un token con permiso de escritura para el Space objetivo.
3. En GitHub abre Settings → Secrets and variables → Actions. Crea el **secret** `HF_TOKEN` con ese token. El workflow ya utiliza `marany/ventas-360`; solo necesitas la **variable** `HF_SPACE_ID` si deseas publicar en otro Space.
4. Ejecuta el workflow desde Actions → Verificar y publicar dashboard → Run workflow, o realiza un push a `main`.
5. El flujo prueba el dashboard y, si pasa, crea o actualiza un Space público Docker. El proveedor construye la imagen; espera a que el Space figure como Running.
6. Comprueba el dashboard en `https://huggingface.co/spaces/marany/ventas-360` desde una ventana privada, después de que el despliegue termine. Esta dirección es el destino configurado; no indica que el Space ya esté publicado.
7. Haz un cambio pequeño en el título y súbelo a `main`. Guarda evidencia del workflow exitoso y del cambio visible: demuestra la automatización.

Los pull requests ejecutan pruebas; la publicación se realiza desde `main`. El token permanece en GitHub Secrets. El script envía solo los archivos de la aplicación. Una subida exitosa no prueba que la construcción remota haya terminado: revisa su estado y funcionamiento.

## Archivos de entrega

`articulo.md`: texto editable para Medium, Dev.to o Hashnode.
`guion_video.md`: narración y acciones para un video de 4:30.
`entrega/enlaces.txt`: registro de URLs reales; inicialmente pendientes.
`entrega/mensaje_telegram.txt`: mensaje para compartir después de publicar.
`entrega/checklist.md`: comprobaciones finales.

## Publicar el artículo en Dev.to

Cuando el repositorio y el dashboard estén públicos, reemplaza los campos entre corchetes en `articulo.md` y añade capturas reales. En Dev.to abre Create Post, usa el título de la primera línea como título y pega el cuerpo del artículo en el editor Markdown. Añade etiquetas como `python`, `streamlit`, `devops` y `tutorial`. Revisa Preview y publica con tu cuenta. Guarda la URL definitiva en `entrega/enlaces.txt`. Cada integrante debe ajustar su autoría y contribución si requiere artículo propio.

## Preparar la entrega

Graba y publica el video siguiendo `guion_video.md`, reemplaza sus enlaces y los del artículo en `entrega/enlaces.txt`, comparte el mensaje de Telegram y vuelve a generar ambos ZIP:

```bash
python scripts/empaquetar.py
```

`proyecto_ventas360.zip` contiene código y materiales. `enlaces_entrega.zip` contiene los enlaces y la checklist. El script incluye la carpeta `.github` y excluye el entorno virtual. Solo entrega el ZIP de enlaces cuando no queden campos pendientes.

## Referencias

- https://docs.streamlit.io/
- https://huggingface.co/docs/hub/spaces-sdks-docker
- https://huggingface.co/docs/huggingface_hub/guides/upload
- https://docs.github.com/en/actions

## Estado

Código y materiales preparados. La creación de cuentas, publicación del repositorio, ejecución remota, artículo, grabación/publicación del video y envío a Telegram requieren completarse con las cuentas del equipo. Los enlaces pendientes no son evidencia de entrega.
