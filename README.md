# Rainfall Prediction App

A machine learning-powered web app to predict rainfall using weather data. Built with Streamlit.

## Features
- Predict rainfall based on user input data.
- Interactive visualizations of weather patterns.
- User-friendly interface powered by Streamlit.

## Files Included
- **`weather.py`**: The Streamlit app script for rainfall prediction.
- **`requirements.txt`**: Lists the dependencies required to run the app.
- **`weather_model.zip`**: The trained machine learning model. Note: Download the zip file and extract to use
- **`ICRISAT_Weather_1978_to_2018.csv`**: Historical weather data (for reference or retraining).

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/weather-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd weather-app
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run weather.py
   ```

## Usage
- Open the app in your browser (default: `http://localhost:8501`).
- Use the sidebar to input weather features like temperature, humidity, wind, etc.
- Click "Predict" to view the rainfall prediction.

## Large Files
- If `weather_model.pkl` is not included due to size limitations, download it from [External Link Placeholder] and place it in the project directory.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## License
This project is licensed under the MIT License.

## Acknowledgments
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)

