# The Goal
# The game is played on a board of 9x9 square spaces. At the start of the game, each player starts on one side of the board.

# The objective is to reach the other side of the board before the other players do.
#  	Rules
# Players take turns moving their dragon:
# The first player (id = 0) always starts somewhere on the left edge of the board and must reach any cell on the right edge.
# The second player (id = 1) always starts somewhere on the right edge of the board and must reach any cell on the left edge.
# The third player (id = 2) always starts somewhere on the top edge of the board and must reach any cell on the bottom edge.

# On each turn of the game, a player may do one of two things:
# Move to an adjacent cell in any direction ( LEFT, RIGHT, UP, DOWN).
# Place a wall somewhere on the board.
# Wall placement:
# The player must indicate the cell on which he/she places a wall on its top left corner, as well as the wall orientation (horizontal or vertical).
# A wall is two cells long.
# Walls cannot cross. If a player tries to put a wall atop another wall, he/she loses the game. But it is still possible to put a vertical wall in between two horizontal walls (--|--).
# A wall may not be placed if it cuts off the only remaining path of any player to the side of the board it must reach. Walls may only be used to slow down an opponent's progress across the board.
# Each player may place a limited amount of walls: 10 each in a 2 player match and 6 each in a 3 player match.
# In games with more than 2 players, players are ranked by the order of finish.

# A player will lose if he/she attempts:
# An illegal wall placement: crossing an existing wall, sticking out the edge of the board, or cutting off a player's only path to his goal.
# An illegal move: moving outside the board or moving into a wall.
# Players not having reached the opposite side of the board within 100 turns will tie for last place.
 
# Victory Conditions
# You win when you reach the opposite side of the board
#  	Example

# Initialization phase
# Player 1 (id = 0) starts out on square (0,1). He/she must get to a square at coordinate x = 8.

# Turn 1: RIGHT
# Player moves towards his goal.

# Turn 2: 1 1 V
# Player puts a wall blocking passage from (1,1) to (0,1) & from (1,2) to (0,2)
 
 
 
 
#  	Game Input
# The program must first read the initialization data from standard input. Then, within an infinite loop, read the contextual data from the standard input (player and wall positions) and provide to the standard output the desired instructions.
# Initialization input
# Line 1: w: width of the board (=9)

# Line 2: h: height of the board (=9)

# Line 3: playerCount: number of players (2 or 3)

# Line 4: myId: your id in the game (first player = 0, second player = 1, etc.)

# Input for one game turn
# First playerCount lines: for each player, 3 integers x, y, wallsLeft: (x,y) indicates the player's coordinates on the grid. (0,0) is the top-left corner. wallsLeft indicates the amount of walls the player may still place during the game. You will receive -1 -1 -1 for players that are no longer playing.

# Next line: wallCount, an integer to specify the amount of walls currently placed on the board.

# Next wallCount lines: for each wall, the coordinates (wallX, wallY) of the top-left point of the wall, followed by wallOrientation, a character to specify the orientation of the wall: H for a horizontal wall or V for a vertical wall.

# Output for one game turn
# A single line (followed by a carriage return) specifying your desired action:
# A move: LEFT RIGHT UP ou DOWN.
# A wall placement: putX putY putOrientation. For example, 3 2 V will place a wall starting on the top-left corner of the square at (3,2) and extending to the bottom-left corner of the square at (3,3).
# Optionally, you may append to the line a message that will display above your dragon (20 characters max).
# Constraints
# w, h = 9
# 2 ≤ playerCount ≤ 3
# 0 ≤ myId < playerCount
# -1 ≤ x < w
# -1 ≤ y < h
# -1 ≤ wallsLeft ≤ 10
# 0 ≤ wallCount ≤ 20
# 0 ≤ wallX, putX< w
# 0 ≤ wallY, putY< h

# Response time per turn ≤ 100ms

STDOUT.sync = true # DO NOT REMOVE
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the board
# h: height of the board
# player_count: number of players (2 or 3)
# my_id: id of my player (0 = 1st player, 1 = 2nd player, ...)
w, h, player_count, my_id = gets.split.map { |x| x.to_i }

