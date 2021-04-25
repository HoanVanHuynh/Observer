# Subject behavior is represented by the NewsPublisher class 

class NewsPublisher: # provides you with an interface so that subscribers can work with it
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None 
    
    # The attach() method is used by the Observer to register with NewsPublisher
    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop() 
    
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    
    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update() 
    
    def addNews(self, news):
        self.__latestNews = news 
    
    def getNews(self):
        return 'Got News:', self.__latestNews 
# Let's talk about the Observer interface now:
# In this example, Subscriber represents the Observer.
# It is an abstract base class and represents any other ConcreteObserver.
# Subscriber has the update() method that needs to be implemented by ConcreteObservers.
# Let's us now look at the code for the Subscriber abstract class:
from abc import ABCMeta, abstractmethod 

class Subscriber(metaclass=ABCMeta):
    @abstractmethod 
    def update(self):
        pass 

# We also develped certain classes that represent ConcreteObserver:
# In this case, we have two main observers: 
class SMSSubscriber: # implements the subscriber interface
    def __init__(self, publisher):
        self.publisher = publisher 
        self.publisher.attach(self) 

    def update(self):
        print(type(self).__name__, self.publisher.getNews()) 

class EmailSubscriber: # implements the subscribe interface
    def __init__(self, publisher):
        self.publisher = publisher 
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())    

class AnyOtherSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher 
        self.publisher.attach(self) 
    def update(self):
        print(type(self).__name__, self.publisher.getNews())

news_publisher = NewsPublisher()
observer1 = SMSSubscriber(news_publisher)

if __name__ == '__main__':
    news_publisher = NewsPublisher()
    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_publisher)
    print('\nSubscribers:', news_publisher.subscribers())
    news_publisher.addNews('Hello World!')
    news_publisher.notifySubscribers() 
    print('\nDetached:', type(news_publisher.detach()).__name__)
    