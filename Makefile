.PHONY: parse preprocess split features baselines train benchmark analyze test
parse:       ; python scripts/01_parse_data.py
preprocess:  ; python scripts/02_preprocess.py
split:       ; python scripts/03_make_splits.py
features:    ; python scripts/04_build_features.py
baselines:   ; python scripts/05_train_baselines.py
train:       ; python scripts/06_train_dl.py --model $(MODEL)
benchmark:   ; python benchmark/run_benchmark.py
analyze:     ; python scripts/07_analyze.py
test:        ; pytest -q tests
