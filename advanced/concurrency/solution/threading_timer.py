"""
* Assignment: Wielowątkowość
* Filename: threading_timer.py
* Complexity: easy
* Lines of code to write: 20 lines
* Estimated time: 21 min

English:
    TODO: English Translation

Polish:
    1. Stwórz kolejkę `queue` do której dodasz różne polecenia systemowe do wykonania, np.:
        a. Linux/macOS: `['/bin/ls /etc/', '/bin/echo "test"', '/bin/sleep 2']`,
        b. Windows: `['dir c:\\Users', 'echo "test"', 'type %HOMEPATH%\Desktop\README.txt']`.
    2. Następnie przygotuj trzy wątki workerów, które będą wykonywały polecenia z kolejki
    3. Wątki powinny być uruchamiane jako `subprocess.run()` w systemie operacyjnym z timeoutem równym `TIMEOUT = 2.0` sekundy
    4. Ilość poleceń może się zwiększać w miarę wykonywania zadania.
    5. Wątki mają być uruchomione w tle (ang. `daemon`)

:Extra task:
    1. Wątki powinny być uśpione za pomocą `Timer` przez `DELAY = 5.0` sekund, a następnie ruszyć do roboty
    2. Parametry rozbij za pomocą `shlex`
    3. Użyj logowania za pomocą biblioteki `logging` tak aby przy wyświetlaniu wyników widoczny był identyfikator procesu i wątku.

Hints:
    * Ustaw parametr `shell=True` dla `subprocess.run()`

Tests:
    TODO: Doctests
"""

# Given
TIMEOUT = 2.0
DELAY = 5.0
TODO = ['ping python.astrotech.io',
        'ls -la',
        'echo "hello world"',
        'cat /etc/passwd']

# Solution
import subprocess
from shlex import shlex
from queue import Queue
from threading import Timer


work_queue = Queue()


def run():
    while True:
        cmd = work_queue.get()
        cmd = shlex(cmd)

        try:
            subprocess.run(cmd, timeout=TIMEOUT, shell=True)
        except subprocess.TimeoutExpired:
            print('Timeout')

        work_queue.task_done()


t = Timer(DELAY, run)
t.start()

# Assign tasks
for todo in TODO:
    work_queue.put(todo)

# Wait to complete all tasks
print('Before join')
t.join(timeout=TIMEOUT)
print('After join')

print('Done.')
