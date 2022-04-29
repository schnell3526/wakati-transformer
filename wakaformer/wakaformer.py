from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch
import subprocess

class WakaFormer():
    def __init__(self):
        self.model = AutoModelForTokenClassification.from_pretrained("schnell3526/wakaformer")
        self.tokenizer = AutoTokenizer.from_pretrained("schnell3526/wakaformer", use_fast=True)
    
    def wakati(self, text):
        input = self.tokenizer(text, return_tensors="pt")
        output = self.model(**input)
        res = torch.argmax(output.logits, dim=-1)[:,1:-1].squeeze(0)

        ans = ""
        for c, l in zip(text, res):
            if l == 1 or l == 3:
                ans += f'{c} '
            else:
                ans += c
        return ans.rstrip()

class Jumanpp():
    def __init__(self):
        self.args = ["jumanpp", "--segment"]
    
    def wakati(self, text):
        res = subprocess.run(self.args, input=text, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return res.stdout