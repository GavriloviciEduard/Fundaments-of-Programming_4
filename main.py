from infrastructure.passengers_repo import PassengersRepo
from infrastructure.planes_repo import PlanesRepo
from application.app_controller import AppController
from ui.console import PPUI

pln_r=PlanesRepo()
pass_r=PassengersRepo()
c=AppController(pln_r,pass_r)
ui=PPUI(c)
ui.start()

