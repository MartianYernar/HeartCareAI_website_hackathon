# HeartCareAI — Structural Heart-Defect Detection from Chest X-Rays

A YOLOv8-based classifier that flags structural heart defects (septal "holes") from
chest X-rays, served through a Flask web app for fast, low-cost screening support.

🎥 **Demo:** https://youtu.be/qYvkSio5m1I

---

## Why

Structural heart defects (e.g. septal holes) are typically caught via specialist
imaging review — slow and bottlenecked by access to a cardiologist. HeartCareAI
explores whether a lightweight vision model can flag likely defects directly from
a chest X-ray, fast enough to run as a pre-screening step ahead of specialist review.

## How it works

```
Chest X-ray  →  YOLOv8 classifier (best.pt)  →  defect / no-defect flag  →  Flask web UI
```

- **Model:** YOLOv8 (classification variant), trained on labeled chest X-ray images
- **Inference scripts:** `AI_hd_detect_hole.py` (defect detection), `AI_hd_recognize.py` (recognition)
- **Serving:** Flask web application — upload an X-ray, get a result in the browser
- **Stack:** Python (model + backend), HTML (frontend)

## Status

Built during a hackathon as a working proof of concept. It is **not a diagnostic
tool** — it has not been clinically validated, and is intended to demonstrate the
feasibility of the pipeline, not to be used for real screening decisions.

## Results

> _[Fill in: dataset size (# images), train/val/test split, accuracy / precision /
> recall, and a confusion matrix or example predictions if you have them. This is
> the single highest-value addition you can make to this README — a concrete
> number here is worth more than anything else on the page.]_

## What I'd improve next

- Validate against a held-out clinical dataset with ground-truth labels from a radiologist
- Report calibrated confidence, not just a binary flag
- Compare YOLOv8-cls against a dedicated medical-imaging architecture (e.g. a fine-tuned ResNet/EfficientNet baseline)

## Run it locally

```bash
git clone https://github.com/MartianYernar/HeartCareAI_website_hackathon.git
cd HeartCareAI_website_hackathon
pip install -r requirements.txt   # add this file if it doesn't exist yet
python app.py
```

---
Built by [Yernar Mars](https://yernar-portfolio.vercel.app/) · Aug 2024 – Present
