from flask import Flask,request,jsonify
from src.model_testing import load_model
import pandas as pd

# Set-up the logger
from src.logger import setup_logger
logger = setup_logger(name="ROOT",log_file="logs/app.log")

#Load the model 
model = load_model("model.pkl")

#Intialize the flask application
app = Flask(__name__)

#feature values
features =["score","trophy_level","accuracy","speed","final_score","negative_score","correct_answers","incorrect_answers","better_than","total_questions","mistakes_corrected","initial_mistake_count"]

@app.route("/predict",methods=["GET","POST"])
def predict_rank():
    try:
        data = request.get_json()
        missing_features = [f for f in features if f not in data]
        if missing_features:
            logger.error(f"Missing features {missing_features}")
            return jsonify({error:f"Missing features: {missing_features}"}),404

        df = pd.DataFrame([data], columns=features)  
        # Ensure numeric conversion (in case data is passed as strings)
        df = df.apply(pd.to_numeric)


        predicted_rank = int(model.predict(df)[0])
        logger.info(f"Predicted rank is :{predicted_rank}")

        return jsonify({"Predicted Rank":predicted_rank}),200

    except Exception as e:
        logger.error("Unexpected error occured",e)
        return jsonify({"error":str(e)}),500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)