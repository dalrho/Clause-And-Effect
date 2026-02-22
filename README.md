# Clause n Effect: Intelligent Contract Analyzer

The **Contract Intelligence Analyzer** uses advanced OCR and LLMs to transform dense legal jargon into actionable intelligence. It doesn't just tell you what the contract says; it tells you what the contract does.


## The Problem

Most people sign contracts based on trust or exhaustion, not understanding. Fine print often hides predatory clauses that only become visible when things go wrong.

## Status: Work in Progress
    Current Sprint: Implementing the API endpoints and configuring the database

## Development Roadmap
A roadmap shows you have a plan. Use standard Markdown checkboxes to show progress:

- [x] Phase 1: Ingestion - PDF to Text via OCR (Completed)

- [ ] Phase 2: Risk Mapping - Prompt engineering for "1-sentence risk" and "Heatmap" generation.

- [ ] Phase 3: The Simulator - Developing the "Counterfactual" logic engine.

- [ ] Phase 4: UI/UX - Building the Next.js dashboard for visual risk heatmaps.

## Known Challenges
Be transparent about what you’re still solving. It makes you look like a more sophisticated engineer.

- **Context Window Management**: Handling 100+ page contracts without losing the "thread."

- **OCR Accuracy**: Improving table-data extraction for complex fee schedules.

- **Hallucination Guardrails**: Ensuring the "Simulator" doesn't invent penalties that aren't there.