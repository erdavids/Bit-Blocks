# Manually set the output image size
w = 1000
h = 1000

# Specify grid for the output image
rows = 30
columns = 41

# Optionally, base the size of the resulting image from a specified cell size
cell_size = 10
w = columns * cell_size
h = rows * cell_size

# Choose if you will use the random color generator
random_colors = False

# Define number of random colors
color_count = 2

# Specify rows that will only be the primary color
skip_rows = []

# Specify columns that will only be the primary color
skip_columns = []

# Give specific colors (if you're not using random)
primary_color = (0, 100, 200)
secondary_color = (20, 20, 20)

# Determines how often the primary color will be chosen
primary_probability = .2

# Display a grid on the output image
grid = True
grid_width = 1

# Choose block borders 
top_border = True
bottom_border = False
left_border = True
right_border = True

# Draw Outline
outline = True
outline_width = 1
outline_color = (255, 255, 255)

# Add Accent color
accent_color = True
acc_probability = .1
acc = (255, 255, 255)

def setup():
    
        
    sect_width = float(w)/columns
    sect_height = float(h)/rows
    
    size(w, h)
    
    if (grid):
        stroke(0, 0, 0, 255)
        strokeWeight(grid_width)
    else:
        noStroke()
    
    # Generate the random list of colors first
    colors = []
    for i in range(color_count):
        colors.append((random(50, 200), random(50, 200), random(50, 200)))
    
    sym_queue = []
    
    for y in range(rows):
        for x in range(columns):
            if (x < columns/2):
                if (random_colors == True):
                    if (random(1) < primary_probability):
                        c = colors[0]
                    else:
                        c = colors[1]
                        
                else:
                    if (random(1) < primary_probability):
                        c = primary_color
                    else:
                        c = secondary_color
                        
                if (accent_color and random(1) < acc_probability):
                    c = acc
                sym_queue.append(c)
            elif (x == columns/2):
                if (random_colors == True):
                    if (random(1) < primary_probability):
                        c = colors[0]
                    else:
                        c = colors[1]
                else:
                    if (random(1) < primary_probability):
                        c = primary_color
                    else:
                        c = secondary_color
                if (accent_color and random(1) < acc_probability):
                    c = acc
            else:
                c = sym_queue.pop()
            if (y in skip_rows or x in skip_columns):
                if (random_colors):
                    c = colors[0]
                else:
                    c = primary_color
            fill(c[0], c[1], c[2])
            rect(x * sect_width, y * sect_height, x * sect_width + sect_width, y * sect_height + sect_height)
            
            if (random_colors == True):
                c = colors[0]
            else:
                c = primary_color
            if (top_border and y == 0):
                fill(c[0], c[1], c[2])
                rect(x * sect_width, y * sect_height, x * sect_width + sect_width, y * sect_height + sect_height)
            elif (bottom_border and y == rows - 1):
                fill(c[0], c[1], c[2])
                rect(x * sect_width, y * sect_height, x * sect_width + sect_width, y * sect_height + sect_height)
            elif (left_border and x == 0):
                fill(c[0], c[1], c[2])
                rect(x * sect_width, y * sect_height, x * sect_width + sect_width, y * sect_height + sect_height)
            elif (right_border and x == columns - 1):
                fill(c[0], c[1], c[2])
                rect(x * sect_width, y * sect_height, x * sect_width + sect_width, y * sect_height + sect_height)


    
    save("Examples/small" + str(int(random(10000))) + ".png")
    
