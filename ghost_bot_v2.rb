STDOUT.sync = true # DO NOT REMOVE
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

link_hash = {}
factory_count = gets.to_i # the number of factories
id = 0
factory_count.times {
  link_hash[id] = {}
  id += 1
}
# STDERR.puts link_hash

link_count = gets.to_i # the number of links between factories
link_count.times do
  factory_1, factory_2, distance = gets.split.map { |x| x.to_i }
  # STDERR.puts "#{factory_1}, #{factory_2}, #{distance}"
  link_hash[factory_1][factory_2] = distance
  link_hash[factory_2][factory_1] = distance
end
STDERR.puts link_hash

bombs = 2
second = 0
# game loop
loop do
  entity_hash = {}
  our_factories = []
  enemy_factories = []
  neutral_factories = []
  our_troops = {}
  enemy_troops = {}
  our_bombs = {}
  enemy_bombs = {}
  hq_id = nil
  enemy_hq_id = nil
  enemy_target = nil
  most_val_enemy = nil
  most_val_enemy_id = nil
  most_val_neut = nil
  most_val_neut_id = nil
  targeted = {}
  entity_count = gets.to_i # the number of entities (e.g. factories and troops)
  entity_count.times {
    entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5 = gets.split
    # STDERR.puts "#{entity_id}, #{entity_type}, #{arg_1}, #{arg_2}, #{arg_3}, #{arg_4}, #{arg_5}"
    entity_id = entity_id.to_i
    arg_1 = arg_1.to_i
    arg_2 = arg_2.to_i
    arg_3 = arg_3.to_i
    arg_4 = arg_4.to_i
    arg_5 = arg_5.to_i
    entity_hash[entity_id] = [entity_type, arg_1, arg_2, arg_3, arg_4, arg_5]
    # STDERR.puts entity_hash
    if entity_type == "FACTORY"
      value = arg_3.to_f / (arg_2 + 1)
      if arg_1 == 1
        our_factories << [entity_id, arg_2, arg_3]
        if !hq_id || arg_2 > entity_hash[hq_id][2]
          hq_id = entity_id
        end
      elsif arg_1 == -1
        enemy_factories << [entity_id, arg_2, arg_3]
        if arg_3 > 0 && (!enemy_hq_id || arg_2 > entity_hash[enemy_hq_id][2])
          enemy_hq_id = entity_id
        end
        if !most_val_enemy || value > most_val_enemy
          most_val_enemy = value
          most_val_enemy_id = entity_id
          # STDERR.puts "En. target so far = #{most_val_neut_id}"
        end
      else
        STDERR.puts "Factory #{entity_id} value = #{value}"
        neutral_factories << [entity_id, arg_2, arg_3, value]
        if (!most_val_neut || value > most_val_neut) && arg_3 != 0
          most_val_neut = value
          most_val_neut_id = entity_id
          # STDERR.puts "Neut. target so far = #{most_val_neut_id}"
        end
      end
    elsif entity_type == "TROOP"
      if arg_1 == 1
        if !our_troops[arg_3]
          our_troops[arg_3] = [[entity_id, arg_2, arg_4, arg_5]]
        else
          our_troops[arg_3] << [entity_id, arg_2, arg_4, arg_5]
        end
      else
        if !enemy_troops[arg_3]
          enemy_troops[arg_3] = [[entity_id, arg_2, arg_4, arg_5]]
        else
          enemy_troops[arg_3] << [entity_id, arg_2, arg_4, arg_5]
        end
      end
    else
      if arg_1 == 1
        our_bombs[arg_3] = [entity_id, arg_2, arg_4]
      else
        if !enemy_bombs["id: #{entity_id}"]
          turns_until_explode = link_hash[arg_2][arg_3]
        else
          turns_until_explode -= 1
        end
        enemy_bombs["id: #{entity_id}"] = [arg_2, arg_3, turns_until_explode]
        enemy_bombs[arg_3] = [entity_id, arg_2, turns_until_explode]
      end
    end
    entity_count -= 1
    if !enemy_target || entity_hash[enemy_target][1] != -1
      enemy_target = most_val_neut_id
    end
  }
  STDERR.puts entity_count, entity_hash
  STDERR.puts "Ours: #{our_factories}"
  STDERR.puts "Enemies: #{enemy_factories}"
  STDERR.puts "Neutral: #{neutral_factories}"
  STDERR.puts "HQs: #{hq_id} #{enemy_hq_id}"
  STDERR.puts "Neut. target = #{most_val_neut_id}"
  # Write an action using puts
  # To debug: STDERR.puts "Debug messages..."
  # Needed loops
  our_factories.each { |factory|
    id = factory[0]
    cyborgs = factory[1]
    production = factory[2]
    freeze = factory[3]
    needed = 0
    enemy_dist = 21
    if enemy_troops[id]
      enemy_troops[id].each { |troop|
        needed += troop[2]
        if troop[3] < enemy_dist
          enemy_dist = troop[3]
        end
      }
    end
    if enemy_bombs[id]
      enemy_bombs[id].each { |bomb|
        if needed > 0
          needed += 10
        end
        if bomb[2] < enemy_dist
          enemy_dist = troop[2]
        end
      }
    end
    if our_troops[id]
      our_troops[id].each { |troop|
        needed -= troop[2]
      }
    end
    if enemy_dist < freeze
      will_produce = 0
    else
      will_produce = production * ((enemy_dist - freeze) + 1)
    end
    additional_needed = needed - (cyborgs + will_produce)
    factory << additional_needed
  }

  enemy_factories.each { |factory|
    id = factory[0]
    cyborgs = factory[1]
    production = factory[2]
    freeze = factory[3]
    needed = cyborgs + 1
    our_dist = 21
    if our_troops[id]
      our_troops[id].each { |troop|
        needed -= troop[2]
        if troop[3] < our_dist
          our_dist = troop[3]
        end
      }
    end
    if our_bombs[id]
      our_bombs[id].each { |bomb|
        if needed > 0
          needed -= 10
        end
        if bomb[2] < our_dist
          our_dist = bomb[2]
        end
      }
    end
    if enemy_troops[id]
      enemy_troops[id].each { |troop|
        needed += troop[2]
      }
    end
    if our_dist < freeze
      will_produce = 0
    else
      will_produce = production * ((our_dist - freeze) + 1)
    end
    additional_needed = needed - (cyborgs + will_produce)
    factory << additional_needed
  }

  neutral_factories.each { |factory|
    id = factory[0]
    cyborgs = factory[1]
    production = factory[2]
    needed = cyborgs + 1
    our_dist = 21
    enemy_dist = 21
    if our_troops[id]
      our_troops[id].each { |troop|
        needed -= troop[2]
        if troop[3] < our_dist
          our_dist = troop[3]
        end
      }
    end
    if enemy_troops[id]
      enemy_troops[id].each { |troop|
        if troop[3] < enemy_dist
          enemy_dist = troop[3]
        end
        if troop[3] < our_dist
          needed -= troop[2]
        else
          needed += troop[2]
        end
      }
    end
    additional_needed = needed
    factory << additional_needed
  }

  # For each factory, find the closest factory or factories that could provide the additional_needed
  our_factories.each { |factory|
    id = factory[0]
    additional_needed = factory[4]
    if additional_needed > 0
      closest_dist = 21
      closest_fact = nil
      our_factories.each { |other_factory|
        other_id = other_factory[0]
        if other_id != id
          if other_factory[4] < 0
            extra_cyborgs -= other_factory[4]
          end
          if extra_cyborgs >= additional_needed
            dist = link_hash[id][other_id]
            if dist && dist < closest_dist
              closest_dist = dist
              closest_fact = other_id
            end
          end
        end
      }
      if closest_fact
        factory << closest_fact
      end
    end
  }

  enemy_factories.each { |factory|
    id = factory[0]
    additional_needed = factory[4]
    if additional_needed > 0
      closest_dist = 21
      closest_fact = nil
      our_factories.each { |other_factory|
        other_id = other_factory[0]
        if other_factory[4] < 0
          extra_cyborgs -= other_factory[4]
        end
        if extra_cyborgs >= additional_needed
          dist = link_hash[id][other_id]
          if dist && dist < closest_dist
            closest_dist = dist
            closest_fact = other_id
          end
        end
      }
      if closest_fact
        factory << closest_fact
      end
    end
  }

  neutral_factories.each { |factory|
    id = factory[0]
    additional_needed = factory[4]
    if additional_needed > 0
      closest_dist = 21
      closest_fact = nil
      our_factories.each { |other_factory|
        other_id = other_factory[0]
        if other_factory[4] < 0
          extra_cyborgs -= other_factory[4]
        end
        if extra_cyborgs >= additional_needed
          dist = link_hash[id][other_id]
          if dist && dist < closest_dist
            closest_dist = dist
            closest_fact = other_id
          end
        end
      }
      if closest_fact
        factory << closest_fact
      end
    end
  }

  all_factories = our_factories + enemy_factories + neutral_factories
  all_factories.sort_by! { |factory| factory[2].to_f / (factory[4] * (factory[5] + 1)) }

  # Capture all factories possible, in order of priority, using puts commands, as spelled out in the instructions, but we want to make sure that a factory does not remain with additional_needed > 0
  cl = ""
  all_factories.each { |factory|
    id = factory[0]
    cyborgs = factory[1]
    production = factory[2]
    freeze = factory[3]
    additional_needed = factory[4]
    closest = factory[5]
    if additional_needed > 0
      cl += "MOVE #{id} #{additional_needed} #{closest};"
      additional_needed = 0
    end
  }
  if cl != ""
    puts cl.chop()
  else
    puts "WAIT"
  end
