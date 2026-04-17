#!/usr/bin/env python
import os
import sys
import warnings

from .crew import SapAccountResearchCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

DEFAULT_QUERY = "Prepare a customer briefing for Nvidia"


def _build_inputs(query: str) -> dict[str, str]:
    return {"query": query}


def _resolve_query() -> str:
    try:
        query = input("Enter a natural-language account query: ").strip()
    except EOFError:
        query = ""

    return query or DEFAULT_QUERY

def run():
    """
    Run the crew.
    """
    inputs = _build_inputs(_resolve_query())

    try:
        result = SapAccountResearchCrew().crew().kickoff(inputs=inputs)
        print(result)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = _build_inputs(DEFAULT_QUERY)
    try:
        SapAccountResearchCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SapAccountResearchCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = _build_inputs(DEFAULT_QUERY)

    try:
        SapAccountResearchCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    query = trigger_payload.get("query") or trigger_payload.get("company") or DEFAULT_QUERY

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "query": query,
    }

    try:
        result = SapAccountResearchCrew().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
