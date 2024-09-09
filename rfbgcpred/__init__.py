# Mark this as a package
from .cli import main
from .model_utils import load_models, predict_bgc
from .sequence_extraction import extract_sequence_from_fasta, extract_sequence_from_gbk
