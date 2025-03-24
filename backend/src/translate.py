import torch
import torch.nn as nn
from src.config import GetConfig
from src.utils import load_vocab, generate_square_subsequent_mask

def greedy_decode(model, src, src_mask, max_len, start_symbol):
    max_len = min(2 * src.shape[0], 50)
    config = GetConfig()
    src = src.to(config["DEVICE"])
    src_mask = src_mask.to(config["DEVICE"])

    memory = model.encode(src, src_mask)
    ys = torch.ones(1, 1).fill_(start_symbol).type(torch.long).to(config["DEVICE"])
    for i in range(max_len-1):
        memory = memory.to(config["DEVICE"])
        tgt_mask = (generate_square_subsequent_mask(ys.size(0))
                    .type(torch.bool)).to(config["DEVICE"])
        out = model.decode(ys, memory, tgt_mask)
        out = out.transpose(0, 1)
        prob = model.generator(out[:, -1])
        _, next_word = torch.max(prob, dim=1)
        next_word = next_word.item()

        ys = torch.cat([ys,
                        torch.ones(1, 1).type_as(src.data).fill_(next_word)], dim=0)
        if next_word == config["EOS_IDX"]:
            break
    return ys

def translate(model: nn.Module, src_sentence: str, vocab_transform):
    config = GetConfig()
    model.eval()
    src = torch.tensor([vocab_transform[config["SRC_LANGUAGE"]][word] for word in src_sentence.split()]).view(-1, 1)
    src_mask = torch.zeros(src.shape[0], src.shape[0]).type(torch.bool)
    tgt_tokens = greedy_decode(model, src, src_mask, max_len=src.shape[0] + 5, start_symbol=config["BOS_IDX"]).flatten()
    return " ".join(vocab_transform[config["TGT_LANGUAGE"]].lookup_tokens(list(tgt_tokens.cpu().numpy()))).replace("<bos>", "").replace("<eos>", "")
