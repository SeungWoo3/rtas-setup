import pandas as pd
import argparse
import matplotlib.pyplot as plt
import numpy as np

# 커맨드 라인 인자 파싱을 위한 설정
parser = argparse.ArgumentParser(description="Calculate execution_time mean, min, max, and std for two CSV files.")
parser.add_argument('file1', type=str, help='Path to the first CSV file')
parser.add_argument('file2', type=str, help='Path to the second CSV file')

# 인자 파싱
args = parser.parse_args()

# 첫 번째 CSV 파일 읽기 및 통계 계산
df1 = pd.read_csv(args.file1)
execution_time_mean1 = df1['execution_time'].mean(skipna=True)
execution_time_min1 = df1['execution_time'].min(skipna=True)
execution_time_max1 = df1['execution_time'].max(skipna=True)
execution_time_std1 = df1['execution_time'].std(skipna=True)

# 두 번째 CSV 파일 읽기 및 통계 계산
df2 = pd.read_csv(args.file2)
execution_time_mean2 = df2['execution_time'].mean(skipna=True)
execution_time_min2 = df2['execution_time'].min(skipna=True)
execution_time_max2 = df2['execution_time'].max(skipna=True)
execution_time_std2 = df2['execution_time'].std(skipna=True)

# 결과 출력
print(f"{args.file1} execution_time avg: {execution_time_mean1}, min: {execution_time_min1}, max: {execution_time_max1}, std: {execution_time_std1}")
print(f"{args.file2} execution_time avg: {execution_time_mean2}, min: {execution_time_min2}, max: {execution_time_max2}, std: {execution_time_std2}")

# 평균, 최소, 최대, 표준편차 값 설정
means = [execution_time_mean1, execution_time_mean2]
mins = [execution_time_min1, execution_time_min2]
maxs = [execution_time_max1, execution_time_max2]
errors = [[mean - min for mean, min in zip(means, mins)],  # 아래로의 에러바
          [max - mean for max, mean in zip(maxs, means)]]  # 위로의 에러바
stds = [execution_time_std1, execution_time_std2]  # 표준편차 값

# 그래프 그리기
plt.figure(figsize=(10, 12))  # 세로 크기를 크게 설정
bars = plt.bar([f'{args.file1}', f'{args.file2}'], 
               means, 
               yerr=errors, 
               capsize=10, 
               color=['skyblue', 'salmon'])

plt.title('Comparison of delays by Jetpack version')
plt.xlabel('Jetpack 5.1.2')
plt.ylabel('Delay')
plt.ylim(0, max(execution_time_max1, execution_time_max2) + 50)  # Y축 범위 설정, 위쪽 공간 확보

# 막대 상단에 평균, min, max 값 텍스트 추가
for i, bar in enumerate(bars):
    y_mean = bar.get_height()
    y_min = mins[i]
    y_max = maxs[i]
    
    # 평균값 텍스트 추가
    plt.text(bar.get_x() + bar.get_width() / 2, y_mean, f"Mean: {round(y_mean, 2)}", ha='center', va='bottom')
    
    # 최소, 최대값 텍스트 추가
    plt.text(bar.get_x() + bar.get_width(), y_max, f"Max: {round(y_max, 2)}", ha='center', va='bottom', color='black')
    plt.text(bar.get_x() + bar.get_width(), y_min, f"Min: {round(y_min, 2)}", ha='center', va='top', color='black')

# 표준편차 값을 막대 하단에 텍스트로 표시
for i, bar in enumerate(bars):
    y_std = stds[i]
    plt.text(bar.get_x() + bar.get_width() / 2, 10, f"Std: {round(y_std, 2)}", ha='center', va='top', color='black')

# 그래프를 PNG 이미지 파일로 저장
plt.savefig('result.png', format='png')

# 그래프 표시
# plt.show()
