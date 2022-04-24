from functools import wraps
from MainLogic.Logic import Logic
import datetime


def mult_threading(func):
    """Декоратор для запуска функции в отдельном потоке"""
    @wraps(func)
    def wrapper(*args_, **kwargs_):
        import threading
        func_thread = threading.Thread(target=func,
                                       args=tuple(args_),
                                       kwargs=kwargs_)
        func_thread.start()
        return func_thread
    return wrapper


class LogicObserve:
    def __init__(self, logic: Logic):
        self.logic = logic
        self.next_observe_iteration = None
        self.is_start = False

    def start(self):
        self.is_start = True
        self.observe()

    def observe(self):
        self.logic.refresh_data()
        self.next_observe_iteration = self.logic.get_next_distribution()
        self.wait_time_date_to_next_observe_iteration()

    @mult_threading
    def wait_time_date_to_next_observe_iteration(self):
        while self.next_observe_iteration is not None and self.is_start:
            now_datetime = datetime.datetime.now()
            if now_datetime == self.next_observe_iteration:
                self.next_observe_iteration = None
        if self.is_start:
            self.observe()

    def stop(self):
        self.is_start = False


