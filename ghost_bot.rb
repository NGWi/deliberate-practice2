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
  hq_id = nil
  enemy_hq_id = nil
  enemy_target = nil
  most_val_enemy = nil
  most_val_enemy_id = nil
  most_val_neut = nil
  most_val_neut_id = nil
  targeted = {}
  entity_count = gets.to_i # the number of entities (e.g. factories and troops)
  entity_count.times do
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
      value = arg_3.to_f/(arg_2 + 1)
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
    elsif entity_type == "BOMB"
      targeted[arg_3] = arg_4
    end
    entity_count -= 1
    if !enemy_target || entity_hash[enemy_target][1] != -1
      enemy_target = most_val_neut_id
    end
  end
  STDERR.puts entity_count, entity_hash
  STDERR.puts "Ours: #{our_factories}"
  STDERR.puts "Enemies: #{enemy_factories}"
  STDERR.puts "Neutral: #{neutral_factories}"
  STDERR.puts "HQs: #{hq_id} #{enemy_hq_id}"
  STDERR.puts "Neut. target = #{most_val_neut_id}"
  # Write an action using puts
  # To debug: STDERR.puts "Debug messages..."
  if enemy_hq_id
    closest_fact = nil
    closest_dist = 21
    link_hash[enemy_hq_id].each { |key, value|
      # STDERR.puts "#{key} #{value}"
      ownership = entity_hash[key][1]
      new_dist = value
      if ownership == 1 && new_dist < closest_dist
        closest_fact = key
        closest_dist = new_dist
      end
    }
    link_hash.each { |id, hash|
      # STDERR.puts "#{id}, #{hash}"
      ownership = entity_hash[id][1]
      new_dist = hash[enemy_hq_id]
      # STDERR.puts "#{new_dist}"
      if new_dist && ownership == 1 && new_dist < closest_dist
        closest_fact = id
        closest_dist = new_dist
      end
    }
  end

  cl = ""
  if most_val_neut_id
    easiest_hash = {}
    our_factories.each { |factory|
      fact_id = factory[0]
      easiest = neutral_factories[0][0]
      e_score = entity_hash[easiest][3]/((entity_hash[easiest][2] + 1) * 21)
      neutral_factories.each { |n_fact|
        neut_id = n_fact[0]
        d = link_hash[fact_id][neut_id]
        score = entity_hash[neut_id][3].to_f/((entity_hash[neut_id][2] + 1) * d)
        STDERR.puts "Checking: #{fact_id}to#{neut_id}: #{score}"
        if score > e_score
          e_score = score
          easiest = neut_id
        end
      }
      easiest_hash[fact_id] = [easiest, e_score]
      STDERR.puts "Factory: #{fact_id}, Easiest: #{easiest}, Score: #{easiest_hash[fact_id][1]}"
    }
    #   needed = entity_hash[most_val_neut_id][2] + 1

    our_factories.each {|factory|
      fact_id = factory[0]
      easiest = easiest_hash[fact_id]
      needed = entity_hash[easiest[0]][2] + 1
      if bombs > 0 && second >= 0 && fact_id == closest_fact
        cl += "BOMB #{fact_id} #{enemy_hq_id};"
        bombs -= 1
        second = -5
      else
        if needed > 0
          # new_value = most_val_neut_id[3].to_f/(most_val_neut_id[2] + 2 + link_hash[fact_id][most_val_neut_id])
          # if new_value <= 0.1 && factory[1] >= 10 && factory[2] < 3
          if easiest_hash[fact_id][1] <= 0.1 && factory[1] >= 10 && factory[2] < 3
            STDERR.puts "Factory: #{fact_id}, Easiest: #{easiest}, Needed: #{needed}, Score: #{easiest_hash[fact_id][1]}"
            cl += "INC #{fact_id};"
          else
            if needed < factory[1]
              cl += "MOVE #{fact_id} #{easiest_hash[fact_id][0]} #{needed};"
              needed = 0
            end
          # else
          #   needed -= factory[1]
          end
        else
          break
        end
      end
      }
  elsif most_val_enemy_id
    needed = entity_hash[most_val_enemy_id][2] + 1
    our_factories.each {|factory|
    fact_id = factory[0]
    fuse = targeted[most_val_enemy_id]
    if bombs > 0 && second >= 0 && fact_id == closest_fact
      cl += "BOMB #{fact_id} #{enemy_hq_id};"
      bombs -= 1
      second = -5
    elsif !fuse || fuse < link_hash[fact_id][most_val_enemy_id]
      if needed > 0
        in_transit = link_hash[fact_id][most_val_enemy_id] + 1
        needed_from_fact = needed + entity_hash[most_val_enemy_id][3] * in_transit
        if needed_from_fact < factory[1]
          if needed_from_fact * in_transit > 10 && factory[1] >= 10 && factory[2] < 3
            cl += "INC #{fact_id};"
          else
            cl += "MOVE #{fact_id} #{most_val_enemy_id} #{needed_from_fact};"
            needed = 0
          end
        # else
        #   needed = needed_from_fact - factory[1]
        end
      end
    end
    }
  else
    cl = "WAIT "
  end
  if cl != ""
    puts cl.chop
  else
    puts "WAIT"
  end
  # if entity_hash[hq_id][2] > entity_hash[closest_fact][2] + (closest_dist + 1) * entity_hash[closest_fact][3]
  #   puts "MOVE #{hq_id} #{closest_fact} #{entity_hash[closest_fact][2] + (closest_dist + 1) * entity_hash[closest_fact][3] + 1}"
  # else
    # puts "WAIT"
  # end
  STDERR.puts bombs
  second += 1
end
