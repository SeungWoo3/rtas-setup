./darknet detector sequential cfg/imagenet1k.data \
                   ./cfg/densenet201.cfg \
                   weights/densenet201.weights \
                   data/dog.jpg -core_id 3 -isGPU 1 -num_exp 100
./darknet detector sequential ./cfg/imagenet1k.data \
                   ./cfg/densenet201.cfg \
                   weights/densenet201.weights \
                   data/dog.jpg -core_id 3 -isGPU 0 -num_exp 100