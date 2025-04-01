
# Green AI UX Pattern: Resource Usage Preview

> **Let’s make AI not just smart—but aware.**

This open project proposes a simple but impactful UX pattern: show users the estimated energy, time, and carbon cost *before* executing high-load AI tasks.

## Why?

Every day, millions of AI queries—image generation, video synthesis, LLM prompts—consume significant compute power. But users have no visibility into the resource impact of what they trigger.

With a simple UI preview, we can:
- Promote eco-conscious usage
- Save energy at scale
- Encourage AI that is both powerful and responsible

## Example Use Case

**Task:** Ghibli-style image generation  
**Estimates:**
- GPU time: ~12 seconds
- Electricity: ~0.005 kWh
- CO₂ Emissions: ~2.5g

**User Sees:**

    Estimated Resource Usage:
    • GPU: ~12s
    • Energy: ~0.005 kWh
    • CO₂: ~2.5g
    [ Proceed ]   [ Eco Mode ]   [ Cancel ]

## What's Inside

- `/mockups/` – Visual example of the UI
- `/src/` – Simple estimator logic (Python)
- `README.md` – This documentation
- `LICENSE` – MIT License (use freely, contribute openly)

## How You Can Help

- Fork and improve the estimator logic
- Build integrations with open-source AI frontends (like Hugging Face Spaces or Gradio)
- Design a browser extension to overlay resource info on AI platforms
- Suggest UX patterns, metrics, or real-time APIs

## License

MIT License – free to use, modify, and share.

---

Let’s push for a future where AI systems are not just intelligent, but *aware* of their environmental impact.

#GreenAI #SustainableAI #AIEthics #OpenUX
