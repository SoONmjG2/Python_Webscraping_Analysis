import os
import sys

current_dir = os.getcwd()
print(f"현재 작업 디렉토리: {current_dir}")

print(f"Python 버전: {sys.version}")

print(f"운영체제: {os.name}")

path_env = os.environ.get('PATH', '')
print(f"환경 변수 PATH 일부: {':'.join(path_env.split(':')[:4])}")  # 앞부분만 표시

full_path = "/Users/username/documents/report.txt"
dir_name = os.path.dirname(full_path)
file_name = os.path.basename(full_path)
name, ext = os.path.splitext(file_name)

print("파일 경로 정보:")
print(f"- 디렉토리: {dir_name}")
print(f"- 파일명: {file_name}")
print(f"- 확장자: {ext}")

file_exists = os.path.exists(full_path)
print(f"파일 존재 여부: {file_exists}")
