# 9.60 Project: Age Classification in Humans vs. Machines

## Overview

This project aims to compare age classification capabilities between humans and machine learning models. Participants will be shown a series of faces and asked to classify the age range of each face. Simultaneously, a machine learning model will perform the same task, allowing for a comparative analysis of human and machine performance.

## Project Structure

- **scripts/**: Contains JavaScript files for running the experiment using PsychoJS.
  - `project.js`: Main script for the experiment.
  - `project-legacy-browsers.js`: Script for supporting legacy browsers.
  - `index.html`: HTML file to load the experiment.

- **models/**: Jupyter notebooks for training and evaluating machine learning models.
  - `model.ipynb`: Notebook for setting up and running the age classification model.
  - `model 2.ipynb`: Additional notebook for model experimentation.

- **data/**: Contains log files and datasets used in the experiment.
  - `198621_project_2024-04-26_11h42.20.610.log`: Log file for a specific experiment session.
  - `907181_project_2024-04-21_12h58.18.215.log`: Another log file for a different session.

- **lib/**: Contains external libraries and stylesheets.
  - `psychojs-2024.1.1.js.LEGAL.txt`: Legal information for the PsychoJS library.
  - `psychojs-2024.1.1.css`: Stylesheet for the PsychoJS library.

- **project.py**: Python script for running the experiment using PsychoPy.

- **project.psyexp**: PsychoPy experiment file.

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   - Ensure you have Python 3.10 or later installed.
   - Install PsychoPy and other dependencies:
     ```bash
     pip install psychopy
     ```

3. **Run the Experiment**:
   - For the web-based version, open `scripts/index.html` in a web browser.
   - For the desktop version, run `project.py` using PsychoPy.

## Usage

- **Human Participants**: Follow the on-screen instructions to classify the age of faces shown.
- **Machine Learning Model**: The model is set up in `models/model.ipynb` and can be run to classify ages automatically.

## Contact

For any issues or questions, please contact [sopsahl@mit.edu](mailto:sopsahl@mit.edu).

## License

This project is licensed under the MIT License. See the `lib/psychojs-2024.1.1.js.LEGAL.txt` file for more details.

## Acknowledgments

This project uses the PsychoJS library for running experiments in the browser and the ViT model for age classification.

## References

- Peirce J, Gray JR, Simpson S, et al. (2019) PsychoPy2: Experiments in behavior made easy. Behav Res 51: 195. https://doi.org/10.3758/s13428-018-01193-y
