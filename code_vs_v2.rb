STDOUT.sync = true # DO NOT REMOVE
# Save humans, destroy zombies!

# game loop
loop do
  x, y = gets.split.map { |x| x.to_i }
  STDERR.puts "x: " + x.to_s + " " + y.to_s

  human_count = gets.to_i
  STDERR.puts "human_count: " + human_count.to_s
  human_coords = []
  human_count.times do
    human_id, human_x, human_y = gets.split.map { |x| x.to_i }
    STDERR.puts "human_id: " + human_id.to_s
    STDERR.puts "human_coord: " + human_x.to_s + " " + human_y.to_s
    human_coords << [human_x, human_y]
  end
  STDERR.puts "human_coords: " + human_coords.to_s

  zombie_count = gets.to_i
  STDERR.puts "zombie_count: " + zombie_count.to_s
  zombies_nexts = []
  zombie_count.times do
    zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = gets.split.map { |x| x.to_i }
    STDERR.puts "zombie_id: " + zombie_id.to_s
    # STDERR.puts "zombie_x: " + zombie_x.to_s
    # STDERR.puts "zombie_y: " + zombie_y.to_s
    STDERR.puts "zombie_next: " + zombie_xnext.to_s + " " + zombie_ynext.to_s
    zombie_next = [zombie_xnext, zombie_ynext]
    zombies_nexts << zombie_next
  end
  STDERR.puts "zombies_nexts: " + zombies_nexts.to_s

  shortest_times = []
  human_coords.each { |set|
    shortest_time = nil
    human_x = set[0]
    human_y = set[1]
    STDERR.puts "Retrieved human_x: " + human_x.to_s + " " + human_y.to_s
    zombies_nexts.each { |set|
      zombie_xnext = set[0]
      zombie_ynext = set[1]
      STDERR.puts "Retrieved zombie_next: " + zombie_xnext.to_s + " " + zombie_ynext.to_s
      distance = Math.sqrt((zombie_xnext - human_x)**2 + (zombie_ynext - human_y)**2)
      STDERR.puts "Distance: " + distance.to_s
      time = (distance/400).ceil + 1
      STDERR.puts "Time: " + time.to_s
      if !shortest_time || time < shortest_time
        shortest_time = time
      end
    }
    STDERR.puts "shortest_time: " + shortest_time.to_s
    shortest_times << shortest_time
  }
  STDERR.puts "shortest_times: " + shortest_times.to_s

  ash_distances = []
  shortest_ash_distance = nil
  closest_human_to_ash = nil
  human_coords.each_with_index { |set, index|
    human_x = set[0]
    human_y = set[1]
    STDERR.puts "Retrieved human: " + human_x.to_s + " " + human_y.to_s
    time = shortest_times[index]
    STDERR.puts "Retrieved time: " + time.to_s
    distance = Math.sqrt((x - human_x)**2 + (y - human_y)**2)
    STDERR.puts "Ash Distance: " + distance.to_s
    ash_time = ((distance - 2000)/1000).ceil
    STDERR.puts "Ash Time: " + ash_time.to_s
    # Write an action using puts
    if ash_time <= time
      puts human_x.to_s + " " + human_y.to_s # Your destination coordinates
      break
    end
  }
end