if my_id == 0
  opp_id = 1
elsif my_id == 1
  opp_id = 0
else
  opp_id = 0
end

my_dir = 0
if my_id == 0
  my_dir = 1
  opp_dir = -1
elsif my_id == 1
  my_dir = -1
  opp_dir = 1
else 
  my_v_dir = 1 #y += 1
  opp_dir = 1
end

# target_x = nil
# target_y = nil

def wall_lookup(x, y, wall_hash)
  wall = wall_hash["#{x},#{y}"]
  STDERR.puts "Retrieved #{x},#{y}: #{wall}"
  if !wall
    wall = ""
  end
  wall
end

def opp_next(player_arr, opp_x, opp_y, opp_dir, wall_hash )
  opp_facing_edge_x = opp_x.dup
  if opp_dir == 1
    opp_facing_edge_x = opp_x + opp_dir
  end
  STDERR.puts "Enemy facing edge: #{opp_facing_edge_x},#{opp_y}"

  wall = wall_lookup(opp_facing_edge_x, opp_y, wall_hash)
  if wall.include?("V")
    STDERR.puts "Blocked"
    return "Blocked"
  else
    STDERR.puts "Open"
    return "Open"
  end
end

def block_opp(player_arr, opp_x, opp_y, wall_hash, opp_dir)
  STDERR.puts "Calculating how to block enemy."
  block_x = opp_dir
  if opp_dir == -1
    block_x = 0
  end
  if opp_next(player_arr, opp_x, opp_y, opp_dir, wall_hash ) == "Open"
    if opp_y < 8 && !wall_lookup(opp_x + block_x, opp_y + 1, wall_hash).include?("V") && !wall_lookup(opp_x + block_x - 1, opp_y + 1, wall_hash).include?("H")
      puts "#{opp_x + block_x} #{opp_y} V"
    elsif opp_y > 0 && !wall_lookup(opp_x + block_x, opp_y - 1, wall_hash).include?("V") && !wall_lookup(opp_x + block_x - 1, opp_y, wall_hash).include?("H")
      puts "#{opp_x + block_x} #{opp_y - 1} V"
    else
      STDERR.puts "Can't"
      return false
    end
    return true
  end
  return false
end

#---------------------------------------------------------------------------------------

def my_next_from_top(player_arr, target_x, target_y, my_v_dir, wall_hash )
  facing_edge_y = target_y.dup
  if my_v_dir == 1
    facing_edge_y = target_y + my_v_dir
  end
  STDERR.puts "Thinking about crossing h_edge: #{target_x},#{facing_edge_y}"
  wall = wall_lookup(target_x, facing_edge_y, wall_hash)
  STDERR.puts wall
  if wall.include?("H")
    STDERR.puts "Think again."
    return "Blocked"
  else
    STDERR.puts "Good to go."
    return "Open"
  end
end

def find_gap_from_top(player_arr, target_x, target_y, my_v_dir, wall_hash, search_dir)
  if (search_dir == -1 && target_x > 0 ) || (search_dir == 1 && target_x < 8)
    target_x = target_x + search_dir
  else
    search_dir = -search_dir
  end
  STDERR.puts "Checking: #{target_x}, #{target_y}"
  if my_next_from_top(player_arr, target_x, target_y, my_v_dir, wall_hash ) == "Blocked"
    find_gap_from_top(player_arr, target_x, target_y, my_v_dir, wall_hash, search_dir)
  else
    STDERR.puts "Gap found: #{target_x}, #{target_y}"
    return target_x, target_y
  end
end

def my_next(player_arr, target_x, target_y, my_dir, wall_hash )
  facing_edge_x = target_x.dup
  if my_dir == 1
    facing_edge_x = target_x + my_dir
  end
  STDERR.puts "Thinking about crossing v_edge: #{facing_edge_x},#{target_y}"
  wall = wall_lookup(facing_edge_x, target_y, wall_hash)
  STDERR.puts wall
  if wall.include?("V")
    STDERR.puts "Think again."
    return "Blocked"
  else
    STDERR.puts "Good to go."
    return "Open"
  end
