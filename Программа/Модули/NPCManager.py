"""
    Неигровой персонаж

    Класс описывает неигрового персонажа, с которым пользователь может взаимодействовать

    @author     ChazGrant
    @version    1.0
    @todo       Реализовать все методы
"""
from typing import List


class NPCMood:
    ...


class NPC:
    def __init__(self, has_ash, ash_type, has_plot, health_points):
        """
            Конструктор класса

            Создаёт неигрового персонажа, создавая параметры, переданные в конструктор

            Аргументы:
                has_ash: 
                ash_type: 
                has_plot: 
                health_points: 
        """
        ...

    def getNPCReplics(self, player_replic: str) -> List[str]:
        """
            Получить реплики NPC

            Возвращает реплики неигрового персонажа, в зависимости от того что сделал игрок

            Аргументы:
                player_replic: Реплика, которую выбрал пользователь
            
            Возвращает:
                Список реплик, которые может ответить NPC
        """
        ...

    def advanceThePlot(self) -> int:
        """
            Продвинуться по сюжету

            Продвигает сюжет неигрового персонажа, давая ему другие реплики и возможно меняя его настроение

            Возвращает:
                Новый уровень текущего сюжета
        """
        ...

    def getNPCMood(self) -> NPCMood:
        """
            Получить настроение NPC

            * Оно может быть либо дружелюбным либо враждебно настроенным

            Возвращает: 
                Настроение неигрового перонажа
        """
        ...

    def NPCHasAsh(self) -> bool:
        """
            NPC имеет пепел

            Возвращает наличие пепла у неигрового персонажа
            * Пепел нужен для того чтобы открывать новые предметы в магазине
            * Пепел выпадает только при смерти неигрового персонажа

            Возвращает:
                Наличие пепла у неигрового персонажа
        """
        ...
