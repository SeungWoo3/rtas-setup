import pandas as pd
import argparse
import matplotlib.pyplot as plt

# 커맨드 라인 인자 파싱을 위한 설정
parser = argparse.ArgumentParser(description="Plot histograms of execution_time with mean line for two CSV files.")
parser.add_argument('file1', type=str, help='Path to the first CSV file')
parser.add_argument('file2', type=str, help='Path to the second CSV file')
parser.add_argument('bins', type=int, help='bins')

# 인자 파싱
args = parser.parse_args()

# 첫 번째 CSV 파일 읽기
df1 = pd.read_csv(args.file1)
execution_time1 = df1['execution_time'].dropna()  # NaN 제거
execution_time_mean1 = execution_time1.mean()

# 두 번째 CSV 파일 읽기
df2 = pd.read_csv(args.file2)
execution_time2 = df2['execution_time'].dropna()  # NaN 제거
execution_time_mean2 = execution_time2.mean()

bins = args.bins

# 첫 번째 히스토그램 (CPU)
plt.figure(figsize=(10, 8))
plt.hist(execution_time1, bins=bins, color='skyblue', edgecolor='black', alpha=0.7)  # bins 값 증가
plt.axvline(execution_time_mean1, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {execution_time_mean1:.2f}')
plt.title(f'Histogram of Execution Time for {args.file1}')
plt.xlabel('Execution Time')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('histogram_cpu.png', format='png')  # 첫 번째 파일 저장
plt.close()  # 그래프 닫기

# 두 번째 히스토그램 (GPU)
plt.figure(figsize=(10, 8))
plt.hist(execution_time2, bins=bins, color='salmon', edgecolor='black', alpha=0.7)  # bins 값 증가
plt.axvline(execution_time_mean2, color='blue', linestyle='dashed', linewidth=2, label=f'Mean: {execution_time_mean2:.2f}')
plt.title(f'Histogram of Execution Time for {args.file2}')
plt.xlabel('Execution Time')
plt.ylabel('Frequency')
plt.legend()
plt.savefig('histogram_gpu.png', format='png')  # 두 번째 파일 저장
plt.close()  # 그래프 닫기
