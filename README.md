 # Kalender-Python
A Python script for generating SVG calendars to print

## Overview
`kalender-python` is a Python 3 script that automates the creation of customizable, beautifully designed calendar images in SVG format suitable for printing. This project serves as an efficient solution for individuals or organizations seeking a personalized way to organize their schedules, events, and holidays.

## Key Features
- Customizable layout: modify the design parameters in the provided `design.yaml` file to tailor the calendar to your specific needs.
- Support for multiple calendars: Generate separate SVG files for different months or years as required.
- Flexible text and image placement: Add custom titles, footers, and images to personalize your calendar.
- Holidays and school vacations: Include national holidays and custom events such as school breaks within the generated calendars.

## Getting Started
To use `kalender-python`, follow these steps:

1. Install Python 3 (if not already installed) from the official website: https://www.python.org/downloads/
2. Download and save this repository to your local machine.
3. Install required packages by running the following command in the project directory: `pip install -r requirements.txt`
4. Modify design parameters in the `design.yaml` file as needed.
5. Run the script using the following command: `python generate-kalender.py [year] [month]`, replacing the placeholders with the desired year and month (e.g., `python generate-kalender.py 2023 1`).
6. A new SVG file named after the specified year, month, and day will be generated in the project directory.

## Advanced Usage
For more advanced usage and customization options, explore the script's source code, specifically `generate-kalender.py`. The code is well-organized and extensible, allowing developers to further modify the behavior or introduce new features as needed.

## Contributing
Contributions are welcome! If you would like to contribute to this project, please fork the repository, make your changes, and submit a pull request for review.

## Acknowledgements
Special thanks to the original creator of this code for sharing their work on GitHub. We hope that this project helps simplify the process of creating personalized calendars for users worldwide.

Happy calendaring!