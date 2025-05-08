
# TKINTER-SLIDING-SCALE.py

## Overview
The `TKINTER-SLIDING-SCALE.py` script demonstrates how to create a graphical user interface (GUI) application using Python's `tkinter` library. This application features a sliding scale widget that allows users to select a value within a specified range and submit it. The selected value is then displayed in the console.

## Features
- **Scale Widget**: A vertical sliding scale that allows users to select a value between 0 and 100.
- **Submit Button**: A button that retrieves the current value of the scale and prints it to the console.
- **Customizable Appearance**: The scale widget and the application window are styled with colors and fonts for better visual appeal.
- **Dynamic Scaling**: The application window has minimum and maximum size constraints to ensure proper scaling.

## Components
### 1. **Scale Widget**
- **Range**: The scale ranges from 0 to 100.
- **Orientation**: The scale is vertical.
- **Length**: The scale has a length of 400 pixels.
- **Tick Interval**: Tick marks are displayed at intervals of 10.
- **Styling**: 
  - Background color: Light green.
  - Trough color: Blue.
  - Font: Arial, size 10.

### 2. **Submit Button**
- **Functionality**: When clicked, the button retrieves the current value of the scale and prints it in the format: `The Temperature is: <value> degrees Celsius`.

### 3. **Window Configuration**
- **Title**: "Temperature scaling App".
- **Size**: 
  - Initial size: 300x200 pixels.
  - Minimum size: 500x500 pixels.
  - Maximum size: 800x700 pixels.
- **Background Color**: Light blue.

## Code Walkthrough
1. **Importing Libraries**:
   - The `tkinter` library is imported to create the GUI components.

2. **Defining the `submit` Function**:
   - This function retrieves the value from the scale using `scale.get()` and prints it to the console.

3. **Creating the Main Window**:
   - A `Tk` instance is created to serve as the main application window.
   - The window is configured with a title, size, and background color.

4. **Adding the Scale Widget**:
   - A `Scale` widget is added to the window with the specified range, orientation, length, and styling.

5. **Adding the Submit Button**:
   - A `Button` widget is added to the window, which triggers the `submit` function when clicked.

6. **Running the Application**:
   - The `mainloop()` method is called to start the GUI event loop.

## How to Run
1. Ensure you have Python installed on your system.
2. Save the script as `TKINTER-SLIDING-SCALE.py`.
3. Run the script using the following command:
   ```bash
   python TKINTER-SLIDING-SCALE.py
   ```
4. Interact with the scale widget and click the "Submit" button to see the selected value in the console.

## Example Output
When the user selects a value of 75 on the scale and clicks "Submit", the following output will appear in the console:
```
The Temperature is: 75 degrees Celsius
```

## Dependencies
- Python 3.x
- `tkinter` (comes pre-installed with Python)

## Customization
You can modify the following parameters to customize the application:
- **Scale Range**: Change the `from_` and `to` values in the `Scale` widget.
- **Orientation**: Change `orient=VERTICAL` to `HORIZONTAL` for a horizontal scale.
- **Styling**: Update the `bg`, `troughcolor`, and `font` attributes of the `Scale` widget.
- **Window Size**: Adjust the `geometry`, `minsize`, and `maxsize` values.

## Use Cases
- Temperature selection in a thermostat application.
- Volume control in a media player.
- Any scenario requiring user input within a defined range.

## Conclusion
The `TKINTER-SLIDING-SCALE.py` script is a simple yet powerful example of how to use `tkinter` to create interactive GUI applications. It demonstrates the use of the `Scale` widget and event handling in Python, making it a great starting point for learning GUI development.
```
