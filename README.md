# WakaFormer
Japanese sentence segmenter using pre-trained BERT.
It uses 900 training data which were separated by juman++.

# how to use

```python
from wakaformer import WakaFormer
wf = WakaFormer()
wf.wakati("河原研究室は自然言語処理を専門としている研究室です。")
```

# For developers

First, install the following packages required to build the library.

```shell
pip install wheel
pip install setuptools
pip install twine
```

- build
```shell
python setup.py bdist_wheel
```

- test
```shell
python setup.py pytest
```
