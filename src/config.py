"""Project-wide constants. No magic numbers elsewhere in the codebase."""

from pathlib import Path
from typing import Final

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent.parent

DATA_DIR: Final[Path] = PROJECT_ROOT / "data"
HOLDOUT_DIR: Final[Path] = DATA_DIR / "holdout"
HOLDOUT_IMAGES_DIR: Final[Path] = HOLDOUT_DIR / "images"
GROUND_TRUTH_CSV: Final[Path] = HOLDOUT_DIR / "ground_truth.csv"

MODELS_DIR: Final[Path] = PROJECT_ROOT / "models"
DETECTION_WEIGHTS: Final[Path] = MODELS_DIR / "detection" / "best.pt"

OUTPUTS_DIR: Final[Path] = PROJECT_ROOT / "outputs"
CROPS_DIR: Final[Path] = OUTPUTS_DIR / "crops"
ANNOTATED_DIR: Final[Path] = OUTPUTS_DIR / "annotated"
REPORTS_DIR: Final[Path] = OUTPUTS_DIR / "reports"

DATABASE_PATH: Final[Path] = PROJECT_ROOT / "anpr.db"

# Detection
DETECTION_CONFIDENCE_THRESHOLD: Final[float] = 0.25
CROP_MARGIN_RATIO: Final[float] = 0.05

# OCR
MIN_CROP_HEIGHT_PX: Final[int] = 64
OCR_CONFIDENCE_THRESHOLD: Final[float] = 0.40
PLATE_CHARACTER_ALLOWLIST: Final[str] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Web
MAX_UPLOAD_BYTES: Final[int] = 10 * 1024 * 1024
ALLOWED_UPLOAD_EXTENSIONS: Final[frozenset[str]] = frozenset({".jpg", ".jpeg", ".png"})

# Detection training
DATASET_YAML: Final[Path] = DATA_DIR / "raw" / "roboflow-lpr-v13" / "data.yaml"
DEFAULT_BASE_MODEL: Final[str] = "yolov8n.pt"
DEFAULT_EPOCHS: Final[int] = 50
DEFAULT_IMAGE_SIZE: Final[int] = 640
DEFAULT_BATCH_SIZE: Final[int] = 16
