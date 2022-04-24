from MainLogic.Logic import Logic
from MainLogic.LogicObserve import LogicObserve
from WebsiteBrowserController.WebsiteController import WebsiteController

if __name__ == "__main__":
    websiteController = WebsiteController()
    logic = Logic(websiteController)
    logic_observe = LogicObserve(logic)
    logic_observe.start()
