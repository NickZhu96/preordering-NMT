python /root/work/transformers/examples/pytorch/translation/run_translation.py \
    --model_name_or_path ./ \
    --do_predict \
    --source_lang order \
    --target_lang preorder \
    --per_device_train_batch_size 8 \
    --learning_rate 3e-5 \
    --source_prefix "turn order to preorder: " \
    --output_dir ./model_mt5/checkpoint-20000  \
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


