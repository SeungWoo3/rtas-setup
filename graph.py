import pandas as pd
import argparse
import matplotlib.pyplot as plt

# 커맨드 라인 인자 파싱을 위한 설정
parser = argparse.ArgumentParser(description="Calculate execution_time mean for two CSV files.")
parser.add_argument('file1', type=str, help='Path to the first CSV file')
parser.add_argument('file2', type=str, help='Path to the second CSV file')

# 인자 파싱
args = parser.parse_args()

# 첫 번째 CSV 파일 읽기 및 평균 계산
df1 = pd.read_csv(args.file1)
execution_time_mean1 = df1['execution_time'].mean(skipna=True)

# 두 번째 CSV 파일 읽기 및 평균 계산
df2 = pd.read_csv(args.file2)
execution_time_mean2 = df2['execution_time'].mean(skipna=True)

# 결과 출력
print(f"{args.file1} execution_time avg: {execution_time_mean1}")
print(f"{args.file2} execution_time avg: {execution_time_mean2}")

# 평균값에 대한 막대 그래프 그리기
plt.figure(figsize=(10, 8))  # 세로 크기를 키움
bars = plt.bar([f'{args.file1}', f'{args.file2}'], [execution_time_mean1, execution_time_mean2], color=['skyblue', 'salmon'])
plt.title('Comparison of delays by Jetpack version')
plt.xlabel('Jetpack 5.1.3')
plt.ylabel('Delay')
plt.ylim(0, max(execution_time_mean1, execution_time_mean2) + 30)  # Y축 범위 설정

# 막대 상단에 평균값 텍스트 추가
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 2), ha='center', va='bottom')

# 그래프를 PNG 이미지 파일로 저장
plt.savefig('result.png', format='png')

# 그래프 표시
# plt.show()
