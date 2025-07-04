# python-Threads-Lec1-29-JUN-25

Threads

* required to import the **threading** library
* each Thread has the current running name:
    ```
     threading.current_thread().name)
    ```
* to create new thread, it needs the function/proccess to run in it:
    ```
    thread1 = threading.Thread(target=print_numbers)
    ```
* start the thread, need to call the start() function from the new instance
    ```
    thread1.start()
    ```
* the function can receive parameters to send the target function:
    ```
  thread1 = threading.Thread(target=print_numbers, args=(5,))  
  ```
* since each thread works on its own asyncly.
we can control them by waiting for all threads to finish and then continue the programs:
thread1.join()
thread2.join()
* then they will wait for each to complete and will be sync
* lock parameter: # Ensuring only one thread modifies resource at a time:
  *  create lock: ```lock = threading.Lock()```
  * to use it: within the function use the keyword: **with**:
  ```
  def increment():
    global counter
    with lock:  # Ensuring only one thread modifies counter at a time
        for _ in range(10):
            print(threading.current_thread().name, counter)
            counter += 1
  ``` 
  * when the function is completed, it releases the lock, for the other usage
* extra usage of threads:[See thread7.py](./thread7.py) 
  * each thread receives the fetch_content function and the url of the site
  * from each site, get its title, description and first 5 links and prints to the console the results