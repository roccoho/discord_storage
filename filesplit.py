import os

MAX_FILESIZE = 8388294
directory = os.fsencode("files")

for file in os.listdir(directory):
    print(file)

# get filename, save chunks by numbered filename, recombine chunks back to same filename

    def chunks(file_name, size=MAX_FILESIZE):
        with open(file_name, mode='rb') as f:
            i = 0
            while chunk := f.read(size):
                save_chunk(chunk, i)
                i+=1

    def save_chunk(chunk, i):
        with open(f"splitfiles/temp_{i}.mp4","wb") as f:
            f.write(chunk)

chunk_list = []
for file in os.scandir("splitfiles"):  
    with open(file.path, mode='rb') as chunk:
        chunk_list.append(chunk.read())
 
recombined_file = b''.join(chunk_list)
    
with open(f"recombinedfiles/temp.mp4","wb") as f:
    f.write(recombined_file)