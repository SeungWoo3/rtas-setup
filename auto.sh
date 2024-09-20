# GPU 파워모드 설정
sudo sh -c 'cat test.txt >> /etc/nvpmodel.conf'

# BLIS 빌드
cd ~
git clone https://github.com/flame/blis
cd blis/
./configure auto
make -j $(nproc)
sudo make install

# OpenBLAS 빌드
cd ~
git clone https://github.com/AveesLab/OpenBLAS
cd OpenBLAS
./setup.sh

# rt-max 빌드
cd ~
git clone https://github.com/AveesLab/rt-max
cd rt-max
make -j $(nproc)
./mkdir.sh

# densenet weight 파일 복사
cp ~/rt-max-setting/*.weights ~/rt-max/weights/

# 검증 코드 복사 및 접근 권한 부여
cp ~/rt-max-setting/run.sh ~/rt-max
cd ~/rt-max
chmod +x run.sh

# 검증 코드 실행
./run.sh

# 검증 코드 csv로 그래프 그리기
mkdir -p ~/graph
cp ~/rt-max-setting/graph.py ~/graph
cp ~/rt-max/measure/sequential/densenet201/*.csv ~/graph
cd ~/graph
python3 graph.py sequential_cpu_03core.csv sequential_gpu_03core.csv