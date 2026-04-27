# Maze Forge

Maze Forge is a polished, single-file HTML maze generator built with vanilla JavaScript and `<canvas>`. It renders responsive, high-DPI mazes in the browser, supports multiple generation algorithms, and automatically reveals the shortest solution path after generation.

## Features

- Responsive canvas that adapts to the browser window
- High-DPI rendering for sharper visuals on modern displays
- Two generation algorithms:
  - Depth-First Backtracker
  - Randomized Prim
- Adjustable cell size
- Adjustable generation speed
- Pause and resume support
- Automatic shortest-path solver after generation
- Animated solution overlay
- PNG export of the current maze
- Keyboard shortcuts for faster control
- Single-file implementation with no dependencies

## How It Works

Maze Forge builds a grid of cells and removes walls between neighboring cells to carve out a valid maze.

### Generation modes

**Depth-First Backtracker**  
Creates long, winding corridors with a classic labyrinth feel.

**Randomized Prim**  
Produces a more evenly branching maze with a different visual structure.

### Solving

Once the maze is complete, Maze Forge runs a shortest-path search from the entrance to the exit and animates the solution path over the finished maze.

## Controls

- **Generation algorithm**: Choose between DFS and Prim
- **Cell size**: Increase or decrease maze resolution
- **Speed**: Control how fast the maze is generated
- **Solution speed**: Control how quickly the solved path is drawn
- **Pause / Resume**: Freeze or continue animation
- **New Maze**: Generate a fresh maze
- **Export PNG**: Save the current maze as an image

### Keyboard shortcuts

- **Space** — Pause / resume
- **N** — New maze
- **S** — Export PNG

## Usage

1. Save the file as `index.html`
2. Open it in a modern browser
3. Use the controls to customize the maze
4. Generate, solve, and export as needed

## File Structure

This project is designed as a single self-contained HTML file:

- **HTML** — layout and controls
- **CSS** — visual styling and responsive UI
- **JavaScript** — grid logic, generation, solving, rendering, and interaction

## Browser Support

Maze Forge works best in current versions of:

- Google Chrome
- Microsoft Edge
- Firefox
- Safari

For the best experience, use a modern browser with Canvas support and hardware acceleration enabled.

## Customization

You can extend the project by adding:

- Additional algorithms, such as Wilson’s or Eller’s
- A start/end marker system
- Maze themes or color presets
- Pathfinding options like A* or BFS
- Step-by-step generation mode
- Mobile touch controls
- Maze statistics such as dead-end count, corridor length, or branching factor

## Technical Notes

- Rendering uses the Canvas 2D API
- The canvas is scaled using `devicePixelRatio` for crisp output
- Maze cells store wall states in an array:
  - top
  - right
  - bottom
  - left
- Solution finding uses a breadth-first traversal to guarantee the shortest path
- The UI is fully responsive and designed to work on both desktop and smaller screens

## License

No license has been specified. Add one if you plan to distribute or publish the project.

## Credits

Created as an advanced browser-based maze generator and visualizer using vanilla web technologies.
