from dataclasses import dataclass


@dataclass
class Event:
    name: str
    subscribers: set = ()

    def __post_init__(self):
        self.subscribers = set(self.subscribers)

    def call(self, *args, **kwargs):
        for subscriber in self.subscribers:
            subscriber(*args, **kwargs)
    __call__ = call

    def register(self, function):
        self.subscribers.add(function)
        return self

    def unregister(self, function):
        self.subscribers.remove(function)
        return self


class MessageBroker:
    @staticmethod
    def register(event_name):
        if not hasattr(MessageBroker, event_name):
            setattr(MessageBroker, event_name, Event(event_name))
        return getattr(MessageBroker, event_name).register



@MessageBroker.register('on_echo')
def echo(*args, **kwargs):
    print(locals())


if __name__ == '__main__':
    MessageBroker.on_echo()
    MessageBroker.on_echo(1, 2, 3)
    MessageBroker.on_echo(a=1, b=2, c=3)
    MessageBroker.on_echo(1, 2, 3, a=1, b=2, c=3)
