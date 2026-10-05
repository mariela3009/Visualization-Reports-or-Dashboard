# Ventas 360

Repositorio: https://github.com/mariela3009/Visualization-Reports-or-Dashboard

Dashboard público: https://ventas360-mariela3009.streamlit.app/

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

1. Conecta tu cuenta de Streamlit Community Cloud con GitHub, revisando los permisos solicitados.
2. Pulsa Create app y selecciona el repositorio `mariela3009/Visualization-Reports-or-Dashboard`, rama `main`, archivo `app.py`.
3. Selecciona Python 3.11 o posterior en Advanced settings y publica la aplicación.
4. Comprueba la URL pública y guarda el enlace en `entrega/enlaces.txt`.
5. Cada cambio en `main` activa las pruebas de Actions y la actualización automática del proveedor. Son procesos independientes: el despliegue no espera a las pruebas. Para bloquear cambios que no pasen pruebas se requiere protección de rama.
6. Demuestra la automatización con un cambio visible en el título y captura el resultado remoto.

La alternativa Hugging Face Docker requiere PRO según el error obtenido durante el despliegue. Su script se conserva, pero la publicación de Actions queda desactivada salvo que se configure `ENABLE_HF_DEPLOY=true`. El despliegue principal usa Streamlit Community Cloud y no necesita el secreto HF_TOKEN.

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
- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
- https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app
- https://docs.github.com/en/actions

## Estado

Código y materiales preparados. El repositorio está publicado. La aplicación está publicada en Streamlit Community Cloud. El artículo en Dev.to, el video y el envío a Telegram siguen pendientes. Los enlaces pendientes no son evidencia de entrega.
