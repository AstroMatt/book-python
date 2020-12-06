*****************
Async Programming
*****************

.. glossary::

    promises
    futures
    coroutines
    awaitable
    queue


Rationale
=========
* ``asyncio`` in stdlib
* ``async`` keyword
* ``await`` keyword
* CPU-bound Concurrency:

    * Using Queues and Multiprocessing
    * Using Futures and Multiprocessing

* I/O-bound Concurrency:

    * Using Queues and Threading
    * Using Futures and Threading



Async Programming
=================
* Source: https://www.youtube.com/watch?v=F19R_M4Nay4
* Source: https://talkpython.fm/async
* By Michael Kennedy

.. figure:: img/sync-execution-sequence.png
    :align: center
    :width: 75%

.. figure:: img/sync-execution-timeline.png
    :align: center
    :width: 75%

.. figure:: img/async-execution-sequence.png
    :align: center
    :width: 75%

.. figure:: img/async-execution-timeline.png
    :align: center
    :width: 75%

.. figure:: img/eventloop-sync.png
    :align: center
    :width: 75%

.. figure:: img/eventloop-async.png
    :align: center
    :width: 75%

.. figure:: img/async-python.png
    :align: center
    :width: 75%

.. figure:: img/async-threads.png
    :align: center
    :width: 75%

.. figure:: img/async-gil.png
    :align: center
    :width: 75%

.. figure:: img/async-anatomy.png
    :align: center
    :width: 75%

.. figure:: img/uvloop-doc.png
    :align: center
    :width: 75%

.. figure:: img/uvloop-using.png
    :align: center
    :width: 75%





*******
AsyncIO
*******

Rationale
=========
* Running asynchronously: 3s + 1s + 1s = bit over 3s [execution time]

.. code-block:: python

    import asyncio


    async def a():
        print('A: started')
        await asyncio.sleep(2)
        print('A: finished')
        return 'a'

    async def b():
        print('B: started')
        await asyncio.sleep(1)
        print('B: finished')
        return 'b'

    async def c():
        print('C: started')
        await asyncio.sleep(3)
        print('C: finished')
        return 'c'


    async def main():
        result = await asyncio.gather(
            a(),
            b(),
            c(),
        )
        print(f'Result: {result}')


    if __name__ ==  '__main__':
        asyncio.run(main())

    # A: started
    # B: started
    # C: started
    # B: finished
    # A: finished
    # C: finished
    # Result: ['a', 'b', 'c']


Running Program
===============
* ``asyncio.run(coro, *, debug=False)``
* Execute the coroutine ``coro`` and return the result
* Takes care of managing the asyncio event loop, finalizing asynchronous generators, and closing the threadpool.
* Cannot be called when another asyncio event loop is running in the same thread.
* Always creates a new event loop and closes it at the end.
* It should be used as a main entry point for asyncio programs, and should ideally only be called once.

.. code-block:: python

    import asyncio


    async def main():
        await asyncio.sleep(1)
        print('hello')


    asyncio.run(main())


Awaitables
==========
* Object is an awaitable if it can be used in an ``await`` expression
* There are three main types of awaitable objects:

    * coroutines,
    * Tasks,
    * Futures.


Sleeping
========
* coroutine ``asyncio.sleep(delay, result=None)``
* Block for delay seconds.
* If result is provided, it is returned to the caller when the coroutine completes

.. code-block:: python

    import asyncio


    async def main():
        result = await asyncio.sleep(1, 'done')
        print(result)


    asyncio.run(main())
    # done


Coroutines
==========
* Python coroutines are awaitables
* Coroutines declared with the async/await syntax is the preferred way of writing asyncio applications. [AsyncioTask]_
* Term 'coroutine' can be used for two closely related concepts [AsyncioTask]_:

    * a coroutine function: an ``async def`` function;
    * a coroutine object: an object returned by calling a coroutine function.

