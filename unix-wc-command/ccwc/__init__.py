class ccwc():

    def run():
        while True:
            command = input(">")
            if(command == "exit"):
                break
            else:
                first_part = command[0:7]
                if(first_part == "ccwc -c"):
                    filename = command[8:]
                    bytes = ccwc.read_bytes_size(f"./unix-wc-command/input/{filename}")
                    print(f"  {bytes} {filename}")
                elif(first_part == "ccwc -l"):
                    filename = command[8:]
                    lines = ccwc.count_lines(f"./unix-wc-command/input/{filename}")
                    print(f"  {lines} {filename}")
                

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