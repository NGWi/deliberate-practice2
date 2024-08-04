# Write a Product class that stores the name, price, and metadata, where metadata is a hash that stores additional information about the product.
class Product
  attr_writer :name, :price, :metadata
end

product = Product.new
product.name = "New Product"
product.price = 5.99
product.metadata = { Description: "Bla bla bla...", first_posted: "08_04_2024" }
pp productA