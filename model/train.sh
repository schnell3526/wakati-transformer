# 合計1000件のデータで学習

torchrun --nproc_per_node 1 train.py \
--model_name_or_path cl-tohoku/bert-base-japanese-char-whole-word-masking \
--train_file data.json \
--text_column_name text \
--label_column_name label \
--cache_dir cache \
--output_dir model \
--per_device_train_batch_size 8 \
--seed 42