end

# #
# Summary of new rules

# Starting from the bronze league, you can increase the production rate of your factories.
# This is the last rule change.
# See the updated statement for details.
#  	The Goal
# Your objective is to produce a maximum amount of cyborgs in order to destroy those of your opponent. To this end, you must take ownership of factories that will enable you to increase the size of your cyborg army.
#  	Rules
# The game is played with 2 players on a board on which a variable number of factories are placed (from 7 to 15 factories). Initially, each player holds a single factory in which there is a stock of 15 to 30 cyborgs. The other factories are neutral but also have cyborgs defending them.

# On each turn, a player can send any number of cyborgs from one factory to another. The cyborgs in transit form a troop. This troop will take between 1 and 20 turns to reach its destination. When the troop arrives, the cyborgs will fight with any opponent cyborgs present at the factory.

# Factory placement

# Factories are placed randomly across the map at the start of each game. The player is given the distance between each factory, expressed as the number of turns it takes to reach a factory starting from another.

# Game Turn

# One game turn is computed as follows:

# Move existing troops and bombs
# Execute user orders
# Produce new cyborgs in all factories
# Solve battles
# Make the bombs explode
# Check end conditions

# Cyborg Production

# Each turn, every non-neutral factory produces between 0 and 3 cyborgs.

# Battles