* Python distinguishes between a coroutine function and a coroutine object
* Write a coroutine function by putting ``async`` in front of the ``def``
* Only a coroutine function can use ``await``, non-coroutine functions cannot.
* Calling a coroutine function does not execute it, but rather returns a coroutine object. (This is analogous to generator functions - calling them doesn't execute the function, it returns a generator object, which we then use later.)
* To execute a coroutine object, either:

    * use it in an expression with await in front of it, or
    * use asyncio.run(coroutine_object()), or
    * schedule it with ensure_future() or create_task().

.. code-block:: python

    import asyncio


    async def work():
        return 'done'


    async def main():
        result = await work()
        print(result)


    asyncio.run(main())
    # done


Tasks
=====
* ``asyncio.create_task(coro, *, name=None)``
* Tasks are used to schedule coroutines concurrently
* Wrap the ``coro`` coroutine into a ``Task`` and schedule its execution.
* Return the ``Task`` object:

    * can be used to cancel execution
    * can be awaited until it is complete

* The task is executed in the loop returned by ``get_running_loop()``
* ``RuntimeError`` is raised if there is no running loop in current thread.
* Tasks are used to run coroutines in event loops.
* If a coroutine awaits on a Future, the Task suspends the execution of the coroutine and waits for the completion of the Future.
* When the Future is done, the execution of the wrapped coroutine resumes.
* Use the high-level asyncio.create_task() function to create Tasks.
* Manual instantiation of Tasks is discouraged.


.. code-block:: python

    import asyncio


    async def work():
        return 'done'


    async def main():
        task = asyncio.create_task(work())
        result = await task
        print(result)


    asyncio.run(main())
    # done

.. code-block:: python

    import asyncio


    async def a():
        print(f'A: started')
        await asyncio.sleep(2)
        print(f'A: finished')


    async def b():
        print(f'B: started')
        await asyncio.sleep(1)
        print(f'B: finished')


    async def c():
        print(f'C: started')
        await asyncio.sleep(3)
        print(f'C: finished')


    async def main():
        t1 = asyncio.create_task(a())
        t2 = asyncio.create_task(b())
        t3 = asyncio.create_task(c())
        await t1
        await t2
        await t3


    if __name__ == '__main__':
        asyncio.run(main())

    # A: started
    # B: started
    # C: started
    # B: finished
    # A: finished
    # C: finished

Selected Task methods:

    * class ``asyncio.Task(coro, *, loop=None, name=None)`` - A Future-like object that runs a Python coroutine. Not thread-safe.
    * method ``asyncio.Task.cancel(msg=None)`` - Request the Task to be cancelled. This arranges for a ``CancelledError`` exception to be thrown into the wrapped coroutine on the next cycle of the event loop.
    * method ``asyncio.Task.cancelled()`` - Return ``True`` if the ``Task`` is cancelled.
    * method ``asyncio.Task.done()`` - Return ``True`` if the ``Task`` is done.
    * method ``asyncio.Task.result()`` - Return the result of the ``Task``. If the result isn't yet available, raise ``InvalidStateError``.
    * method ``asyncio.Task.exception()`` - Return the exception of the ``Task``
    * method ``asyncio.Task.add_done_callback(callback, *, context=None)`` - Add a callback to be run when the ``Task`` is done.
    * method ``asyncio.Task.remove_done_callback(callback)`` - Remove callback from the callbacks list.
    * method ``asyncio.Task.set_name(value)`` - Set the name of the ``Task``.
    * method ``asyncio.Task.get_name()`` - Return the name of the ``Task``.


Futures
=======
* Low-level awaitable object
* Represents an eventual result of an asynchronous operation
* When a Future object is awaited it means that the coroutine will wait until the Future is resolved in some other place
* Future objects in asyncio are needed to allow callback-based code to be used with async/await.
* Normally there is *no need* to create Future objects at the application level code.


Running Tasks Concurrently
==========================
* awaitable ``asyncio.gather(*aws, return_exceptions=False)``
* Run awaitable objects in the ``aws`` sequence concurrently.
* If any awaitable in ``aws`` is a coroutine, it is automatically scheduled as a ``Task``.
* If all awaitables are completed successfully, the result is an aggregate list of returned values.
* The order of result values corresponds to the order of awaitables in ``aws``.
* If ``return_exceptions`` is:

    * ``False`` (default): the first raised exception is immediately propagated to the task that awaits on ``gather()``. Other awaitables in the ``aws`` sequence won't be cancelled and will continue to run.
    * ``True``: exceptions are treated the same as successful results, and aggregated in the result list.

* If ``gather()`` is cancelled, all submitted awaitables (that have not completed yet) are also cancelled.
* If any ``Task`` or ``Future`` from the ``aws`` sequence is cancelled, it is treated as if it raised ``CancelledError`` – the ``gather()`` call is not cancelled in this case.
* This is to prevent the cancellation of one submitted Task/Future to cause other Tasks/Futures to be cancelled.

.. code-block:: python

    import asyncio


    async def a():
        print(f'A: started')
        await asyncio.sleep(2)
        print(f'A: finished')
        return 'a'

    async def b():
        print(f'B: started')
        await asyncio.sleep(1)
        print(f'B: finished')
        return 'b'

    async def c():
        print(f'C: started')
        await asyncio.sleep(3)
        print(f'C: finished')
        return 'c'


    async def main():
        result = await asyncio.gather(
            a(),
            b(),
            c(),
        )
        print(f'Result: {result}')


    if __name__ ==  '__main__':
        asyncio.run(main())

    # A: started
    # B: started
    # C: started
    # B: finished
    # A: finished
    # C: finished
    # Result: ['a', 'b', 'c']


Shielding from Cancellation
===========================
* awaitable ``asyncio.shield(aw)``
* Protect an awaitable object from being cancelled.

.. code-block:: python

    import asyncio

    async def work():
        return 'done'


    async def main():
        try:
            res = await shield(work())
        except CancelledError:
            res = None


    asyncio.run(main())


Timeouts
========
* coroutine ``asyncio.wait_for(aw, timeout)``
* Wait for the aw awaitable to complete with a timeout.
* Timeout can either be ``None`` or a ``float`` or int number of seconds to wait for.
* If timeout is ``None``, block until the future completes.
* If a timeout occurs, it cancels the task and raises ``asyncio.TimeoutError``
* If the wait is cancelled, the future ``aw`` is also cancelled.

.. code-block:: python

    import asyncio

    HOUR = 3600


    async def work():
        await asyncio.sleep(HOUR)
        return 'done'


    async def main():
        try:
            await asyncio.wait_for(work(), timeout=1.0)
        except asyncio.TimeoutError:
            print('timeout!')

    asyncio.run(main())
    # timeout!


Wait
====
* coroutine ``asyncio.wait(aws, *, timeout=None, return_when=ALL_COMPLETED)``
* Run awaitable objects in the ``aws`` iterable concurrently and block until the condition specified by return_when.
* The ``aws`` iterable must not be empty.
* ``timeout: float|int`` if specified, maximum number of seconds to wait before returning.
* ``wait()`` does not cancel the futures when a timeout occurs.
* ``return_when`` indicates when this function should return. It must be one of the following constants:

    * ``FIRST_COMPLETED`` - The function will return when any future finishes or is cancelled.
    * ``FIRST_EXCEPTION`` - The function will return when any future finishes by raising an exception. If no future raises an exception then it is equivalent to ALL_COMPLETED.
    * ``ALL_COMPLETED`` - The function will return when all futures finish or are cancelled.

.. code-block:: python

    done, pending = await asyncio.wait(aws)

* Does not raise ``asyncio.TimeoutError``
* ``Futures`` or ``Tasks`` that aren’t done when the timeout occurs are simply returned in the second set (``pending``).

.. code-block:: python

    import asyncio


    async def work():
        return 'done'


    async def main():
        task = asyncio.create_task(work())
        done, pending = await asyncio.wait({task})

        if task in done:
            print('work is done')

    asyncio.run(main())
    # work is done


As Completed
============
* ``asyncio.as_completed(aws, *, timeout=None)``
* Run awaitable objects in the aws iterable concurrently.
* Return an iterator of coroutines.
* Each coroutine returned can be awaited to get the earliest next result from the iterable of the remaining awaitables.
* Raises ``asyncio.TimeoutError`` if the timeout occurs before all Futures are done.

.. code-block:: python

    import asyncio


    async def a():
        print(f'A: started')
        await asyncio.sleep(2)
        print(f'A: finished')
        return 'a'


    async def b():
        print(f'B: started')
        await asyncio.sleep(1)
        print(f'B: finished')
        return 'b'


    async def c():
        print(f'C: started')
        await asyncio.sleep(3)
        print(f'C: finished')
        return 'c'


    async def main():
        work = [a(), b(), c()]
        for coro in asyncio.as_completed(work):
            result = await coro
            print(result)


    if __name__ == '__main__':
        asyncio.run(main())

    # C: started
    # B: started
    # A: started
    # B: finished
    # b
    # A: finished
    # a
    # C: finished
    # c


Running in Threads
==================
* coroutine ``asyncio.to_thread(func, /, *args, **kwargs)``
* Asynchronously run function func in a separate thread.
* Any ``*args`` and ``**kwargs`` supplied for this function are directly passed to func.
* Return a coroutine that can be awaited to get the eventual result of func.
* This coroutine function is intended to be used for executing IO-bound functions/methods that would otherwise block the event loop if they were ran in the main thread.

.. code-block:: python

    import asyncio
    import time


    def work():
        print(f'Work started {time.strftime("%X")}')
        time.sleep(2)  # Blocking
        print(f'Work done at {time.strftime("%X")}')


    async def main():
        print(f'Started main at {time.strftime("%X")}')

        await asyncio.gather(
            asyncio.to_thread(work),
            asyncio.sleep(1))

        print(f'Finished main at {time.strftime("%X")}')


    asyncio.run(main())
    # Started main at 02:42:45
    # Work started 02:42:45
    # Work done at 02:42:47
    # Finished main at 02:42:47


.. note:: Due to the GIL, ``asyncio.to_thread()`` can typically only be used to make IO-bound functions non-blocking. However, for extension modules that release the GIL or alternative Python implementations that don’t have one, ``asyncio.to_thread()`` can also be used for CPU-bound functions.


Introspection
=============
* ``asyncio.current_task(loop=None)`` - Return the currently running Task instance, or None if no task is running.
* ``asyncio.all_tasks(loop=None)`` -  Return a set of not yet finished Task objects run by the loop.
* If loop is ``None``, ``get_running_loop()`` is used for getting current loop.


Event loops
===========
Async code can only run inside an event loop.
The event loop is the driver code that manages the cooperative multitasking.
You can create multiple threads and run different event loops in each of them.
For example, Django uses the main thread to wait for incoming requests, so we can’t run an asyncio event loop there, but we can start a separate worker thread for our event loop.
[cheat]_

An event loop runs in a thread (typically the main thread) and executes all callbacks and Tasks in its thread. While a Task is running in the event loop, no other Tasks can run in the same thread. When a Task executes an await expression, the running Task gets suspended, and the event loop executes the next Task. [pydocmultithreading]_

.. code-block:: python

    import asyncio


    async def work(*args, **kwargs):
        # do stuff...
        return result


    result = asyncio.run(work(1, 2, 3))

Since Python 3.7 there is ``asyncio.run()``. Before you had to ``get_event_loop()`` and then ``run_until_complete()``:

.. code-block:: python

    import asyncio


    async def a():
        print(f'A: started')
        await asyncio.sleep(2)
        print(f'A: finished')


    async def b():
        print(f'B: started')
        await asyncio.sleep(1)
        print(f'B: finished')


    async def c():
        print(f'C: started')
        await asyncio.sleep(3)
        print(f'C: finished')


    async def main():
        await asyncio.gather(
            a(),
            b(),
            c(),
        )


    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())

    # A: started
    # B: started
    # C: started
    # B: finished
    # A: finished
    # C: finished

