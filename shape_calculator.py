class Rectangle:
  def __init__(self, width: int, height:int) -> None:
    self._width = width
    self._height = height
  
  def __str__(self) -> str:
    return f"Rectangle(width={self._width}, height={self._height})"

  def set_width(self, width: int) -> None:
    self._width = width
  
  def get_width(self) -> int:
    return self._width
  
  def set_height(self, height: int) -> None:
    self._height = height
  
  def get_height(self) -> int:
    return self._height

  def get_area(self) -> int:
    return self._width * self._height
  
  def get_perimeter(self) -> int:
    return 2 * (self._width + self._height)
  
  def get_diagonal(self) -> int:
    return (self._width ** 2 + self._height ** 2) ** .5

  def get_picture(self) -> str:
    if self._width > 50 or self._height > 50:
      return "Too big for picture."
    output = ""
    for i in range(0, self._height):
      output = output + "*" * self._width + "\n"
    return output
  
  def get_amount_inside(self, rectangle) -> int:
    num_vert = (self._height // rectangle.get_height()) * (self._width // rectangle.get_width())
    num_hor = (self._height // rectangle.get_width()) * (self._width // rectangle.get_height())
    return max(num_vert, num_hor)


class Square(Rectangle):
  def __init__(self, side_length:int) -> None:
    super().__init__(side_length, side_length)
  
  def __str__(self) -> str:
    return f"Square(side={self._height})"
  
  def set_side(self, side_length:int) -> None:
    self._height = side_length
    self._width = side_length

  def set_width(self, width:int) -> None:
    self.set_side(width)
  
  def set_height(self, height: int) -> None:
    self.set_side(height)


