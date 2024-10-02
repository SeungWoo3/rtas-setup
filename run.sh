mkdir -p ~/graph
cd ~/graph
date +"start at %Y-%m-%d %H:%M:%S" >> log.txt

cp ~/rt-max-setting/graph.py ~/graph
cp ~/rt-max-setting/hist.py ~/graph

sleep 10s

cd ~/rt-max
./darknet detector sequential cfg/imagenet1k.data \
                   ./cfg/densenet201.cfg \
                   weights/densenet201.weights \
                   data/dog.jpg -core_id 3 -isGPU 1 -num_exp 40
./darknet detector sequential ./cfg/imagenet1k.data \
                   ./cfg/densenet201.cfg \
                   weights/densenet201.weights \
                   data/dog.jpg -core_id 3 -isGPU 0 -num_exp 40

# 검증 코드 csv로 그래프 그리기
mv ~/rt-max/measure/sequential/densenet201/*.csv ~/graph
cd ~/graph
python3 graph.py sequential_cpu_03core.csv sequential_gpu_03core.csv
python3 hist.py sequential_cpu_03core.csv sequential_gpu_03core.csv 50

cd ~/graph
date +"end at %Y-%m-%d %H:%M:%S" >> log.txt