Queue
=====
* ``asyncio`` queues are designed to be similar to classes of the ``queue`` module.
* Although ``asyncio`` queues are not thread-safe, they are designed to be used specifically in async/await code.
* Note that methods of asyncio queues don’t have a timeout parameter; use`` asyncio.wait_for()`` function to do queue operations with a timeout.

FIFO Queue (first in, first out):

    * class ``asyncio.Queue(maxsize=0)``
    * If maxsize is less than or equal to zero, the queue size is infinite.
    * Unlike the standard library threading queue, the size of the queue is always known and can be returned by calling the qsize() method.
    * ``maxsize`` - Number of items allowed in the queue.
    * ``empty()`` - Return True if the queue is empty, False otherwise.
    * ``full()`` - Return True if there are maxsize items in the queue.
    * coroutine ``get()`` - Remove and return an item from the queue. If queue is empty, wait until an item is available.
    * ``get_nowait()`` - Return an item if one is immediately available, else raise QueueEmpty.
    * coroutine ``join()`` - Block until all items in the queue have been received and processed.
    * coroutine ``put(item)`` - Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
    * ``put_nowait(item)`` - Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
    * ``qsize()`` - Return the number of items in the queue.
    * ``task_done()`` - Indicate that a formerly enqueued task is complete.

Priority Queue:

    * class ``asyncio.PriorityQueue``
    * Retrieves entries in priority order (lowest first).
    * Entries are typically tuples of the form (priority_number, data).

