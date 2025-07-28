logs = [
    "2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다",
    "2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패",
    "2025-07-20 11:00:00 - INFO - 시스템 정상 작동 중",
    "2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음",
    "2025-07-20 12:00:00 - WARNING - 디스크 공간 부족",
]

with open("system.log", "w", encoding="utf-8") as f:
    for log in logs:
        f.write(log + "\n")

print("로그 파일이 생성되었습니다.\n")

def print_logs_by_level(filename, level):
    print(f"{level} 레벨 로그들:")
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if f" - {level} - " in line:
                print(line.strip())
    print()

print_logs_by_level("system.log", "ERROR")
print_logs_by_level("system.log", "WARNING")
