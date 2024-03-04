class Movement:           
    def moveCharacter(char: Character, offset_position: Point3D):
        """
            Перемещаем персонажа, смещая его на точку 3D
        """
        ...


class Render:
    def render_character(char: Character):
        """
            Отрисовываем персонажа на экране
        """


class Background:
    def set_background(background_image: Image, filters: List[Filter]):
        """
            Устанавливаем задний фон локации, и применяем к нему заданные фильтры
        """


class Collisions:
    def check_collision(object: Object):
        """
            Проверяем коллизию заданного объекта с другими
        """


class Interactions:
    def open_door(door_object: Object):
        """
            Открытие двери
        """
        ...

    def open_chest(chest_object: Object):
        """
            Открытие сундука
        """
        ...

    def hit_enemy(enemy_object: Object):
        """
            Нападение на врага
        """
        ...

    
class CutSceneTrigger:
    def start_cut_scene():
        """
            Был ли задет триггер
            Если был, то начинается повествование
        """


class Abilities:
    def parry():
        """
            Проведение парирования и проверка попало ли 
            событие в кадр нанесения удара противником
        """
        ...

    def roll():
        """
            Перекат и игнорирование всего урона, проходящего по персонажу в момент переката
        """
        ...


class WorldRendering:
    def render_world(world: Asset):
        """
            Прогрузка игрового мира
        """
        ...


class EnemyCreator:
    def create_enemy(enemy_asset: Asset, enemy_class: Object):
        """
            Создание врага и прорисовка его на сцене
        """
        ...


class ItemsCollector:
    def pickup_item(item: Object, char: Character):
        """
            Переносит предмет в инвентарь игрока и удаляет предмет со сцены
        """
        ...


class Bonfires:
    def rest_at_bonfire(char: Character):
        """
            Восстанавливает здоровье игроку, восполняет эликсиры
            Заново создаёт всех врагов в локации
        """
        ...


class Weapon:
    def __init__(self, weapon_type: WeaponType, durability: int, damage: int, hardening: Hardening):
        """
            Создаёт оружие, которое имееет свои:
                - Тип оружия
                - Прочность
                - Урон
                - Закалка
        """