LIFO Queue (last in, first out):
    * class ``asyncio.LifoQueue``
    * Retrieves most recently added entries first.

Exceptions:

    * exception ``asyncio.QueueEmpty`` - Raised when ``get_nowait()`` method is called on an empty queue.
    * exception ``asyncio.QueueFull`` - Raised when ``put_nowait()`` method is called on a queue that has reached its maxsize.

.. code-block:: python

    import asyncio
    import random
    import time


    async def worker(name, queue):
        while True:
            # Get a "work item" out of the queue.
            sleep_for = await queue.get()

            # Sleep for the "sleep_for" seconds.
            await asyncio.sleep(sleep_for)

            # Notify the queue that the "work item" has been processed.
            queue.task_done()

            print(f'{name} has slept for {sleep_for:.2f} seconds')


    async def main():
        # Create a queue that we will use to store our "workload".
        queue = asyncio.Queue()

        # Generate random timings and put them into the queue.
        total_sleep_time = 0
        for _ in range(20):
            sleep_for = random.uniform(0.05, 1.0)
            total_sleep_time += sleep_for
            queue.put_nowait(sleep_for)

        # Create three worker tasks to process the queue concurrently.
        tasks = []
        for i in range(3):
            task = asyncio.create_task(worker(f'worker-{i}', queue))
            tasks.append(task)

        # Wait until the queue is fully processed.
        started_at = time.monotonic()
        await queue.join()
        total_slept_for = time.monotonic() - started_at

        # Cancel our worker tasks.
        for task in tasks:
            task.cancel()
        # Wait until all worker tasks are cancelled.
        await asyncio.gather(*tasks, return_exceptions=True)

        print('====')
        print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
        print(f'total expected sleep time: {total_sleep_time:.2f} seconds')


    asyncio.run(main())
    # worker-0 has slept for 0.26 seconds
    # worker-0 has slept for 0.41 seconds
    # worker-1 has slept for 0.89 seconds
    # worker-2 has slept for 0.98 seconds
    # worker-0 has slept for 0.59 seconds
    # worker-0 has slept for 0.09 seconds
    # worker-0 has slept for 0.11 seconds
    # worker-2 has slept for 0.53 seconds
    # worker-1 has slept for 0.91 seconds
    # worker-1 has slept for 0.21 seconds
    # worker-0 has slept for 0.87 seconds
    # worker-2 has slept for 0.86 seconds
    # worker-2 has slept for 0.11 seconds
    # worker-2 has slept for 0.23 seconds
    # worker-0 has slept for 0.53 seconds
    # worker-1 has slept for 0.89 seconds
    # worker-0 has slept for 0.53 seconds
    # worker-0 has slept for 0.10 seconds
    # worker-2 has slept for 0.86 seconds
    # worker-1 has slept for 0.82 seconds
    # ====
    # 3 workers slept in parallel for 3.74 seconds
    # total expected sleep time: 10.79 seconds


