# Write a ShoppingCart class that stores an array of items with methods to add an item, remove an item, and display all the items.

class ShoppingCart
  attr_accessor :items_array
  
  def initialize
    @items_array = []
  end
  def add(item)
    pp items_array
    items_array << item
  end

  def remove(value)
    if items_array.delete(value)
    else items_array.delete_at(value)
    end
  end
  alias_method :delete, :remove
  def display
    pp items_array
  end
end

shopping_cart = ShoppingCart.new
shopping_cart.add("Apples")
shopping_cart.display
shopping_cart.add("Pears")
shopping_cart.display
shopping_cart.delete("Apples")
shopping_cart.display
shopping_cart.remove(0)
shopping_cart.display
