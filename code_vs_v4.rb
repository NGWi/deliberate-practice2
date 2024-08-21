STDOUT.sync = true # DO NOT REMOVE
# Save humans, destroy zombies!

# game loop
loop do
  x, y = gets.split.map { |x| x.to_i }
  STDERR.puts "x: #{x} #{y}"

  human_count = gets.to_i
  STDERR.puts "human_count: #{human_count}"
  human_coords = []
  human_count.times do
    human_id, human_x, human_y = gets.split.map { |x| x.to_i }
    STDERR.puts "human_id: #{human_id}"
    STDERR.puts "human_coord: #{human_x} #{human_y}"
    human_coords << [human_x, human_y]
  end
  STDERR.puts "human_coords: #{human_coords}"

  zombie_count = gets.to_i
  STDERR.puts "zombie_count: #{zombie_count}"
  zombies_nexts = []
  zombie_count.times do
    zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = gets.split.map { |x| x.to_i }
    STDERR.puts "zombie_id: #{zombie_id}"
    zombie_next = [zombie_xnext, zombie_ynext]
    zombies_nexts << zombie_next
  end
  STDERR.puts "zombies_nexts: #{zombies_nexts}"

  shortest_times = []
  human_coords.each do |human_coord|
    shortest_time = Float::INFINITY
    human_x, human_y = human_coord
    STDERR.puts "Retrieved human: #{human_x} #{human_y}"
    zombies_nexts.each do |zombie_next|
      zombie_xnext, zombie_ynext = zombie_next
      distance = Math.sqrt((zombie_xnext - human_x)**2 + (zombie_ynext - human_y)**2)
      time = (distance / 400).ceil + 1
      if time < shortest_time
        shortest_time = time
      end
    end
    shortest_times << shortest_time
  end
  STDERR.puts "shortest_times: #{shortest_times}"

  # Calculate danger level for each human
  danger_levels = []
  human_coords.each do |human_coord|
    danger_level = 0
    human_x, human_y = human_coord
    zombies_nexts.each do |zombie_next|
      zombie_xnext, zombie_ynext = zombie_next
      distance = Math.sqrt((zombie_xnext - human_x)**2 + (zombie_ynext - human_y)**2)
      if distance < 2000
        danger_level += 1
      end
    end
    danger_levels << danger_level
  end
  STDERR.puts "danger_levels: #{danger_levels}"

  # Sort humans by danger level and distance to ash
  human_coords.sort_by! { |human_coord| [danger_levels[human_coords.index(human_coord)], Math.sqrt((x - human_coord[0])**2 + (y - human_coord[1])**2)] }

  closest_human_to_ash = human_coords.first
  shortest_ash_distance = Float::INFINITY
  human_coords.each do |human_coord|
    human_x, human_y = human_coord
    distance = Math.sqrt((x - human_x)**2 + (y - human_y)**2)
    ash_time = ((distance - 2000) / 1000).ceil
    if ash_time <= shortest_times[human_coords.index(human_coord)] && distance < shortest_ash_distance
      closest_human_to_ash = human_coord
      shortest_ash_distance = distance
    end
  end
  puts closest_human_to_ash.join(' ') # Your destination coordinates
end