Streams
=======
.. code-block:: python

    import asyncio

    async def tcp_echo_client(message):
        reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
        print(f'Send: {message!r}')
        writer.write(message.encode())
        await writer.drain()
        data = await reader.read(100)
        print(f'Received: {data.decode()!r}')
        print('Close the connection')
        writer.close()
        await writer.wait_closed()

    asyncio.run(tcp_echo_client('Hello World!'))

.. code-block:: python

    import asyncio


    async def handle_echo(reader, writer):
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')
        print(f"Received {message!r} from {addr!r}")
        print(f"Send: {message!r}")
        writer.write(data)
        await writer.drain()
        print("Close the connection")
        writer.close()


    async def main():
        server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)
        addr = server.sockets[0].getsockname()
        print(f'Serving on {addr}')
        async with server:
            await server.serve_forever()

    asyncio.run(main())


Synchronization Primitives
==========================
Mutex Lock:

    * Class ``asyncio.Lock()``
    * Can be used to guarantee exclusive access to a shared resource
    * Not thread-safe.

.. code-block:: python

    lock = asyncio.Lock()

    async with lock:
        # access shared state

Condition object:

    * class ``asyncio.Condition(lock=None)``
    * Not thread-safe.

.. code-block:: python

    cond = asyncio.Condition()

    async with cond:
        await cond.wait()

