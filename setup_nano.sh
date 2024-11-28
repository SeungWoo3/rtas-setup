sudo apt-get update
# GPU 파워모드 설정
# sudo sh -c 'cat power_nano.txt >> /etc/nvpmodel.conf'

# gfortran
sudo apt-get install gfortran

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

# rtas-resource-scheduling 빌드
cd ~/
git clone https://github.com/AveesLab/rtas-resource-scheduling
cd ~/rtas-resource-scheduling
git fetch origin device/nano
git checkout device/nano
make -j $(nproc)
echo making directories..
./mkdir.sh

# densenet weight 파일 복사
echo copy weights file..
cd ~
git clone https://github.com/SeungWoo3/rtas-weights.git weights
cp -r weights/ rtas-resource-scheduling/

# 검증 코드 복사 및 접근 권한 부여
cd ~/rtas-resource-scheduling
./darknet detector sequential ./cfg/imagenet1k.data ./cfg/densenet201.cfg ./weights/densenet201.weights data/dog.jpg -num_exp 30 -isGPU 1
echo validation
