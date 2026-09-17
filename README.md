# anpr-uk

UK licence plate recognition. YOLOv8 detects the plate, OpenCV deskews the crop, OCR reads it, and a Flask app serves results backed by SQLite.

## Status

Phase 0 — scaffolding and holdout set.

## Setup

```bash
uv venv --python 3.11 .venv
source .venv/bin/activate
uv pip install -r requirements.txt
pytest
```

## Layout

| Path | Contents |
|---|---|
| `src/detection` | YOLO plate detection |
| `src/ocr` | Crop preprocessing, OCR, UK format validation |
| `src/pipeline` | End-to-end orchestration |
| `src/storage` | SQLite + CSV export |
| `src/web` | Flask app |
| `data/holdout` | Real photos + `ground_truth.csv`, never trained on |
| `scripts` | Evaluation and data-prep entry points |

## Datasets

- Detection: [Roboflow License Plate Recognition](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e) (10k annotated images)
- OCR fine-tune: [UK synthetic plates](https://www.kaggle.com/datasets/saadbinmunir/uk-licence-plate-synthetic-images) (48k, DVLA spacing)
- Evaluation: self-collected holdout, hand-labelled