Semaphore:

    * class ``asyncio.Semaphore(value=1)``
    * Manages an internal counter which is decremented by each ``acquire()`` call and incremented by each ``release()`` call.
    * The counter can never go below zero.
    * When ``acquire()`` finds that it is zero, it blocks, waiting until some task calls ``release()``.

.. code-block:: python

    sem = asyncio.Semaphore(10)

    async with sem:
        # work with shared resource

Event:

    * class ``asyncio.Event()``
    * Can be used to notify multiple asyncio tasks that some event has happened.
    * coroutine ``wait()`` - Wait until the event is set. If the event is set, return ``True`` immediately. Otherwise block until another task calls ``set()``.
    * ``set()`` - Set the event. All tasks waiting for event to be set will be immediately awakened.
    * ``clear()`` - Clear (unset) the event. Tasks awaiting on ``wait()`` will now block until the ``set()`` method is called again.
    * ``is_set()`` - Return ``True`` if the event is set.

.. code-block:: python

    import asyncio


    async def listener(event):
        print(f'Waiting for event')
        await event.wait()
        print(f'Event processed')


    async def main():
        myevent = asyncio.Event()

        # Spawn a Task to wait until 'event' is set.
        handler = asyncio.create_task(listener(myevent))

        # Sleep for 1 second and set the event.
        await asyncio.sleep(1)
        myevent.set()

        # Wait until processing is complete
        await handler


    asyncio.run(main())
    # Waiting for event
    # Event processed


Debug
=====
* By default asyncio runs in production mode.
* Asyncio has a debug mode which can be enabled by:

    * Setting the ``PYTHONASYNCIODEBUG`` environment variable to 1.
    * Using the Python Development Mode.
    * Passing ``debug=True`` to ``asyncio.run()``.
    * Calling ``loop.set_debug()``.

* In addition to enabling the debug mode, consider also:

    * setting the log level of the asyncio logger to ``logging.basicConfig(level=logging.DEBUG)``
    * configuring the warnings module to display ``ResourceWarning`` warnings. One way of doing that is by using the ``-W`` default command line option.

* When the debug mode is enabled:

    * ``asyncio`` checks for coroutines that were not awaited and logs them; this mitigates the 'forgotten await' pitfall.
    * Many non-threadsafe asyncio APIs (such as ``loop.call_soon()`` and ``loop.call_at()`` methods) raise an exception if they are called from a wrong thread.
    * The execution time of the I/O selector is logged if it takes too long to perform an I/O operation.
    * Callbacks taking longer than 100ms are logged.
    * The ``loop.slow_callback_duration`` attribute can be used to set the minimum execution duration in seconds that is considered 'slow'.


Protocol
========
* ``__await__``

Iterator
--------
* ``__aiter__``
* ``__anext__``

.. code-block:: python

    class Reader:
        async def readline(self):
            ...

        def __aiter__(self):
            return self

        async def __anext__(self):
            val = await self.readline()
            if val == b'':
                raise StopAsyncIteration
            return val

Context Manager
---------------
* ``__aenter__``
* ``__aexit__``

.. code-block:: python

    class AsyncContextManager:
        async def __aenter__(self):
            await print('entering context')

        async def __aexit__(self, exc_type, exc, tb):
            await print('exiting context')


3rd Party Libraries
===================

Trio
----
* https://trio.readthedocs.io/en/latest/tutorial.html

.. code-block:: console

    $ pip install trio

