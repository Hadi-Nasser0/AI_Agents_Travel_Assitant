# AI Agents Travel Assistant

A multi-agent AI system built with **crewAI** that plans complete travel itineraries including flights, hotels, activities, and local advice.

## Quick Start

```bash
# Install dependencies
pip install -e .

# Run the travel planner (example: Paris trip)
python -m my_crew.main
# or
run_crew
```

## What It Does

This project uses 5 specialized AI agents working together:

- **Flight Agent** – Finds flight options
- **Hotel Agent** – Recommends hotels with amenities
- **Tour Agent** – Creates detailed 3-day itineraries
- **Advice Agent** – Provides travel tips and safety advice
- **Coordination Agent** – Compiles everything into a final report

## Example Output

See [`final_report.md`](final_report.md) for a sample 3-day family trip to Paris including flights, hotel, daily itinerary, and travel tips.

## Project Structure

```
AI_Agents_Travel_Assistant/
├── pyproject.toml          # Project config & dependencies
├── final_report.md         # Sample output (Paris trip)
├── src/
│   └── my_crew/
│       ├── main.py         # Entry point
│       ├── crew.py         # Crew & agent definitions
│       ├── config/
│       │   ├── agents.yaml # Agent roles & goals
│       │   └── tasks.yaml  # Task descriptions
│       └── tools/          # Custom tools (if any)
```

## Requirements

- Python 3.10+
- crewAI 0.193+
- OpenAI API key (set as `OPENAI_API_KEY` environment variable)

## License

MIT