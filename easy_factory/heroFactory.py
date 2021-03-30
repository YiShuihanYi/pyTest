# -*- encoding: utf-8 -*-
from logging import exception

from easy_factory.police import Police
from easy_factory.timo import Timo

class HeroFactory:

    def createHero(self, name):
        if name == "timo":
            return Timo()
        elif name == "police":
            return Police()
        else:
            raise exception("there is no this hero")

heroFactory = HeroFactory()
timo = heroFactory.createHero("timo")
police = heroFactory.createHero("police")
timo.speak_lines()
police.speak_lines()
timo.fight(police)