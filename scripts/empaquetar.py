"""Crea el ZIP de trabajo y el ZIP de enlaces sin incluir credenciales ni entornos."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

raiz = Path(__file__).resolve().parents[1]
archivos = ["app.py", "data.py", "requirements.txt", "Dockerfile", ".gitignore", "README.md",
            "articulo.md", "guion_video.md", ".github/workflows/deploy.yml", "scripts/deploy.py",
            "scripts/empaquetar.py", "tests/test_dashboard.py", "entrega/enlaces.txt",
            "entrega/mensaje_telegram.txt", "entrega/checklist.md"]
with ZipFile(raiz / "proyecto_ventas360.zip", "w", ZIP_DEFLATED) as paquete:
    for nombre in archivos:
        paquete.write(raiz / nombre, arcname=nombre)
with ZipFile(raiz / "enlaces_entrega.zip", "w", ZIP_DEFLATED) as paquete:
    for nombre in ["enlaces.txt", "checklist.md"]:
        paquete.write(raiz / "entrega" / nombre, arcname=nombre)
print("ZIPs creados. Actualiza enlaces.txt con URLs reales y vuelve a ejecutar este script antes de entregar.")
