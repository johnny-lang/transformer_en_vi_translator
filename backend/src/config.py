import torch 

def GetConfig():
    return {
        "num_encoder_layers": 4,
        "num_decoder_layers": 4,
        "emb_size": 512,
        "batchsize": 64,
        "nhead": 8,
        "dropout": 0.10,
        "dim_feedforward": 512,
        "DEVICE": "cuda" if torch.cuda.is_available() else "cpu",
        "special_symbols": ['<unk>', '<pad>', '<bos>', '<eos>'],
        "UNK_IDX": 0,
        "PAD_IDX": 1,
        "BOS_IDX": 2,
        "EOS_IDX": 3,
        "SRC_LANGUAGE": "en",
        "TGT_LANGUAGE": "vi",
        "model_path": "transformer_en_to_vi_model_30_epochs.pt",
    }