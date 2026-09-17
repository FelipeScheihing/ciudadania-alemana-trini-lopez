# Scripts de OCR usados para verificar transcripciones

Entorno (Windows, ruta corta obligatoria):

```bash
python -m venv C:\ocr\venv && C:\ocr\venv\Scripts\activate
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install "transformers<5" pillow sentencepiece
```

Poner los recortes de renglones en `lines/*.jpg` y correr:

```bash
PYTHONUTF8=1 python run_trocr.py dh-unibe/trocr-kurrent
```

Kraken (entorno aparte):

```bash
pip install kraken
curl -L -o german_handwriting.mlmodel "https://zenodo.org/records/7933463/files/german_handwriting.mlmodel?download=1"
kraken -i lines/obs_1.jpg out.txt ocr -s -m german_handwriting.mlmodel
```

`-s` = el recorte ya es un renglón (no segmentar).
