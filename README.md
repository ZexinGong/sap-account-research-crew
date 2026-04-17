# SAP Account Research Crew

A multi-agent AI system built with CrewAI that prepares pre-meeting 
customer briefings for SAP Account Executives.

## Setup

1. Follow [CrewAI's official installation guide](https://docs.crewai.com/en/installation#text-tutorial) to install `python`, `uv`, and `crewai`.
    > NOTE: python version should be >=3.10 and <3.14, as specified in the [official guide](https://docs.crewai.com/en/installation).
2. Copy `.env.example` to `.env` and add your API keys
   - Groq API key: groq.com (free tier available)
   - Serper API key: serper.dev (free tier available)
   - Model: Any models accessible through your Groq API. Testing is conducted using `groq/llama-3.3-70b-versatile`
3. Run the crew with a natural-language query, either by typing it when prompted or by setting `SAP_ACCOUNT_QUERY` before launch.
4. `crewai install` to install all dependencies.
5. `crewai run` to conduct research and generate the briefing. The final briefing is written to `output/customer_briefing.md`.

## Example

### Example query
"Prepare a customer briefing for Nvidia"

### Example output
See the attached `customer_briefing.md` in the output directory.
