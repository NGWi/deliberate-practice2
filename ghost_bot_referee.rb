# Based on Referee.java
# Read initialization input
factory_count = gets.to_i
link_count = gets.to_i
links = []
link_count.times do
  factory1, factory2, distance = gets.split.map(&:to_i)
  links << [factory1, factory2, distance]
end

# Read game turn input
entity_count = gets.to_i
entities = []
entity_count.times do
  entityId, entityType, arg1, arg2, arg3, arg4, arg5 = gets.split
  entities << [entityId.to_i, entityType, arg1.to_i, arg2.to_i, arg3.to_i, arg4.to_i, arg5.to_i]
end

# Analyze the game state
factories = entities.select { |entity| entity[1] == "FACTORY" }
troops = entities.select { |entity| entity[1] == "TROOP" }
bombs = entities.select { |entity| entity[1] == "BOMB" }

# Heuristic: prioritize capturing neutral factories, then attacking opponent factories
neutral_factories = factories.select { |factory| factory[2] == 0 }
opponent_factories = factories.select { |factory| factory[2] == -1 }

if neutral_factories.any?
  # Capture a neutral factory
  target_factory = neutral_factories.max_by { |factory| factory[3] }
  source_factory = factories.select { |factory| factory[2] == 1 }.max_by { |factory| factory[3] }
  action = "MOVE #{source_factory[0]} #{target_factory[0]} #{source_factory[3]}"
elsif opponent_factories.any?
  # Attack an opponent factory
  target_factory = opponent_factories.max_by { |factory| factory[3] }
  source_factory = factories.select { |factory| factory[2] == 1 }.max_by { |factory| factory[3] }
  action = "MOVE #{source_factory[0]} #{target_factory[0]} #{source_factory[3]}"
else
  # Default to increasing production of a random factory
  factory = factories.select { |factory| factory[2] == 1 }.sample
  action = "INC #{factory[0]}"
end

# Output the action
puts action