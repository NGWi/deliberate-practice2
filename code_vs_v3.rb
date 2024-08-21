STDOUT.sync = true # DO NOT REMOVE
# Save humans, destroy zombies!

# game loop
loop do
  x, y = gets.split.map { |x| x.to_i }
  STDERR.puts "x: #{x} #{y}"

  human_count = gets.to_i
  STDERR.puts "human_count: #{human_count}"
  human_coords = {}
  human_count.times do
    human_id, human_x, human_y = gets.split.map { |x| x.to_i }
    STDERR.puts "human_id: #{human_id}"
    STDERR.puts "human_coord: #{human_x} #{human_y}"
    human_coords[human_id] = [human_x, human_y]
  end
  STDERR.puts "human_coords: #{human_coords}"

  zombie_count = gets.to_i
  STDERR.puts "zombie_count: #{zombie_count}"
  zombies_nexts = {}
  zombie_count.times do
    zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = gets.split.map { |x| x.to_i }
    STDERR.puts "zombie_id: #{zombie_id}"
    zombie_next = [zombie_xnext, zombie_ynext]
    zombies_nexts[zombie_id] = zombie_next
  end
  STDERR.puts "zombies_nexts: #{zombies_nexts}"

  shortest_times = {}
  human_coords.each do |human_id, human_coord|
    shortest_time = Float::INFINITY
    human_x, human_y = human_coord
    STDERR.puts "Retrieved human: #{human_x} #{human_y}"
    zombies_nexts.each do |zombie_id, zombie_next|
      zombie_xnext, zombie_ynext = zombie_next
      distance = (zombie_xnext - human_x).abs + (zombie_ynext - human_y).abs
      time = (distance / 400).ceil + 1
      if time < shortest_time
        shortest_time = time
      end
    end
    shortest_times[human_id] = shortest_time
  end
  STDERR.puts "shortest_times: #{shortest_times}"

  closest_human_to_ash = human_coords.values.first
  shortest_ash_distance = Float::INFINITY
  human_coords.each do |human_id, human_coord|
    human_x, human_y = human_coord
    distance = (x - human_x).abs + (y - human_y).abs
    ash_time = ((distance - 2000) / 1000).floor + 1
    if ash_time <= shortest_times[human_id] && distance < shortest_ash_distance
      closest_human_to_ash = human_coord
      shortest_ash_distance = distance
    end
  end
  puts closest_human_to_ash.join(' ') # Your destination coordinates
end