# To conquer a factory, you must send cyborgs to the coveted factory. Battles are played in this order:

# Cyborgs that reach the same destination on the same turn fight between themselves.
# Remaining cyborgs fight against the ones already present in the factory (beware that the cyborgs currently leaving do not fight).
# If the number of attacking cyborgs is greater than the number of cyborgs in defense, the factory will then belong to the attacking player and it will start producing new cyborgs for this player on the next turn.

# Bombs

# Each player possesses 2 bombs for each game. A bomb can be sent from any factory you control to any factory. The corresponding action is: BOMB source destination, where source is the identifier of the source factory, and destination is the identifier of the destination factory.

# When a bomb reaches a factory, half of the cyborgs in the factory are destroyed (floored), for a minimum of 10 destroyed cyborgs. For example, if there are 33 cyborgs, 16 will be destroyed. But if there are only 13 cyborgs, 10 will be destroyed.

# Following a bomb explosion, the factory won't be able to produce any new cyborgs during 5 turns.

# Be careful, your radar is able to detect the launch of a bomb but you don't know where its target is!

# It is impossible to send a bomb and a troop at the same time from the same factory and to the same destination. If you try to do so, only the bomb will be sent.

# Production Increase

# At any moment, you can decide to sacrifice 10 cyborgs in a factory to indefinitely increase its production by one cyborg per turn. A factory will not be able to produce more than 3 cyborgs per turn. The corresponding action is: INC factory, where factory is the identifier of the factory that you want to improve.

# Victory Conditions
# Your opponent has no cyborgs left, nor any factories capable of producing new cyborgs.
# You have more cyborgs than your opponent after 200 turns.
#  	Expert Rules
# Because a source code is worth a thousand words, you can access to the code of the "Referee" on our GitHub.
#  	Game Input
# Initialization input
# Line 1:factoryCount, the number of factories.
# Line 2:linkCount, the number of links between factories.
# Next linkCount lines: 3 space-separated integers factory1, factory2 and distance, where distance is the number of turns needed for a troop to travel between factory1 and factory2.
# Input for one game turn
# Line 1: an integer entityCount, the number of entities.
# Next entityCount lines: an integer entityId, a string entityType and 5 integers arg1, arg2, arg3, arg4 and arg5.

# If entityType equals FACTORY then the arguments are:
# arg1: player that owns the factory: 1 for you, -1 for your opponent and 0 if neutral
# arg2: number of cyborgs in the factory
# arg3: factory production (between 0 and 3)
# arg4: number of turns before the factory starts producing again (0 means that the factory produces normally)
# arg5: unused
# If entityType equals TROOP then the arguments are:
# arg1: player that owns the troop: 1 for you or -1 for your opponent
# arg2: identifier of the factory from where the troop leaves
# arg3: identifier of the factory targeted by the troop
# arg4: number of cyborgs in the troop (positive integer)
# arg5: remaining number of turns before the troop arrives (positive integer)
# If entityType equals BOMB then the arguments are:
# arg1: player that send the bomb: 1 if it is you, -1 if it is your opponent
# arg2: identifier of the factory from where the bomb is launched
# arg3: identifier of the targeted factory if it's your bomb, -1 otherwise
# arg4: remaining number of turns before the bomb explodes (positive integer) if that's your bomb, -1 otherwise
# arg5: unused
# Output for one game turn
# The available actions are:
# MOVE source destination cyborgCount: creates a troop of cyborgCount cyborgs at the factory source and sends that troop towards destination. Example: MOVE 2 4 12 will send 12 cyborgs from factory 2 to factory 4.
# BOMB source destination: creates a bomb in the factory source and sends it towards destination.
# INC factory: increases the production of the factory factory at the cost of 10 cyborgs.
# WAIT: does nothing.
# MSG message: prints a message on the screen.
# You may use several actions by using a semi-colon ;. Example: MOVE 1 3 18 ; MSG Attack Factory 3. If you try to move more cyborgs that there are in the source factory, then all the available units will be sent.
# Constraints
# 7 ≤ factoryCount ≤ 15
# 21 ≤ linkCount ≤ 105
# 1 ≤ distance ≤ 20
# Response time for first turn ≤ 1000ms
# Response time for one turn ≤ 50ms