.. code-block:: python

    import trio

    async def child1():
        print("  child1: started! sleeping now...")
        await trio.sleep(1)
        print("  child1: exiting!")

    async def child2():
        print("  child2: started! sleeping now...")
        await trio.sleep(1)
        print("  child2: exiting!")

    async def parent():
        print("parent: started!")
        async with trio.open_nursery() as nursery:
            print("parent: spawning child1...")
            nursery.start_soon(child1)

            print("parent: spawning child2...")
            nursery.start_soon(child2)

            print("parent: waiting for children to finish...")
            # -- we exit the nursery block here --
        print("parent: all done!")

    trio.run(parent)

.. code-block:: python
    :caption: Client

    import sys
    import trio

    # arbitrary, but:
    # - must be in between 1024 and 65535
    # - can't be in use by some other program on your computer
    # - must match what we set in our echo server
    PORT = 12345
    # How much memory to spend (at most) on each call to recv. Pretty arbitrary,
    # but shouldn't be too big or too small.
    BUFSIZE = 16384

    async def sender(client_stream):
        print("sender: started!")
        while True:
            data = b"async can sometimes be confusing, but I believe in you!"
            print(f"sender: sending {data!r}")
            await client_stream.send_all(data)
            await trio.sleep(1)

    async def receiver(client_stream):
        print("receiver: started!")
        while True:
            data = await client_stream.receive_some(BUFSIZE)
            print(f"receiver: got data {data!r}")
            if not data:
                print("receiver: connection closed")
                sys.exit()

    async def parent():
        print(f"parent: connecting to 127.0.0.1:{PORT}")
        client_stream = await trio.open_tcp_stream("127.0.0.1", PORT)
        async with client_stream:
            async with trio.open_nursery() as nursery:
                print("parent: spawning sender...")
                nursery.start_soon(sender, client_stream)

                print("parent: spawning receiver...")
                nursery.start_soon(receiver, client_stream)

    trio.run(parent)

.. code-block:: python
    :caption: Server

    import trio
    from itertools import count

    # Port is arbitrary, but:
    # - must be in between 1024 and 65535
    # - can't be in use by some other program on your computer
    # - must match what we set in our echo client
    PORT = 12345
    # How much memory to spend (at most) on each call to recv. Pretty arbitrary,
    # but shouldn't be too big or too small.
    BUFSIZE = 16384

    CONNECTION_COUNTER = count()

    async def echo_server(server_stream):
        # Assign each connection a unique number to make our debug prints easier
        # to understand when there are multiple simultaneous connections.
        ident = next(CONNECTION_COUNTER)
        print("echo_server {}: started".format(ident))
        try:
            while True:
                data = await server_stream.receive_some(BUFSIZE)
                print(f"echo_server {ident}: received data {data!r}")
                if not data:
                    print(f"echo_server {ident}: connection closed")
                    return
                print(f"echo_server {ident}: sending data {data!r}")
                await server_stream.send_all(data)
        # FIXME: add discussion of MultiErrors to the tutorial, and use
        # MultiError.catch here. (Not important in this case, but important if the
        # server code uses nurseries internally.)
        except Exception as exc:
            # Unhandled exceptions will propagate into our parent and take
            # down the whole program. If the exception is KeyboardInterrupt,
            # that's what we want, but otherwise maybe not...
            print(f"echo_server {ident}: crashed: {exc!r}")

    async def main():
        await trio.serve_tcp(echo_server, PORT)

    # We could also just write 'trio.run(serve_tcp, echo_server, PORT)', but real
    # programs almost always end up doing other stuff too and then we'd have to go
    # back and factor it out into a separate function anyway. So it's simplest to
    # just make it a standalone function from the beginning.
    trio.run(main)


Unsync
------
* Library decides which to run, thread, asyncio or sync

.. code-block:: console

    $ pip install unsync

.. code-block:: python

    @unsync
    def my_function():
        pass


References
==========
* https://www.youtube.com/watch?v=Pe3b9bdRtiE
* https://www.youtube.com/watch?v=Xbl7XjFYsN4

.. [AsyncioTask] https://docs.python.org/3/library/asyncio-task.html

.. [cheat] https://cheat.readthedocs.io/en/latest/python/asyncio.html

.. [pydocmultithreading] https://docs.python.org/3/library/asyncio-dev.html#concurrency-and-multithreading
