# preordering-NMT
事前訓練済みのモデルを用い、preorderingと翻訳の試しです。このプロセスにはソース言語、ターゲット言語、対応する単語のアライメントデータが必要です
## 並べ替え文の作成
     python new_make_pre.py -s /path/to/source -t /path/to/target -a /path/to/tgt-src-alignment -o /path/to/output_dir
     
ただし、nttの中日データを使うとき、日本語側の和文数字とかが一つの単語にされていないので、以下のものを使ってください 

     new_make_pre_for_ja.py -s /path/to/source -t /path/to/target -a /path/to/tgt-src-alignment -o /path/to/output_dir
     
## jsonl形式に整形する
     python transform_raw_to_json_mt5.py -train /path/to/original/train/file -valid /path/to/original/valid/file -test /path/to/original/test/file -pre_train /path/to/preordered/train/file -pre_valid /path/to/preordered/valid/file  -pre_test /path/to/preordered/test/file -o /path/to/output/dir
     
## 並べ替えモデルの訓練と推論
huggingfaceのtransformersを使っているので、事前に環境を準備します。

     pip install transformers
     
また、huggingfaceからmt5-small, mt5-base, mt5-largeと mbart-large-50をダウンロードしてください。

### モデルの訓練

     python run_translation.py \ 
     --model_name_or_path ./path/to/mt5_xx \ #事前訓練済みのモデルの置き場
     --do_train \
     --do_eval \
     --source_lang order \
     --target_lang preorder \
     --per_device_train_batch_size 8 \
     --learning_rate 3e-5 \
     --source_prefix "turn order to preorder: " \
     --output_dir ./preorder-from-ja-to-en/model_mt5_xx\ #fine-tuneモデルを出力するディレクトリ指す、model_mt5_xxを実際で使うモデル
     --per_device_eval_batch_size 8 \
     --overwrite_output_dir \
     --max_steps 20000 \ 
     --warmup_steps 2000 \ 
     --num_beams 5 \
     --learning_rate 3e-5 --weight_decay 0.1 \
     --save_steps 1000 
     --eval_steps 1000 
     --load_best_model_at_end --evaluation_strategy steps --gradient_accumulation_steps 4 \
     --predict_with_generate \
     --train_file train_mt5.jsonl \
     --validation_file valid_mt5.jsonl \
     
### モデルの推論

      python run_translation.py \
     --model_name_or_path ./model_mt5-xx/checkpoint-xx \ #eval_bleuが最大のcheckpoint指す
     --do_predict \
     --source_lang order \
     --target_lang preorder \
     --per_device_train_batch_size 8 \
     --learning_rate 3e-5 \
     --source_prefix "turn order to preorder: " \
     --output_dir ./model_mt5-xx/checkpoint-xx/  \
     --per_device_eval_batch_size 8 \
     --overwrite_output_dir \
     --max_steps 20000 \
     --warmup_steps 2000 \
     --num_beams 5 \
     --learning_rate 3e-5 --weight_decay 0.1 --num_train_epochs 50 \
     --save_steps 10000 \
     --eval_steps 1000 \
     --load_best_model_at_end --evaluation_strategy steps \
     --predict_with_generate \
     --train_file train_mt5.jsonl \
     --validation_file valid_mt5.jsonl \
     --test_file test_mt5.jsonl
     
## 翻訳モデルの訓練と推論
翻訳は[fairseq](https://github.com/facebookresearch/fairseq)を使っているので、公式のgithubによるインストールしてください。

     bash mbart_preprocess-train-generate.sh
