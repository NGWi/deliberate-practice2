# Broken into functions by Blackbox.ai and debugged
STDOUT.sync = true # DO NOT REMOVE

def initialize_game
  @factory_count = gets.to_i # the number of factories
  @link_hash = {}
  @id = 0
  @factory_count.times do
    @link_hash[@id] = {}
    @id += 1
  end
end

def read_links
  @link_count = gets.to_i # the number of links between factories
  @link_count.times do
    factory_1, factory_2, distance = gets.split.map { |x| x.to_i }
    @link_hash[factory_1][factory_2] = distance
    @link_hash[factory_2][factory_1] = distance
  end
end

def read_entities
  @entity_hash = {}
  @our_factories = []
  @enemy_factories = []
  @neutral_factories = []
  @hq_id = nil
  @enemy_hq_id = nil
  @enemy_target = nil
  @most_val_enemy = nil
  @most_val_enemy_id = nil
  @most_val_neut = nil
  @most_val_neut_id = nil
  @targeted = {}
  @entity_count = gets.to_i # the number of entities (e.g. factories and troops)
  @entity_count.times do
    entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5 = gets.split
    entity_id = entity_id.to_i
    arg_1 = arg_1.to_i
    arg_2 = arg_2.to_i
    arg_3 = arg_3.to_i
    arg_4 = arg_4.to_i
    arg_5 = arg_5.to_i
    @entity_hash[entity_id] = [entity_type, arg_1, arg_2, arg_3, arg_4, arg_5]
    if entity_type == "FACTORY"
      value = arg_3.to_f/(arg_2 + 1)
      if arg_1 == 1
        @our_factories << [entity_id, arg_2, arg_3]
        if !@hq_id || arg_2 > @entity_hash[@hq_id][2]
          @hq_id = entity_id
        end
      elsif arg_1 == -1
        @enemy_factories << [entity_id, arg_2, arg_3]
        if arg_3 > 0 && (!@enemy_hq_id || arg_2 > @entity_hash[@enemy_hq_id][2])
          @enemy_hq_id = entity_id
        end
        if !@most_val_enemy || value > @most_val_enemy
          @most_val_enemy = value
          @most_val_enemy_id = entity_id
        end
      else
        @neutral_factories << [entity_id, arg_2, arg_3, value]
        if (!@most_val_neut || value > @most_val_neut) && arg_3 != 0
          @most_val_neut = value
          @most_val_neut_id = entity_id
        end
      end
    elsif entity_type == "BOMB"
      @targeted[arg_3] = arg_4
    end
  end
end

def calculate_closest_factory
  @closest_fact = nil
  min_dist = Float::INFINITY
  @our_factories.each do |factory|
    if @link_hash[factory[0]] && @link_hash[factory[0]][@enemy_hq_id]
      dist = @link_hash[factory[0]][@enemy_hq_id]
      if dist && dist < min_dist
        min_dist = dist
        @closest_fact = factory[0]
      end
    end
  end
end

def calculate_easiest_factory
  @easiest_hash = {}
  @our_factories.each do |factory|
    fact_id = factory[0]
    easiest = @neutral_factories[0][0]
    e_score = @entity_hash[easiest][3].to_f/((@entity_hash[easiest][2] + 1) * 21)
    @neutral_factories.each do |n_fact|
      neut_id = n_fact[0]
      d = @link_hash[fact_id][neut_id]
      score = @entity_hash[neut_id][3].to_f/((@entity_hash[neut_id][2] + 1) * d)
      if score > e_score
        e_score = score
        easiest = neut_id
      end
    end
    @easiest_hash[fact_id] = [easiest, e_score]
  end
end

def decide_action
  cl = ""
  if @most_val_neut_id
    @our_factories.each do |factory|
      fact_id = factory[0]
      easiest = @easiest_hash[fact_id]
      needed = @entity_hash[easiest[0]][2] + 1
      if @bombs > 0 && @second >= 0 && fact_id == @closest_fact
        cl += "BOMB #{fact_id} #{@enemy_hq_id};"
        @bombs -= 1
        @second = -5
      else
        if needed > 0
          if easiest[1] <= 0.1 && factory[1] >= 10 && factory[2] < 3
            cl += "INC #{fact_id};"
          else
            if needed < factory[1]
              cl += "MOVE #{fact_id} #{easiest[0]} #{needed};"
              needed = 0
            end
          end
        else
          break
        end
      end
    end
  elsif @most_val_enemy_id
    needed = @entity_hash[@most_val_enemy_id][2] + 1
    @our_factories.each do |factory|
      fact_id = factory[0]
      fuse = @targeted[@most_val_enemy_id]
      if @bombs > 0 && @second >= 0 && fact_id == @closest_fact
        cl += "BOMB #{fact_id} #{@enemy_hq_id};"
        @bombs -= 1
        @second = -5
      elsif !fuse || fuse < @link_hash[fact_id][@most_val_enemy_id]
        if needed > 0
          in_transit = @link_hash[fact_id][@most_val_enemy_id] + 1
          needed_from_fact = needed + @entity_hash[@most_val_enemy_id][3] * in_transit
          if needed_from_fact < factory[1]
            if needed_from_fact * in_transit > 10 && factory[1] >= 10 && factory[2] < 3
              cl += "INC #{fact_id};"
            else
              cl += "MOVE #{fact_id} #{@most_val_enemy_id} #{needed_from_fact};"
              needed = 0
            end
          end
        end
      end
    end
  else
    cl = "WAIT "
  end
  if cl != ""
    puts cl.chop
  else
    puts "WAIT"
  end
  @second += 1
end

initialize_game
read_links
# game loop
@bombs = 2
@second = 0
loop do
  read_entities
  calculate_closest_factory
  calculate_easiest_factory
  decide_action
end