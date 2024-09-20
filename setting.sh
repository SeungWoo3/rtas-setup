cd ~
git clone https://github.com/flame/blis
cd blis/
./configure auto
make -j $(nproc)
sudo make install
cd ~
git clone https://github.com/AveesLab/OpenBLAS
cd OpenBLAS
./setup.sh
cd ~
git clone https://github.com/AveesLab/rt-max
cd rt-max
make -j $(nproc)

mkdir -p ~/rt-max/weights
mv ~/*.weights ~/rt-max/weights/

mkdir -p ~/rt-max/measure/sequential/densenet201

mv ~/run.sh ~/rt-max
cd ~/rt-max
chmod +x run.sh
# ./run.sh

# mkdir -p ~/graph
# mv ~/graph.py ~/graph
# mv ~/rt-max/measure/sequential/densenet201/*.csv ~/graph
# cd ~/graph
# python3 graph.py sequential_cpu_03core.csv sequential_gpu_03core.csv