
for i in $1
do
	echo "Loop $i device: $2; dataset: $3"
    python3 main_one_model_train.py\
     --dataset_path data/$3\
     --logs_path tmp/$3_logs \
     --recepies_list_path data/top_recipes.json\
     --recepie_id $i\
     --device_id $2

done




# for i in $1
# do
# 	echo "Loop $i device: $2"
#     python3 main_one_model_train.py\
#      --dataset_path data/hywiki\
#      --logs_path tmp/hywiki_logs \
#      --recepies_list_path data/top_recipes.json\
#      --recepie_id $i\
#      --device_id $2

# done


