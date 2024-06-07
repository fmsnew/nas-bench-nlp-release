# NAS-Bench-NLP

Preparation:
1. unzip data/datasets.zip, train\_logs\_single\_run/logs.zip, train\_logs\_multi\_runs/logs.zip, and train\_logs\_wikitext-2/logs.zip;
2. install requirements.txt (currently contains unuseed packages; to be cleaned);
3. optionally, copy models from the dropbox (sample: https://www.dropbox.com/sh/qviytkrlbu2cy5u/AABy59Bb9CpiS7D4osbvY_xva?dl=0, all models: https://www.dropbox.com/scl/fo/4r36x7wqb6gvzcmz8zo61/AIzcRCPZhmzORxJdSI2AdtY?rlkey=516wk0knseuuow45wn4mhy0ak&e=1&dl=0) to the folder models\_weights.

Usage:
* search\_space\_examples.ipynb demonstrates how to generate architectures from the search space;
* to train a model, run script main\_one\_model\_train.py --recepie\_id=<index of the architecture from the list>, where the list of architectures is by defaultin data/recepies\_example.json; logs and final weights will be stored in tmp folder by default (see script argumens for more info); 
* reproduce\_model.ipynb demonstrates how to load and apply the trained model;
* make\_arch\_embedding.ipynb creates graph2vec features for architectures;
* search\_space\_analysis.ipynb reproduces figures from the analysis section in the paper;
* benchmarking\_examples.ipynb shows how NAS methods can be tested based on precomputed results in the logs.




