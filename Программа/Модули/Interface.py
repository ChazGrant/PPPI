class Interface:
    def showMessage(self):
        """
            Показывает сообщение о каком-то действии, выводя его на экран
        """
        ...

    def renderBackground(self, background_image):
        """
            Отображает задний фон локации
        """
        ...
    
    def renderAtmosphericPhenomenon(self, phenomenon_type: int):
        """
            Вызывает метод отображения атмосферного явления в зависимости от типа явления
            * Всего может быть 3 типа: дождь, туман и солнце
        """
        ...

    def renderRain(self):
        """
            Отображает дождь на локации
        """
        ...

    def renderFog(self):
        """
            Отображает туман на локации
        """
        ...

    def renderSunshine(self):
        """
            Отображает солнце на локации
        """
        ...

    def renderMap(self):
        """
            Отрисовывает карту, на которой игрок может увидеть все локации и где он находится
        """
        ...

    def renderPickupItem(self, pickup_item_type: int, x: int, y: int):
        """
            Отрисовывает предмет сбора, в зависимости от его типа и положения
        """
        ...
