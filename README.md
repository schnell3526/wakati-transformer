# WakaFormer
Japanese sentence segmenter using pre-trained BERT.
It uses 900 training data which were separated by juman++.

# Install

```shell
pip install git+https://github.com/schnell3526/wakati-transformer
```

# how to use

```python
from wakaformer import WakaFormer
wf = WakaFormer()
wf.wakati("人間と同程度に言語を理解することのできる人工知能システムについて研究しています。")
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
