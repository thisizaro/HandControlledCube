**HandControlledCube**

Welcome to HandControlledCube! This repository contains code for a simple 3D cube visualization using Pygame, with the ability to control the rotation of the cube using hand gestures detected by a separate module.

### Contents:

1. **cube.py**: This script initializes a Pygame window and draws a rotating 3D cube. The cube can be rotated using keyboard inputs.

2. **CordReader1.py**: This script is intended to read hand gesture data from a sensor or file (not provided) and update the rotation angles of the cube accordingly. However, it seems to have the same functionality as cube.py.

### How to Use:

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/your-username/HandControlledCube.git
    ```

2. Install the required dependencies:

    ```
    pip install pygame
    ```

3. Run the `cube.py` or `CordReader1.py` script using Python:

    ```
    python cube.py
    ```

    or

    ```
    python CordReader1.py
    ```

4. Use the keyboard inputs to rotate the cube (`a`, `d`, `w`, `s`, `q`, `e`, `r`).

### Additional Notes:

- Both scripts contain the main loop that updates the rotation of the cube and handles user input.

- The cube's rotation angles can be modified by changing the values in the `angle_x`, `angle_y`, and `angle_z` variables.

- The `angle.json` file seems intended to store rotation angles but is not fully utilized in the provided code.

- Feel free to explore and modify the code according to your requirements.

### Contributors:

- [Your Name](https://github.com/your-username)

### License:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments:

- This project is inspired by the desire to create interactive 3D visualizations using Python and Pygame.

- Thanks to the Pygame community for providing helpful resources and tutorials.

