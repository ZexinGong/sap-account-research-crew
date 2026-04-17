# SAP Account Research Crew

A multi-agent AI system built with CrewAI that prepares pre-meeting 
customer briefings for SAP Account Executives.

## Setup

1. Follow [CrewAI's official installation guide](https://docs.crewai.com/en/installation#text-tutorial) to install `python`, `uv`, and `crewai`.
2. Clone the repo, then in the project's root directory...
3. `python -m venv venv && source venv/bin/activate`
    > NOTE: python version should be >=3.10 and <3.14, as specified in the [official guide](https://docs.crewai.com/en/installation).
4. `pip install -r requirements.txt`
5. `cd crew`, then in `<root>/crew`...
6. Copy `.env.example` to `.env` and add your API keys
   - Groq API key: groq.com (free tier available)
   - Serper API key: serper.dev (free tier available)
   - Model: Any models accessible through your Groq API. Testing is conducted using `groq/llama-3.3-70b-versatile`
7. In `main.py`, replace `company` with the name of the company you'd like to research on.
8. `crewai install`, then `crewai run`.

## Example Outputs

### Prompt: `python main.py "Nvidia"`
[Paste actual output from your run here]

### Prompt: `python main.py "Volkswagen AG"`
[Paste second example here]
