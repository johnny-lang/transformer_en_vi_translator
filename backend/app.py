from fastapi import FastAPI
from pydantic import BaseModel
import torch
import uvicorn
from src.model import Seq2SeqTransformer
from src.utils import load_vocab
from src.translate import translate
from src.config import GetConfig
from fastapi.middleware.cors import CORSMiddleware

# Load model configuration
config = GetConfig()

# Load vocabulary
vocab_transform = {
    "en": load_vocab("D:\projects\\translation_app\\backend\\vocab\\vocab_en.json"),
    "vi": load_vocab("D:\projects\\translation_app\\backend\\vocab\\vocab_vi.json")
}

# Initialize model
model = Seq2SeqTransformer(
    num_encoder_layers=config["num_encoder_layers"],
    num_decoder_layers=config["num_decoder_layers"],
    emb_size=config["emb_size"],
    nhead=8,
    src_vocab_size=len(vocab_transform["en"]),
    tgt_vocab_size=len(vocab_transform["vi"]),
    dim_feedforward=512,
    dropout=0.1
)

# Load trained weights
model.load_state_dict(torch.load(config["model_path"], map_location=config["DEVICE"]))
model.eval()

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Hoặc chỉ định frontend cụ thể: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Request model
class TranslationRequest(BaseModel):
    text: str

@app.post("/translate/")
def translate_text(request: TranslationRequest):
    print(f"Input text: {request.text}")
    translated_text = translate(model, request.text, vocab_transform)
    print(f"Output text: {translated_text}")
    return {"translated_text": translated_text}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)