import json
from main import build_graph

def run_evaluation():
    with open("evaluation/test_data.json") as f:
        test_cases = json.load(f)

    graph_func = build_graph()
    results = []
    for case in test_cases:
        state = {"news": case}
        result = graph_func(state)
        results.append(result["final_analysis"])

    with open("evaluation/results.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    run_evaluation()
