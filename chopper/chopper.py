import Queue
import threading

g = threading.local()


class Chopper(object):
    Task = Queue.Queue()
    Pool = []

    def __init__(self, *args, **kwargs):
        self.thread_num = kwargs.get('thread_num', 20)
        self.daemons = kwargs.get('daemons', True)
        self.task_funcs = {}
        self.before_task_funcs = []
        self.after_task_funcs = []

    def before_task(self, f):
        self.before_task_funcs.append(f)

    def after_task(self, f):
        self.after_task_funcs.append(f)

    def put_tasks(self, func, *args, **kwargs):
        self.Task.put((func, args, kwargs))

    def make_thread_pool(self):
        for _ in range(self.thread_num):
            new_thread = threading.Thread(target=self.dispatch)
            new_thread.setDaemon(self.daemons)
            self.Pool.append(new_thread)
            new_thread.start()

    def dispatch(self):
        while True:
            func, args, kwargs = self.Task.get()
            if func == 'stop':
                break
            g.func = {
                'name': func.__name__,
                'params': args,
            }
            g.func.update(kwargs)
            for f in self.before_task_funcs:
                f()
            func(*args, **kwargs)
            for f in self.after_task_funcs:
                f()

    def free_thread_pool(self):
        for _ in range(len(self.Pool)):
            self.put_tasks("stop")

        for existing_thread in self.Pool:
            existing_thread.join()

        del self.Pool[:]

    def run(self):
        self.make_thread_pool()
        self.free_thread_pool()

app = Chopper()
