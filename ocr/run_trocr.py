import glob, os, time, json, sys
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import torch
name = sys.argv[1]
t=time.time()
proc = TrOCRProcessor.from_pretrained(name)
model = VisionEncoderDecoderModel.from_pretrained(name).eval()
print(f"modelo {name} cargado en {time.time()-t:.0f}s", flush=True)
out={}
for f in sorted(glob.glob('lines/*.jpg')):
    im = Image.open(f).convert('RGB')
    with torch.no_grad():
        ids = model.generate(proc(images=im, return_tensors='pt').pixel_values, max_new_tokens=64, num_beams=4)
    txt = proc.batch_decode(ids, skip_special_tokens=True)[0]
    out[os.path.basename(f)[:-4]] = txt
    print(f"{os.path.basename(f)[:-4]:18} | {txt}", flush=True)
json.dump(out, open(f"res_{name.replace('/','_')}.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
