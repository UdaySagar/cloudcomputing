hadoop fs -rmr /user/vcslstudent/kmerOutput_20mer
hadoop jar /opt/hadoop/contrib/streaming/hadoop-*streaming*.jar \
 -file /home/vcslstudent/Downloads/kmer_count/20mer/20mer_mapper.py\
 -mapper /home/vcslstudent/Downloads/kmer_count/20mer/20mer_mapper.py \
 -file /home/vcslstudent/Downloads/kmer_count/20mer/20mer_reducer.py \
 -reducer /home/vcslstudent/Downloads/kmer_count/20mer/20mer_reducer.py \
 -input /user/vcslstudent/kmerInput/ecoli.fa -output /user/vcslstudent/kmerOutput_20mer
