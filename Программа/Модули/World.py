"""
    Окружающий мир

    Класс описывает онлайн функцию, где игроки сражаются друг против друга

    @author     ChazGrant
    @version    1.0
    @todo       Реализовать все методы
"""
from typing import List, Union


class Achievement:
    ...


class Player:
    ...


class Object:
    ...


class StatusType:
    ...


class Texture:
    ...

class World:
    def acquireAchievemnt(self) -> Achievement:
        """
            Получение достижения

            Проверяет достигнуты ли условия достижения и выдаёт достижение игроку

            Возвращает:
                Достижение которое будет получено
        """
        ...

    def checkCollisions(self, player: Player, object: Object) -> Object:
        """
            Проверка коллизий

            Проверяет столкнулась ли модель игрока с моделью данного объекта

            Аргументы:
                player - Объект игрока, с которым проверяются коллизии
                object - Любой объект, с которым игрок должен столкнуться
            Возвращает:
                Объект, с которым произошла коллизия
        """
        ...

    def sinkInPuddle(self, puddle_type: int) -> List[List[Union[StatusType, int]]]:
        """
            Тонуть в болоте

            Наносит урон игроку, в зависимости в каком болоте находится игрок
            * Лава наносит огненный урон
            * Болото накладывает статус отравления по достижению определённого уровня отравления

            Аргументы:
                puddle_type - тип болота, в котором находится игрок
                * 1 - Лава
                * 2 - Ядовитое болото
                * 3 - Болото гнили
                * 4 - Ледяное болото
            Возвращает:
                Какой статус накладывается и сколько урона он наносит
        """
        ...

    def createEnemy(self, enemy_type: int, is_elite: bool) -> Object:
        """
            Создание противника

            Создаёт противника, в зависимости от его типа и того является ли он элитным

            Аргументы:
                enemy_type - тип врага
                * 1 - Обычный рядовой
                * 2 - Солдат со щитом
                * 3 - Солдат с луком
                * 4 - Гигант
                is_elite - является ли враг элитным
                * Если является то его здоровье увеличивается на 30% и урон на 10%
        """
        ...

    def createBonfires(self) -> List[List[int]]:
        """
            Создание костров

            Создаёт все костры в текущей локации

            Возввращает:
                Список позиций костров. Каждый список содержит x, y и z
        """
        ...

    def createWeapon(self, weapon_type: int, weapon_texture: Texture) -> Object:
        """
            Создание оружия

            Аргументы:
                weapon_type - Тип оружия
                * 1 - Меч
                * 2 - Топор
                * 3 - Щит
                * 4 - Лук
                * 5 - Арбалет
                weapon_texture - Текстура оружия
            Возвращает:
                Объект оружия
        """
        ...

    def spawnBoss(self) -> Object:
        """
            Создание босса

            Создаёт босса после того как игрок прошёл через стену тумана и попал на арену с боссом

            Возвращает:
                Объект босса
        """
        ...

    def respawnAllEnemies(self) -> int:
        """
            Возрождает всех врагов
            
            При возрождении устанавливает их здоровье на максимум

            Возвращает:
                Количество врагов, которые были возрождены
        """
        ...

    def interactWithObject(self, object_type: int) -> bool:
        """
            Взаимодействие с объектом

            Взаимодействует с объектом, открывая его(дверь), приводя его в действие(лифт), переключая на 
            противоположное состояние(рычаг) и добавляя его в инвентарь(ключ)

            Аргументы:
                object_type - Тип объекта, с которым игрок взаимодействует
                * 1 - Дверь
                * 2 - Лифт
                * 3 - Рычаг
                * 4 - Ключ
            Возвращает:
                Доступно данное действие или нет
        """
        ...

    def collectSouls(self) -> int:
        """
            Сбор душ

            Подбирает души и добавляет их к общему количеству душ игрока

            Возвращает:
                Количество душ которые были добавлены
        """
        ...

    def levelUpPlayer(self, player: Player) -> int:
        """
            Увеличение уровня игрока

            Увеличивает уровень игрока на 1 и даёт ему на выбор улучшить одну из характеристик

            Аргументы:
                player - Главный персонаж
            Возвращает:
                Новый уровень игрока
        """
        ...

    def dealElementalDamage(self, player: Player, element_type: int) -> List[List[Union[StatusType, int]]]:
        """
            Наносит стихийный урон игроку

            Аргументы:
                player - Главный персонаж
                element_type - Тип стихийного урона
                * 1 - Обморожение накапливает статус и при достижении отметки уменьшает сопротивление 
                от всех типов урона
                * 2 - Огонь наносит большой урон и поджигает игрока
                * 3 - Отравление при достижении отметки накладывает статус, который в течении определённого времени
                отнимает очки здоровья у игрока
                * 4 - Опустошение при достижении определённой отметки мгновенно убивает игрока
            Возвращает:
                Какой статус накладывается и сколько урона он наносит
        """
        ...
