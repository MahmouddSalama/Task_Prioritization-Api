from flask import Flask, request, jsonify
import pandas as pd
import joblib
from datetime import datetime
from flask_cors import CORS  # ✅ إضافة مكتبة CORS


model = joblib.load("weights/model")  
Task_Type = joblib.load("weights/Task_Type")  
Completion_Status = joblib.load("weights/Completion_Status")  

app = Flask(__name__)
CORS(app)  # ✅ تفعيل CORS لكل الطلبات

@app.route("/prioritize-tasks", methods=["POST"])
def prioritize_tasks_api():
    try:
        task_list = request.json.get("tasks")
        
        if not task_list:
            return jsonify({"error": "No tasks provided"}), 400
        
        tasks_df = pd.DataFrame(task_list)
        task_name = tasks_df['task_name']
        tasks_df.drop('task_name', axis=1, inplace=True)
        
        tasks_df['Deadline'] = pd.to_datetime(tasks_df['Deadline'])
        tasks_df['Time_Remaining'] = (tasks_df['Deadline'] - datetime.now()).dt.total_seconds() / 3600

        ordered_tasks = tasks_df.sort_values(by='Deadline').reset_index(drop=True)

        ordered_tasks['Predicted_Priority'] = ordered_tasks['Deadline'].rank(method='dense').astype(int)

      
        ordered_tasks['task_score'] = ordered_tasks['Deadline'].apply(
            lambda deadline: (
                'high' if (deadline - datetime.now()).days < 2 else
                'medium' if (deadline - datetime.now()).days < 4 else
                'low'
            )
        )

        ordered_tasks['Time_Remaining'] = ordered_tasks['Deadline'].apply(
            lambda deadline: (
                f"{int((deadline - datetime.now()).total_seconds() // 3600)}h "
                f"{int(((deadline - datetime.now()).total_seconds() % 3600) // 60)}m"
                if (deadline - datetime.now()).total_seconds() > 0 else "0h 0m"
            )
        )
        
        result = ordered_tasks.to_dict(orient='records')
        for i, task in enumerate(result):
            task['task_name'] = task_name.iloc[i]

        return jsonify({"prioritized_tasks": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)