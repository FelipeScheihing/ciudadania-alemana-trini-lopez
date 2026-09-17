# Herramientas para leer manuscrito alemán antiguo (Kurrent / Sütterlin)

Verificado el 2026-09-17 (modelos confirmados vía API de Hugging Face, Zenodo y GitHub).

Los documentos del caso están en **Kurrent del siglo XIX** (matrículas consulares, índices de Hamburgo,
bautismo de Lübeck). Sütterlin es posterior (1911–1941). Conviene elegir modelos entrenados en siglo XIX.

## Recomendación rápida

| Si quieres… | Usa |
|---|---|
| Resultado bueno sin programar | **Transkribus** (web), modelo *German Kurrent* o *German_Kurrent_XIX_pylaia* |
| Gratis, local, en Python | **TrOCR `dh-unibe/trocr-kurrent`** (Hugging Face) |
| Pipeline open source completo (segmentar página + reconocer) | **Kraken** + modelo de Zenodo |
| Leer pocas entradas puntuales | Claude u otro modelo con visión, con recortes ampliados (así se leyó la matrícula N° 687) |

## 1. Transkribus — la opción más madura

- Plataforma de READ-COOP, estándar en archivos europeos. Web: https://www.transkribus.org
- Modelos públicos relevantes:
  - **German Kurrent** — Kurrent, Sütterlin y Fraktur, siglos XVII–XX.
  - **German_Kurrent_XIX_pylaia** — específico del siglo XIX.
  - **Transkribus Early Kurrent M1** — siglos XVI a comienzos del XIX.
- Costo: plan gratuito con **50 créditos/mes**; manuscrito = 1 crédito por página. Planes pagos desde
  ~€8,25/mes. La API existe (con descuento en créditos) pero en planes de organización.
- Ventaja: segmenta la página sola (tablas, columnas) y permite corregir y reentrenar.
- Contra: no es local ni open source; los documentos se suben a su servidor.

## 2. TrOCR Kurrent (Hugging Face) — gratis y local

- **`dh-unibe/trocr-kurrent`** — Universidad de Berna (Widmer, Hodel). Kurrent **siglo XIX**. Licencia MIT.
  ~5.900 descargas, actualizado ago-2026. https://huggingface.co/dh-unibe/trocr-kurrent
- `dh-unibe/trocr-kurrent-XVI-XVII` — misma familia, siglos XVI–XVIII (no es nuestra época).
- `fhswf/TrOCR_german_handwritten` — manuscrito alemán moderno, no histórico.
- Limitación: **reconoce líneas, no páginas**. Hay que recortar cada renglón antes (a mano, con Kraken, o
  con un segmentador).

Uso mínimo:

```python
# pip install transformers torch pillow
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image

proc = TrOCRProcessor.from_pretrained("dh-unibe/trocr-kurrent")
model = VisionEncoderDecoderModel.from_pretrained("dh-unibe/trocr-kurrent")

linea = Image.open("renglon.jpg").convert("RGB")   # una sola línea de texto
ids = model.generate(proc(images=linea, return_tensors="pt").pixel_values, max_new_tokens=128)
print(proc.batch_decode(ids, skip_special_tokens=True)[0])
```

## 3. Kraken — pipeline completo open source

- `pip install kraken` (versión actual 7.1.1; requiere Python 3.10+). Hace segmentación de página y
  reconocimiento.
- Modelos:
  - **Zenodo 7933463** — "HTR model for German manuscripts trained from several datasets"
    (archivo `german_handwriting.mlmodel`). https://zenodo.org/records/7933463
  - **GitHub `MGJamJam/htr_german_kurrent_model`** — 3 modelos Kraken + 1 Calamari, Kurrent siglo XIX
    (tesis de licenciatura, 2025), con extractor de líneas y evaluación.
  - Datos de entrenamiento siglo XIX: **Zenodo 17252677** (9.317 líneas) por si se quiere afinar un modelo.

Uso mínimo:

```bash
pip install kraken
kraken -i pagina.jpg salida.txt segment -bl ocr -m german_handwriting.mlmodel
```

## Prueba real sobre nuestros documentos (2026-09-17)

Se corrieron los dos modelos gratuitos, localmente y en CPU, sobre 20 renglones recortados de la matrícula
N° 687 y del índice de defunciones de Hamburgo. Scripts en `ocr/`.

| Modelo | Rendimiento en estos documentos |
|---|---|
| **TrOCR `dh-unibe/trocr-kurrent`** | **El mejor.** Leyó bien nombres, fechas y frases completas ("den 5t. Jenner 1901. auf Grund", "eingetragen", "in Conzeptien unter Nr. 53", "Vermehren"). Detectó que la palabra era *Schutzscheines* y corrigió una lectura humana. Falla con números sueltos (leyó 887 por 187) y con topónimos (Lübeck → "Jubel"). |
| **Kraken + modelo Zenodo 7933463** | Mucho más débil en este Kurrent (modelo general, no específico del siglo XIX). Útil solo como desempate: acertó el número "187" donde TrOCR falló. |

Lecciones:
- **Renglón completo > palabra suelta.** Ambos modelos empeoran mucho con recortes de una sola palabra.
- **Números y nombres propios: siempre verificar a ojo** con ampliación. Ningún modelo leyó bien "492" ni "9/2".
- Usar los dos modelos y comparar: cuando coinciden, la lectura es sólida; cuando difieren, ampliar la imagen.
- Instalación en Windows: crear el entorno virtual en una ruta corta (ej. `C:\ocr`), porque rutas largas rompen
  la instalación de `pip` (error WinError 206).

## Consejos prácticos para estos documentos

- **Recortar antes de reconocer.** Las matrículas son tablas de doble página; el reconocimiento funciona
  mucho mejor columna por columna o renglón por renglón.
- **Nombres propios y abreviaturas** ("Eingetr.", "Kais.", "geb.", "Wwe.") son donde más fallan todos los
  modelos. Siempre revisar a mano esos campos.
- **Nunca usar la transcripción automática como prueba.** Lo que va al BVA es la copia certificada del
  documento; la transcripción es solo para entender qué pedir.
