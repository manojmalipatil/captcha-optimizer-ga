# 🧬 CAPTCHA Optimizer using Genetic Algorithms

This Python project uses a **Genetic Algorithm (GA)** to evolve **CAPTCHA images** that are *challenging for bots to solve* (like OCR systems such as Tesseract) but still **readable by humans**. It combines image generation, noise manipulation, and evolutionary principles to iteratively improve CAPTCHA designs.

---

## 🚀 Features

- 🎨 **Dynamic CAPTCHA Generation** using `captcha` library.
- 🔍 **OCR Evaluation** using `pytesseract` to simulate bot decoding attempts.
- 🧠 **Genetic Algorithm** for optimizing CAPTCHA text and noise parameters.
- 🔁 **Mutation & Crossover** to introduce variety and improve difficulty.
- 📈 **Fitness Function** prioritizes CAPTCHA designs unreadable by OCR.
- 🖼️ **Image Visualization** to preview generated CAPTCHAs.

---

## 🛠️ Installation

### 📦 Dependencies

Ensure Python 3.7+ is installed. Then install the required libraries:

```bash
pip install captcha pillow pytesseract numpy
```

Also, install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and configure its path:

```plaintext
Windows default path: C:\Program Files\Tesseract-OCR\tesseract.exe
```

Update this line in `main.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## 📂 File Structure

```
captcha-ga/
│
├── main.py            # Core implementation of the genetic algorithm
├── README.md          # You're reading it!
```

---

## 🧬 How It Works

1. **Initial Population:** Randomly generates 5-character CAPTCHA strings with random noise levels.
2. **Fitness Evaluation:** Uses OCR to test if the CAPTCHA can be decoded correctly.
3. **Selection:** Keeps the most difficult CAPTCHAs for bots (based on OCR results).
4. **Crossover:** Combines two CAPTCHAs to generate a new one (mix of characters + average noise).
5. **Mutation:** Occasionally introduces new characters or modifies noise.
6. **Iteration:** Repeats the process for multiple generations to evolve optimal designs.

---

## 🧪 Example Output

```bash
Generation 1: Best fitness = True
Generation 2: Best fitness = True
...
```

At the end, images from the final generation are shown using the default image viewer.

---

## 🧠 Customization

You can tweak:

- CAPTCHA string length
- Noise levels (range 0 to 3)
- Number of generations (`generations`)
- Population size (`population_size`)
- OCR config flags for stricter evaluation

---

## 📌 Use Cases

- Training CAPTCHA generation models
- Evaluating OCR model robustness
- Building more secure user verification mechanisms
- AI security and adversarial testing

---

## 📋 TODO / Improvements

- ✅ Add font and distortion variation
- 📈 Include human readability scoring
- 🧠 Combine with deep learning for smarter evolution
- 💾 Save/export generated CAPTCHA images
- 🌐 Optionally build a Flask web interface

---

## 📄 License

MIT License. Feel free to use and modify for research or personal use.

---

## 👨‍💻 Author

**Manoj Malipatil**  
Feel free to reach out for feedback, suggestions, or collaboration!
