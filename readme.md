# Student Rank Predictor

## Overview

The **Student Rank Predictor** is a machine learning application designed to predict a student's rank based on various performance metrics. The project encompasses data ingestion, preprocessing, model training, and deployment through a Flask API.

## Project Workflow

1. **Data Ingestion**: Data is extracted from a specified URL and stored in the `data` directory.
2. **Data Preprocessing**: The ingested data undergoes preprocessing for analysis, with results saved in the `data-preprocesses` directory.
3. **Model Training**: A Linear Regression model is trained and saved as `model.pkl`.
4. **API Deployment**: A Flask application is developed to serve predictions at the `/predict` endpoint.

## Insights

The following visualizations provide insights into the relationships between various metrics:

1. **Accuracy vs. Rank**:
   ![Accuracy vs. Rank](https://github.com/Dharansh-Neema/Student-Rank-Predictor/blob/main/analytics/visuals/accuracy_vs_rank.png)

2. **Score vs. Accuracy**:
   ![Score vs. Accuracy](https://github.com/Dharansh-Neema/Student-Rank-Predictor/blob/main/analytics/visuals/score_vs_accuracy.png)

3. **Score vs. Correct Answers**:
   ![Score vs. Correct Answers](https://github.com/Dharansh-Neema/Student-Rank-Predictor/blob/main/analytics/visuals/score_vs_correct_answers.png)

## Setup Instructions

To set up and run the application using Docker:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Dharansh-Neema/Student-Rank-Predictor.git
   cd Student-Rank-Predictor
   ```

2. **Build the Docker Image**:

   ```bash
   docker build -t rank-prediction .
   ```

3. **Run the Docker Container**:
   ```bash
   docker run -d -p 5000:5000 rank-prediction
   ```

The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Testing the Prediction API

To test the `/predict` endpoint, send a POST request with the following JSON payload:

```json
{
  "score": 85,
  "trophy_level": 2,
  "accuracy": 90,
  "speed": 100,
  "final_score": 92,
  "negative_score": 3,
  "correct_answers": 40,
  "incorrect_answers": 10,
  "better_than": 354,
  "total_questions": 70,
  "mistakes_corrected": 5,
  "initial_mistake_count": 8
}
```

You can use tools like `curl` or Postman to send the request:

```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "score": 85,
  "trophy_level": 2,
  "accuracy": 90,
  "speed": 100,
  "final_score": 92,
  "negative_score": 3,
  "correct_answers": 40,
  "incorrect_answers": 10,
  "better_than": 354,
  "total_questions": 70,
  "mistakes_corrected": 5,
  "initial_mistake_count": 8
}' http://127.0.0.1:5000/predict
```

The API will respond with the predicted rank based on the provided data.
