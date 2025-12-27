
# Task Prioritization API

A lightweight Python project for predicting task attributes and priority levels from a dataset of tasks. The repository contains model weights, an example API, and scripts to run predictions.

**Project structure**
- `main.py`: Example entrypoint / runner for model predictions.
- `api/` : Contains an API example and `api.py` for serving the model.
- `data/`: Contains `Task_Prioritization_Dataset.csv` (sample dataset used for training/evaluation).
- `weights/`: Saved model artifacts organized by target (e.g., `Priority`, `Completion_Status`, `Task_Type`).
- `model1.ipynb`: Notebook with exploratory analysis or model experiments.
- `pyproject.toml`: Project metadata and dependency config.

## Features
- Predicts task priority and related attributes from task text and metadata.
- Pretrained model weights provided in the `weights/` folder.
- Simple REST API example to serve predictions (`api/api.py`).

## Requirements
- Python 3.8+
- Recommended: create a virtual environment.

Install dependencies (choose one):

Using pip with a requirements file (if you create one):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Using Poetry (if you prefer `pyproject.toml`):

```bash
poetry install
poetry shell
```

If no `requirements.txt` is included, install typical ML dependencies used in this repo:

```bash
pip install numpy pandas scikit-learn flask joblib
```

## Quick start

1. Activate your virtual environment.
2. Ensure `weights/` contains the model files for the target you want to predict.
3. Run the sample script:

```bash
python main.py
```

`main.py` should demonstrate loading models from `weights/` and running a sample prediction. If you prefer to run the API server, see below.

## Running the API

The `api/api.py` file provides a minimal Flask (or similar) server to serve predictions. Example usage:

```bash
# from project root
python api/api.py
```

Then POST JSON to the prediction endpoint; an example payload (adjust fields to match your model inputs):

```json
{
	"task_title": "Finish monthly report",
	"task_description": "Compile sales and expense figures for December",
	"metadata": {
		"estimated_time_hours": 3,
		"assignee": "alice"
	}
}
```

Example curl request:

```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"task_title":"Finish monthly report","task_description":"Compile sales and expense figures"}'
```

The API returns a JSON object containing predicted labels and confidence scores.

## Models & Weights

- Models are saved in the `weights/` directory. Subfolders include `Priority`, `Completion_Status`, and `Task_Type`.
- The code expects a serialized model file (e.g., joblib, pickle, or framework-specific format). Update the loading logic in `main.py` or `api/api.py` if you use a different format.

## Dataset

- The `data/Task_Prioritization_Dataset.csv` file contains the dataset used for training and evaluation. Inspect `model1.ipynb` for exploration and preprocessing steps.

## Notebook

- Open `model1.ipynb` to review data exploration, preprocessing, feature engineering, and model training experiments.

## Development

- To add or update a model, place new weights into `weights/<Target>/` and update loading code accordingly.
- Add unit tests or integration tests as needed.

## Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repository.
2. Create a topic branch (`git checkout -b feat/your-change`).
3. Make changes and add tests.
4. Open a pull request with a clear description.

## Troubleshooting

- If model loading fails, confirm the model file path and serialization format.
- For API issues, check which port is used and whether dependencies (Flask, etc.) are installed.

## License & Contact

Specify your license here (e.g., MIT) and contact details.

---

If you'd like, I can:
- run the API locally and show a sample prediction, or
- add a `requirements.txt` generated from `pyproject.toml`, or
- update `main.py`/`api/api.py` with explicit model-loading code examples.

