DATA=/path/to/sentencepiece_tokenized_data
DATADIR=/path/to/preprocessed/data/dir
DIR=/path/to/model/dir
mkdir -p $DATADIR
mkdir -p $DIR

DICT=/path/to/mt5-large/dict
lang_pairs=en_XX-ja_XX
source_lang=en_XX
target_lang=ja_XX
lang_list=/path/to/mbart50.pretrained/ML50_langs.txt
langs=ar_AR,cs_CZ,de_DE,en_XX,es_XX,et_EE,fi_FI,fr_XX,gu_IN,hi_IN,it_IT,ja_XX,kk_KZ,ko_KR,lt_LT,lv_LV,my_MM,ne_NP,nl_XX,ro_RO,ru_RU,si_LK,tr_TR,vi_VN,zh_CN
pretrained_model=path/to/mbart50.pretrained/model.pt

REF=/path/to/reference/data

export MKL_THREADING_LAYER=GNU
fairseq-preprocess\
 --source-lang $source_lang \
 --target-lang $target_lang \
 --trainpref $DATA/train\
 --validpref $DATA/valid \
 --testpref $DATA/test\
 --destdir $DATADIR\
 --thresholdtgt 0 \
 --thresholdsrc 0 \
 --srcdict ${DICT} \
 --tgtdict ${DICT} \
 --workers 70

fairseq-train $DATADIR\
 --finetune-from-model $pretrained_model \
 --save-dir $DIR \
 --encoder-normalize-before --decoder-normalize-before \
 --arch mbart_large --layernorm-embedding \
 --task translation_multi_simple_epoch \
 --sampling-method "temperature" \
 --sampling-temperature 1.5 \
 --encoder-langtok "src" \
 --decoder-langtok \
 --lang-dict "$lang_list" \
 --lang-pairs "$lang_pairs" \
 --criterion label_smoothed_cross_entropy --label-smoothing 0.2 \
 --optimizer adam --adam-eps 1e-06 --adam-betas '(0.9, 0.98)' \
 --lr-scheduler inverse_sqrt --lr 3e-05 --warmup-updates 2500 --max-update 40000 \
 --dropout 0.3 --attention-dropout 0.1 --weight-decay 0.0 \
 --max-tokens 1024  \
 --no-epoch-checkpoints\
 --seed 222


fairseq-generate $DATADIR \
 --path $DIR/checkpoint_best.pt\
 --task translation_multi_simple_epoch \
 --gen-subset test \
 --source-lang $source_lang \
 --target-lang $target_lang\
 --remove-bpe 'sentencepiece'\
 --batch-size 32 \
 --encoder-langtok "src" \
 --decoder-langtok \
 --lang-dict "$lang_list" --lang-pairs "$lang_pairs" > $DIR/test.result

cd $DIR


cat test.result | grep ^H- > test.result.H
cut -f 3 test.result.H > test.result.H.split

python /root/work/H_T_sort.py test.result.H test.result.H.split test.result.H.split

perl /root/work/multi-bleu.perl -lc $REF < test.result.H.split.sort > test.result.bleu

