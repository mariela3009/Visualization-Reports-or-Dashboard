"""Publica únicamente los archivos necesarios para ejecutar el dashboard."""
import os
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil
from huggingface_hub import HfApi

def main():
    token = os.environ["HF_TOKEN"]
    repo_id = os.environ["HF_SPACE_ID"]
    if len(repo_id.split("/")) != 2:
        raise ValueError("HF_SPACE_ID debe tener el formato usuario/nombre-space")
    api = HfApi(token=token)
    api.create_repo(repo_id=repo_id, repo_type="space", space_sdk="docker", private=False, exist_ok=True)
    with TemporaryDirectory() as carpeta:
        for nombre in ["app.py", "data.py", "requirements.txt", "Dockerfile"]:
            shutil.copy2(nombre, carpeta)
        Path(carpeta, "README.md").write_text(
            "---\ntitle: Ventas 360\nemoji: 📊\ncolorFrom: blue\ncolorTo: green\nsdk: docker\napp_port: 7860\n---\n"
            "Dashboard educativo con datos simulados. Desplegado desde GitHub Actions.\n", encoding="utf-8")
        api.upload_folder(repo_id=repo_id, repo_type="space", folder_path=carpeta,
                          commit_message="Despliegue automático desde GitHub Actions")
    print(f"Space: https://huggingface.co/spaces/{repo_id}")

if __name__ == "__main__":
    main()
