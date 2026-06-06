log = list(map(int, input("Enter log status codes separated by space: ").split()))

last_5_logs = log[-5:]
has_500_error = 500 in last_5_logs

print("Last 5 log entries:",log[-5:])
print("500 error found:", {has_500_error})