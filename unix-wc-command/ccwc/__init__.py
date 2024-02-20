class ccwc():

    def run():
        while True:
            command = input(">")
            if(command == "exit"):
                break
            else:
                first_part = command[0:7]
                filename = command[8:]
                if(len(filename) == 0):
                    filename = input("filename: ") 
                filepath = f"./unix-wc-command/input/{filename}"
                if(first_part == "ccwc -c"):                    
                    bytes = ccwc.read_bytes_size(filepath)
                    print(f"  {bytes} {filename}")
                elif(first_part == "ccwc -l"):
                    lines = ccwc.count_lines(filepath)
                    print(f"  {lines} {filename}")
                elif(first_part == "ccwc -w"):
                    words = ccwc.count_words(filepath)
                    print(f"  {words} {filename}")
                elif(first_part == "ccwc -m"):
                    chars = ccwc.count_chars(filepath)
                    print(f"  {chars} {filename}")
                elif(first_part[0:4] == "ccwc"):
                    filename = command[5:]
                    filepath = f"./unix-wc-command/input/{filename}"
                    bytes = ccwc.read_bytes_size(filepath)
                    lines = ccwc.count_lines(filepath)
                    words = ccwc.count_words(filepath)
                    print(f"  {lines} {words} {bytes} {filename}")

    def read_bytes_size(file_name):
        try:
            with open(file_name, 'rb') as file:
                # Read and print each line in the file
                return len(file.read())
        except FileNotFoundError:
            print("File not found!")
        except Exception as e:
            print("An error occurred:", e)

    def count_lines(file_name):
        try:
            with open(file_name, 'rb') as file:
                line_count = 0
                for line in file:
                    line_count += 1
            return line_count
        except FileNotFoundError:
            print("File not found!")
        except Exception as e:
            print("An error occurred:", e)

    def count_words(file_name):
        try:
            with open(file_name, 'rb') as file:
                word_count = 0
                for line in file:
                    words = line.split()
                    word_count += len(words)
            return word_count
        except FileNotFoundError:
            print("File not found!")
        except Exception as e:
            print("An error occurred:", e)
            
    def count_chars(file_name):
        try:
            with open(file_name, 'rb') as file:
                data = file.read()
                return len(data)
        except FileNotFoundError:
            print("File not found!")
        except Exception as e:
            print(f"An error occurred: {e}")