end

def move_from_top(player_arr, my_v_dir, my_x, my_y, target_x, target_y, wall_hash)
  STDERR.puts "func move_from_top (my_v_dir #{my_v_dir}. #{my_x},#{my_y}=>#{target_x},#{target_y})"
  right = my_next(player_arr, target_x, target_y, 1, wall_hash )
  left = my_next(player_arr, target_x, target_y, -1, wall_hash )
  if target_x < my_x && left == "Open"
    puts "LEFT"
  elsif target_x > my_x && right == "Open"
    puts "RIGHT"
  elsif target_x == my_x && target_y >= my_y
    puts "DOWN"
  elsif my_y > 0
    puts "UP"
  elsif left == "Open"
    puts "LEFT"
  elsif right == "Open"
    puts "RIGHT"
  elsif my_v_dir == 1
    puts "UP"
  elsif my_v_dir == -1
    puts "DOWN"
  else
    STDERR.puts "What's going down here?!"
  end
end

#---------------------------------------------------------------------------------------


def find_gap(player_arr, target_x, target_y, my_dir, wall_hash, search_dir, switched_search)
  STDERR.puts "Search_dir: #{search_dir}"
  if (search_dir == -1 && target_y > 0) || (search_dir == 1 && target_y < 8)
    target_y = target_y + search_dir
  elsif switched_search == false
    search_dir = -search_dir
    switched_search = true
    target_y = target_y + search_dir
  elsif switched_search == true
    target_x = my_x - my_dir
    target_y = my_y
    forbidding = [[my_x, target_x].max(), my_y, "V"]
    STDERR.puts "Move out."
    return target_x, target_y
  end
  STDERR.puts "Checking: #{target_x}, #{target_y}"
  open = my_next(player_arr, target_x, target_y, my_dir, wall_hash )
  if open == "Open"
    STDERR.puts "Gap found: #{target_x}, #{target_y}"
    return target_x, target_y
  elsif open == "Blocked"
      find_gap(player_arr, target_x, target_y, my_dir, wall_hash, search_dir, switched_search)
  end
end

def move(player_arr, my_dir, my_x, my_y, target_x, target_y, wall_hash)
  target_x += my_dir
  STDERR.puts "func move (my_dir #{my_dir}. #{my_x},#{my_y}=>#{target_x},#{target_y})"
  right = my_next(player_arr, my_x, my_y, 1, wall_hash )
  left = my_next(player_arr, my_x, my_y, -1, wall_hash )
  if target_y == my_y && target_x > my_x  && right == "Open"
    puts "RIGHT"
  elsif target_y == my_y && target_x < my_x && left == "Open"
    puts "LEFT"
  elsif target_y < my_y && my_y > 0 && my_next_from_top(player_arr, my_x, my_y, -1, wall_hash) == "Open"
    puts "UP"
  elsif target_y > my_y && my_y < 8 && my_next_from_top(player_arr, my_x, my_y, 1, wall_hash) == "Open"
    puts "DOWN"
  elsif my_dir == -1 && left == "Open" # my_dir == 1  && left == "Open" && my_x > 0
    puts "LEFT"     # Because otherwise would be boxed in
  elsif my_dir == 1 && right == "Open" # my_dir == -1 && right == "Open" && my_x < 8
    puts "RIGHT"    # Because otherwise would be boxed in
  elsif my_next_from_top(player_arr, my_x, my_y, -1, wall_hash) == "Open"
    puts "UP"
  elsif my_next_from_top(player_arr, my_x, my_y, 1, wall_hash) == "Open"
    puts "DOWN"  
  else
    STDERR.puts "Huh?!"
  end
end

