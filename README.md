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
* ThreadPoolExecutor= is an executor manage all threads from the resource pool :
* with **submit** function, the executor assigns the data (each parameter) for the function according to it's requirements.
  * it schedules each task.
  * it manually submits one task at a time.
  * it returns a Future object immediately.
* instead of the join() function, the executor creates a pool of threads(tasks) according to the provided data.
  * each has a function of result(), makes to wait for the other to complete like join()
* the workers are the number of threads that can run simultaneously; 
once one worker finished the task, it takes the next task from the pool
* the map function sends lists of data to the tasks
* see summery of comparing executor's map and submit functions:
| Feature               | `map`                             | `submit`                                 |
| --------------------- | --------------------------------- | ---------------------------------------- |
| API style             | Functional (`map(func, data)`)    | Imperative (`submit(func, *args)`)       |
| Returns               | Iterator of results               | List of `Future` objects                 |
| Preserves input order | ✅ Yes                             | ❌ Not guaranteed unless managed manually |
| Exception handling    | Raises first exception on `map()` | Per-future via `future.exception()`      |
| Fine-grained control  | ❌ Limited                         | ✅ Full control                           |
| Best for              | Simple batch tasks                | Custom args, monitoring, flexibility     |

```
with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(print_sequence, name, count) for name, count in tasks]

    # Wait for all to complete
    for future in futures:
        future.result()
```
* extra usage of threads:[See thread7.py] (./thread7.py) 
  * each thread receives the fetch_content function and the url of the site
  * from each site, get its title, description and first 5 links and prints to the console the results