#!/bin/bash
# Copyright (c) 2020 Ryuichi Yamamoto
# Copyright (c) 2020 Tarou Shirani
# Copyright (c) 2020 oatsu

# wsl run.sh で実行するとPATHが皆無なので登録する
PATH="$HOME/.local/bin:$PATH"

script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
. $script_dir/utils/yaml_parser.sh || exit 1;

# 設定を展開し、変数として記憶する
eval $(parse_yaml "./config.yaml" "config_")

dump_norm_dir=dump/$config_spk/norm

. $config_nnsvs_root/utils/parse_options.sh || exit 1;

# exp name / 音声モデルを判別するための名前
if [ -z ${config_tag:=} ]; then
    expname=${config_spk}
else
    expname=${config_spk}_${config_tag}
fi
expdir=exp/$expname

# 音声出力フォルダを作成
mkdir -p $config_out_wav_dir

# 音声ファイルを生成
nnsvs-synthesis \
    question_path=$config_question_path \
    timelag.checkpoint=$expdir/timelag/best_loss.pth \
    timelag.in_scaler_path=$dump_norm_dir/in_timelag_scaler.joblib \
    timelag.out_scaler_path=$dump_norm_dir/out_timelag_scaler.joblib \
    timelag.model_yaml=$expdir/timelag/model.yaml \
    duration.checkpoint=$expdir/duration/best_loss.pth \
    duration.in_scaler_path=$dump_norm_dir/in_duration_scaler.joblib \
    duration.out_scaler_path=$dump_norm_dir/out_duration_scaler.joblib \
    duration.model_yaml=$expdir/duration/model.yaml \
    acoustic.checkpoint=$expdir/acoustic/best_loss.pth \
    acoustic.in_scaler_path=$dump_norm_dir/in_acoustic_scaler.joblib \
    acoustic.out_scaler_path=$dump_norm_dir/out_acoustic_scaler.joblib \
    acoustic.model_yaml=$expdir/acoustic/model.yaml \
    in_dir=$config_in_lab_dir \
    utt_list=$config_utt_list \
    out_dir=$config_out_wav_dir \
    ground_truth_duration=false \
    sample_rate=$config_sample_rate
