# GPU 파워모드 설정
sudo sh -c 'cat power.txt >> /etc/nvpmodel.conf'

# gfortran
# sudo apt-get install gfortran

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
echo making directories..
./mkdir.sh

# densenet weight 파일 복사
echo copy weights file..
mkdir -p ~/rt-max/weights/
cp ~/rt-max-setting/*.weights ~/rt-max/weights/

# 검증 코드 복사 및 접근 권한 부여
cp ~/rt-max-setting/run.sh ~/rt-max
cd ~/rt-max
chmod +x run.sh
echo ready to run!
