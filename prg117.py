from collections import deque
candidates = deque(["Ravi", "Sita", "Arjun"])

print("Initial candidates:", list(candidates))

candidates.append("Priya")
candidates.append("Kiran")

print("After adding at last:", list(candidates))

candidates.appendleft("Anjali")

print("After adding highest priority candidate:", list(candidates))


while candidates:
    removed = candidates.popleft()
    print("Removed:", removed)
    print("Remaining candidates:", list(candidates))