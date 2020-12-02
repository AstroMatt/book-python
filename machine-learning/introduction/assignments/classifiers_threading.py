import queue
import threading

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

work_queue = queue.Queue()


iris = load_iris()

# Features
x = iris.data

# Labels
y = iris.target

# Split dataset into test and training set in half
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5)


class Worker(threading.Thread):
    daemon = True

    def run(self):
        while True:
            # Remove and return an item from the queue.
            job = work_queue.get()

            # Execute work
            job.fit(x_train, y_train)
            predictions = job.predict(x_test)

            result = accuracy_score(y_test, predictions)
            print(result, job)
            print('\n')

            # Indicate that a formerly enqueued task is complete.
            work_queue.task_done()


def spawn_worker(how_many):
    for i in range(how_many):
        Worker().start()


if __name__ == '__main__':
    spawn_worker(3)

    for todo in [
        KNeighborsClassifier(n_neighbors=1),
        KNeighborsClassifier(n_neighbors=5),
        DecisionTreeClassifier(),
    ]:
        work_queue.put(todo)

    # wait to complete all tasks
    work_queue.join()
