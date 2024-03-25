from abc import ABC, abstractmethod

class WebDriver(ABC):

    @abstractmethod
    def click(self):
        print("Clicking an image")

class ChromeDriver(WebDriver):

    def capturing_screenshot(self):
        print("Capturing Screenshot")

    def click(self):
        print("Clicking an image with Chrome")


obj = ChromeDriver()
obj.capturing_screenshot()