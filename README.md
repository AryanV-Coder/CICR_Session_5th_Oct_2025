# CICR — Session (5th Oct 2025)
Taken by: Aryan Varshney ([GitHub](https://github.com/AryanV-Coder))

Short educational repository for a junior-level tech session covering modern multimodal tools and quick demos.

What this session covers
- Gemini (multimodal models) — concepts and demo scripts showing text, image, audio, and video handling.
- Streamlit — rapid UI for building simple demos and sharing interactive examples with juniors.
- Practical tips — how to wire input media, basic preprocessing, and safe prompts for demos.

Repository contents (high level)
- `main.py` — session launcher or primary demo runner (check code for details).
- `app.py` — example app (could be a Streamlit demo).
- `text_gemini.py`, `image_gemini.py`, `audio_gemini.py`, `video_gemini.py` — focused demo scripts for each modality.
- `img1.png`, `audio1.wav`, `video1.mp4` — sample media used by the demos.
- `requirements.txt` — Python dependencies (install with pip).

Quick setup
1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your API key (required to run the demos)

- Create a `.env` file in the project root and add your Gemini API key (used by the demo scripts):

```
GEMINI_API_KEY="your_api_key_here"
```

- (Optional but recommended for Streamlit) Create a `/.streamlit/secrets.toml` file with the same key so Streamlit apps can access it securely:

```
GEMINI_API_KEY = "your_api_key_here"
```

Note: After adding these files, restart any running Streamlit processes so the new secrets are picked up.

4. Run a demo (example):

```bash
streamlit run app.py
streamlit run main.py
```

Teaching notes for juniors
- Focus on fundamentals first: what multimodal models are, how they accept different input types, and when to use them.
- Keep demos minimal: one input type per script so learners can follow the data flow (load -> preprocess -> model -> postprocess -> display).
- Explain safety and cost: API rate limits, token usage, and safe prompting practices.
- Encourage experimentation: change sample inputs in `img1.png`, `audio1.wav`, and `video1.mp4`.

---
Created for a junior tech session on Gemini, Streamlit, and multimodal demos (5th Oct 2025).
