# Slice list into 3 equal chunks and reverse each chunk
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list", sample_list)
'''chunk1 = sample_list[:3]
print("Chunk 1", chunk1)
chunk1.reverse()
print("After reversing it", chunk1)
chunk2 = sample_list[3:6]
print("Chunk 2", chunk2)
chunk2.reverse()
print("After reversing it", chunk2)
chunk3 = sample_list[6:]
print("Chunk 3", chunk3)
chunk3.reverse()
print("After reversing it", chunk3)'''

length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size

# run loop 3 times
for i in range(1, chunk_size + 1):
    # get indexes
    indexes = slice(start, end)
    
    # get chunk
    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)
    
    # reverse chunk
    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk_size
