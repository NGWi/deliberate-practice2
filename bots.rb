STDOUT.sync = true # DO NOT REMOVE
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

boost_avail = true
last_x = nil
last_y = nil
# game loop
loop do
  # next_checkpoint_x: x position of the next check point
  # next_checkpoint_y: y position of the next check point
  # next_checkpoint_dist: distance to the next checkpoint
  # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
  x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = gets.split.map { |x| x.to_i }
  STDERR.puts next_checkpoint_dist
  STDERR.puts next_checkpoint_angle
  opponent_x, opponent_y = gets.split.map { |x| x.to_i }
  distance = ((x - opponent_x)**2 + (y - opponent_y)**2)**0.5

  
  
  # Write an action using puts
  # To debug: STDERR.puts "Debug messages..."
  # if distance < 900
  #   next_checkpoint_x = opponent_x
  #   next_checkpoint_y = opponent_y
  # end 
  
  if boost_avail && next_checkpoint_dist >= 4500 && next_checkpoint_angle == 0
    thrust = "BOOST"
    boost_avail = false
  elsif next_checkpoint_dist <= 600 || next_checkpoint_dist < 9600 && next_checkpoint_angle.abs > 60 || next_checkpoint_dist < 7500 && next_checkpoint_angle.abs > 55 || next_checkpoint_dist < 6000 && next_checkpoint_angle.abs > 50 || next_checkpoint_dist < 4800 && next_checkpoint_angle.abs > 45 || next_checkpoint_dist < 2400 && next_checkpoint_angle.abs > 30 || next_checkpoint_dist < 1200 && next_checkpoint_angle.abs > 15 || next_checkpoint_angle.abs > 90
    thrust = 0
  else
    thrust = 100
  end
  STDERR.puts boost_avail

  if last_x && last_y
    dx = last_x - x
    dy = last_y - y
    velocity = (dx**2 + dy**2)**0.5
    STDERR.puts "#{dx} #{dy} #{velocity}"
    next_checkpoint_x += dx 
    next_checkpoint_y += dy
  end
  # You have to output the target position
  # followed by the power (0 <= thrust <= 100)
  # i.e.: "x y thrust"
  printf("%d %d #{thrust}\n", next_checkpoint_x, next_checkpoint_y, thrust)
  
  last_x = x
  last_y = y
end