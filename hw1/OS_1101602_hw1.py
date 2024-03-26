## 多執行緒程式碼

# - thread 1 (print_sleep())
#   - 倒數 10
#   - sleep(0.5)
# - thread 2 (print_num()) 
#   - 倒數 10
#   - sleep(1)



import threading
import time



num_time = 0 
let_time  = 0 

def print_sleep():
    start_time = time.time()  # 記錄開始時間
    for i in range(10):
        print(f"目前 : {threading.current_thread()}"  )
        print(f"Number(sleep): {i}")
        time.sleep(0.5)
    end_time = time.time()  # 記錄結束時間
    global num_time 
    num_time = end_time - start_time  # 執行時間


def print_num():
    start_time = time.time()  # 記錄開始時間
    for j in range(10):
        print(f"目前 : {threading.current_thread()}"  )
        print(f"num: {j}")
        time.sleep(1)
    end_time = time.time()  # 記錄結束時間
    global let_time
    let_time = end_time - start_time  # 執行時間



print(f"目前(main) : {threading.current_thread()}"  )

# 創建兩個執行緒
thread1 = threading.Thread(target=print_sleep)
thread2 = threading.Thread(target=print_num)




# 啟動執行緒
thread1.start()
thread2.start()
print(f"| 執行數量 : {threading.active_count()} |" )


thread1.join() # 等待thread1 結束
thread2.join() # 等待thread2 結束

#等兩者結束才會往下執行 

print("-----------------------------------------" )
print("All threads finished.") 
print("兩者時間比較:")
print(f"Thread 1 (print_sleep): {num_time} seconds")
print(f"Thread 2 (print_num): {let_time} seconds")
print(f"Difference: {abs(num_time - let_time)} seconds")
