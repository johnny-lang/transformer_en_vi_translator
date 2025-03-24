import os
from typing import Counter
import json
from src.config import GetConfig
from torchtext.vocab import build_vocab_from_iterator, vocab
import torch
from collections import Counter

vocab_transform = {}


def load_vocab(path):
    with open(path, "r", encoding="utf-8") as f:
        vocab_dict = json.load(f)

    # Tạo Counter với min_freq=1 để giữ thứ tự từ
    counter = Counter({word: 1 for word in vocab_dict["itos"]})

    new_vocab = vocab(counter, specials=GetConfig()["special_symbols"], special_first=True)

    new_vocab.itos = vocab_dict["itos"]
    new_vocab.set_default_index(GetConfig()["UNK_IDX"])

    return new_vocab

def generate_square_subsequent_mask(sz, device=GetConfig()["DEVICE"]):
    mask = (torch.triu(torch.ones((sz, sz), device=device)) == 1).transpose(0, 1)
    mask = mask.float().masked_fill(mask == 0, float('-inf')).masked_fill(mask == 1, float(0.0))
    return mask

def sequential_transforms(*transforms):
    def func(txt_input):
        for transform in transforms:
            txt_input = transform(txt_input)
        return txt_input
    return func

def tensor_transform(token_ids):
    return torch.cat((torch.tensor([GetConfig()["BOS_IDX"]]), torch.tensor(token_ids), torch.tensor([GetConfig()["EOS_IDX"]])))
