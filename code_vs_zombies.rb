STDOUT.sync = true # DO NOT REMOVE
# Save humans, destroy zombies!

# game loop
loop do
  x, y = gets.split.map { |x| x.to_i }
  STDERR.puts "x: " + x.to_s
  STDERR.puts "y: " + y.to_s

  human_count = gets.to_i
  STDERR.puts "human_count: " + human_count.to_s
  human_coords = []
  human_count.times do
    human_id, human_x, human_y = gets.split.map { |x| x.to_i }
    STDERR.puts "human_id: " + human_id.to_s
    STDERR.puts "human_x: " + human_x.to_s
    STDERR.puts "human_y: " + human_y.to_s
    human_coords << [human_x, human_y]
  end
  STDERR.puts "human_coords: " + human_coords.to_s

  zombie_count = gets.to_i
  STDERR.puts "zombie_count: " + zombie_count.to_s
  zombies_distances = []
  shortest_distance = nil
  closest_human = nil
  zombie_count.times do
    zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = gets.split.map { |x| x.to_i }
    STDERR.puts "zombie_id: " + zombie_id.to_s
    STDERR.puts "zombie_x: " + zombie_x.to_s
    STDERR.puts "zombie_y: " + zombie_y.to_s
    STDERR.puts "zombie_xnext: " + zombie_xnext.to_s
    STDERR.puts "zombie_ynext: " + zombie_ynext.to_s
    zombie_distances = []
    human_coords.each_with_index { |set, index|
      human_x = set[0]
      STDERR.puts "Retrieved human_x: " + human_x.to_s
      human_y = set[1]
      STDERR.puts "Retrieved human_y: " + human_y.to_s
      distance = Math.sqrt((zombie_xnext - human_x)**2 + (zombie_ynext - human_y)**2)
      STDERR.puts "Distance: " + distance.to_s
      if !shortest_distance || distance < shortest_distance
        shortest_distance = distance
        closest_human = index
      end
      zombie_distances << distance
    }
    STDERR.puts "shortest_distance: " + shortest_distance.to_s
    STDERR.puts "closest_human: " + closest_human.to_s
    STDERR.puts "zombie_distances: " + zombie_distances.to_s
    zombies_distances << zombie_distances
  end
  STDERR.puts "shortest_distance: " + shortest_distance.to_s
  STDERR.puts "closest_human: " + closest_human.to_s
  STDERR.puts "zombies_distances: " + zombies_distances.to_s

  # Write an action using puts
  # To debug: STDERR.puts "Debug messages..."

  puts human_coords[closest_human][0].to_s + " " + human_coords[closest_human][1].to_s # Your destination coordinates
end