wall_hash = {}
forbidding = []
#=======================================================================================
# game loop
loop do
  player_arr = []
  player_count.times do
    # x: x-coordinate of the player
    # y: y-coordinate of the player
    # walls_left: number of walls available for the player
    x, y, walls_left = gets.split.map { |x| x.to_i }
    player_arr << {x: x, y: y , walls_left: walls_left}
    STDERR.puts player_arr
  end
  wall_count = gets.to_i # number of walls on the board
  wall_count.times do
    # wall_x: x-coordinate of the wall
    # wall_y: y-coordinate of the wall
    # wall_orientation: wall orientation ('H' or 'V')
    wall_x, wall_y, wall_orientation = gets.split
    wall_x = wall_x.to_i
    wall_y = wall_y.to_i
    wall = wall_lookup(wall_x, wall_y, wall_hash)
    if !wall.include?(wall_orientation)
      wall += wall_orientation
      wall_hash["#{wall_x},#{wall_y}"] = wall
    end
    if wall_orientation == "H"
      wall = wall_lookup(wall_x + 1, wall_y, wall_hash)
      if !wall.include?(wall_orientation)
        wall += wall_orientation
        wall_hash["#{wall_x + 1},#{wall_y}"] = wall
        STDERR.puts "Also adding: #{wall_lookup(wall_x + 1, wall_y, wall_hash)}"
      end
    else
      wall = wall_lookup(wall_x, wall_y + 1, wall_hash)
      if !wall.include?(wall_orientation)
        wall += wall_orientation
        wall_hash["#{wall_x},#{wall_y + 1}"] = wall
        STDERR.puts "Also adding: #{wall_lookup(wall_x, wall_y + 1, wall_hash)}"
      end
    end
  end
  STDERR.puts wall_hash.inspect
  
  # Write an action using puts
  # To debug: STDERR.puts "Debug messages..."
  # action: LEFT, RIGHT, UP, DOWN or "putX putY putOrientation" to place a wall

  my_x = player_arr[my_id][:x]
  my_y = player_arr[my_id][:y]
  opp_x = player_arr[opp_id][:x]
  opp_y = player_arr[opp_id][:y]

  target_x = target_x || my_x.dup
  target_y = target_y || my_y.dup
  switched_search = false
  moved_out = false
  #---------------------------------------------------------------------------------------
  if my_id == 2
    if my_next_from_top(player_arr, target_x, target_y, my_v_dir, wall_hash ) == "Blocked"
      STDERR.puts "Blocked"
      target_x, target_y = find_gap_from_top(player_arr, target_x, target_y, my_v_dir, wall_hash, -1)
    end
    STDERR.puts "my_v_dir: #{my_v_dir}, my_x: #{my_x}, opp_x: #{opp_x}"
    walling = false
    my_walls_left = player_arr[my_id][:walls_left]
    if my_walls_left > 0
      walling = block_opp(player_arr, opp_x, opp_y, wall_hash, opp_dir)
    end
    if walling == false
      move_from_top(player_arr, my_v_dir, my_x, my_y, target_x, target_y, wall_hash)
    end
  #---------------------------------------------------------------------------------------
  else
    if my_next(player_arr, target_x, target_y, my_dir, wall_hash ) == "Blocked"
      STDERR.puts "Blocked"
      target_x, target_y = find_gap(player_arr, target_x, target_y, my_dir, wall_hash, -1, switched_search)
    end
    STDERR.puts "my_dir: #{my_dir}, my_x: #{my_x}, opp_x: #{opp_x}"
    walling = false
    my_walls_left = player_arr[my_id][:walls_left]
    if ((my_dir == 1 && my_x >= opp_x && opp_x >= 0) || (my_dir == -1 && my_x <= opp_x && opp_x >= 0)) && my_walls_left > 0
      walling = block_opp(player_arr, opp_x, opp_y, wall_hash, opp_dir)
    end
    if walling == false
       move(player_arr, my_dir, my_x, my_y, target_x, target_y, wall_hash)
    end
  end
  if !forbidding == [] && moved_out
    STDERR.puts "Forbidding."
    wall = wall_lookup(forbidding[0],forbidding[1]) 
    wall += forbidding[2]
    wall_hash["#{forbidding[0]},#{forbidding[1]}"] = forbidding[2]
  end
end
