from user_entry import user_entry
import time
# import pyximport; pyximport.install()


if __name__ == "__main__":
    start = time.time()
    user_entry()
    print(time.time() - start)