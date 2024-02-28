import sys
import time

def loading_animation(option="cli_ver_simple_bar"):
    start_time = time.time()  # 시작 시간 기록
    
    if option == "cli_ver_simple_bar":
        while True:
            for symbol in "\\|/-":
                sys.stdout.write(f"\rSearching {symbol}")
                sys.stdout.flush()
                time.sleep(0.1)
                
                # 현재 시간이 시작 시간에서 10초 이상 경과하면 종료
                if time.time() - start_time >= 10:
                    return ""
    elif option == "cli_ver_simple_dot":
        while True:
            for i in range(0, 4):
                dots = "." * i
                spaces = " " * (4 - i)
                sys.stdout.write(f"\rSearching{dots}{spaces}")
                sys.stdout.flush()
                time.sleep(0.5)
                
                # 현재 시간이 시작 시간에서 10초 이상 경과하면 종료
                if time.time() - start_time >= 10:
                    return ""
    else:
        return "Invalid options"

if __name__ == "__main__":
    try:
        loading_animation()
    except KeyboardInterrupt:
        print("\nSearch canceled.")
