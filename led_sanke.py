import os
import random
import keyboard
import time

class Point:
    def __init__(self, x, y) -> None:
        if x > 7:
            x = 0
        elif x < 0:
            x = 7
        if y > 7:
            y = 0
        elif y < 0:
            y = 7
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.dir_x = 1
        self.dir_y = 0
        self.is_hungry = True
        self.length = 2
        self.cells = [Point(4,3), Point(3,3)]
    def eat(self):
        self.is_hungry = False
    def turn_left(self):
        if self.dir_x == 1 and self.dir_y == 0:
            return
        self.dir_x = -1
        self.dir_y = 0
    def turn_right(self):
        if self.dir_x == -1 and self.dir_y == 0:
            return
        self.dir_x = 1
        self.dir_y = 0
    def turn_up(self):
        if self.dir_x == 0 and self.dir_y == -1:
            return
        self.dir_y = 1
        self.dir_x = 0
    def turn_down(self):
        if self.dir_x == 0 and self.dir_y == 1:
            return
        self.dir_y = -1
        self.dir_x = 0
    def move(self):
        if self.is_hungry:
            new_x = self.cells[0].x + self.dir_x
            new_y = self.cells[0].y + self.dir_y
            for i in range(self.length -1, 0, -1):
                self.cells[i].x = self.cells[i - 1].x
                self.cells[i].y = self.cells[i - 1].y
            self.cells[0] = Point(new_x, new_y)
        else:
            new_x = self.cells[0].x + self.dir_x
            new_y = self.cells[0].y + self.dir_y
            self.cells.insert(0, Point(new_x, new_y))
            self.length += 1
            self.is_hungry = True

class LedMap:
    def __init__(self):
        self.led_map = []
        for i in range(8):
            temp = []
            for j in range(8):
                temp.append(0)
            self.led_map.append(temp)

    def clear(self):
        for i in range(8):
            for j in range(8):
                self.led_map[i][j] = 0
    def new_food_position(self, snake: Snake):
        while True:
            valid_position = True
            food_x = random.randint(0, 7)
            food_y = random.randint(0, 7)
            for cell in snake.cells:
                if cell.x == food_x and cell.y == food_y:
                    valid_position = False
                    break
            if valid_position:
                return Point(food_x, food_y)
    def set_food_led(self, position: Point):
        if position is None:
            return
        x = position.x
        y = position.y
        self.led_map[y][x] = 1
    def set_snake_led(self, snake: Snake):
        for cell in snake.cells:
            x = cell.x
            y = cell.y
            self.led_map[y][x] = 1
    def show(self):
        os.system('cls')
        for y in range(7, -1, -1):
            row = []
            for x in range(8):
                if self.led_map[y][x] == 0:
                    row.append(' ')
                else:
                    row.append('O')
            print(row)
    def get_bit_columns(self):
        columns = []
        for x in range(8):
            tempCol = []
            for y in range(7, -1, -1):
                led = self.led_map[y][x]
                tempCol.append(led)
            columns.append(tempCol)
        return columns
    def get_column_sum(self, column):
        value_sum = 0
        for i in range(8):
            value_sum += column[i] << (7 - i)
        return value_sum
    def get_map_as_tuple(self):
        columns = self.get_bit_columns()
        result = []
        for col in columns:
            column_sum = self.get_column_sum(col)
            result.append(column_sum)
        return tuple(result)
    
snake = Snake()
led_map = LedMap()
food_position: Point = None
while True:
    led_map.clear()
    if food_position is None:
        food_position = led_map.new_food_position(snake)

    if keyboard.is_pressed('up'):
        snake.turn_up()
    if keyboard.is_pressed('down'):
        snake.turn_down()
    if keyboard.is_pressed('left'):
        snake.turn_left()
    if keyboard.is_pressed('right'):
        snake.turn_right()

    snake.move()
    if snake.cells[0].x == food_position.x and snake.cells[0].y == food_position.y:
        snake.is_hungry = False
        food_position = None
    led_map.set_snake_led(snake)
    led_map.set_food_led(food_position)
    led_map.show()
    time.sleep(0.1)
    # map_tuple = led_map.get_map_as_tuple()
    # print(map_tuple)
    # for num in map_tuple:
    #     print(hex(num), end=', ')
    # print()
    # input('debug')

